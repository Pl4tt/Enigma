import re
import random
from constants import ALPHABET

from message import Message
from reflector import Reflector
from rotor import Rotor


class Enigma:
    def __init__(
        self,
        rotors: Rotor,
        reflector: Reflector,
        plug_connections: dict[str, str],
        number_repr: dict[str, str]
    ) -> None:
        self.rotors = rotors
        self.ring_settings = "".join([rotor.ring_settings for rotor in self.rotors])
        self.reflector = reflector
        self.plug_connections = plug_connections
        self.number_repr = number_repr

    def set_settings(
        self,
        rotors: Rotor,
        ring_settings: list[str],
        reflector: Reflector,
        plug_connections: dict[str, str]
    ) -> None:
        self.rotors = rotors
        self.reflector = reflector
        self.plug_connections = plug_connections
        
        for i, rotor in enumerate(self.rotors):
            rotor.ring_settings = ring_settings[i]

    def encrypt_decrypt_char(self, char: str) -> str:
        if self.rotors[0].rotate():  # rotate rotors
            if self.rotors[1].rotate():
                self.rotors[2].rotate()

        if char in self.plug_connections.keys():  # connect plugs
            char = self.plug_connections.get(char)

        index = ord(char) - 65
        for rotor in self.rotors:  # through rotors
            match_char = rotor.in_order[index]
            index = rotor.out_order.index(match_char)

        # reflector
        match_char = self.reflector.in_order[index]
        index = self.reflector.out_order.index(match_char)

        for rotor in self.rotors[::-1]:  # backwards through rotors
            match_char = rotor.out_order[index]
            index = rotor.in_order.index(match_char)
        
        char = chr(index+65)  # set new char
        
        if char in self.plug_connections.keys():  # connect plugs
            char = self.plug_connections.get(char)
            
        return char

    def encrypt_decrypt_rotor_start(self, rotor_start: str, secret_rotor_start: str) -> str:
        for i, rotor in enumerate(self.rotors[::-1]):
            rotor.set_start(rotor_start[i])

        return "".join([self.encrypt_decrypt_char(char) for char in secret_rotor_start])

    def encrypt(self, message: str, time: int, authorization: str, rotor_start: list[str]) -> Message:
        # clean up message
        message = message.strip().upper()

        for key, val in self.number_repr.items():
            message = message.replace(key, val)

        message = message.replace(" ", "X").replace("CH", "Q").replace("CK", "Q")
        message = message.replace("Ü", "UE").replace("Ä", "AE").replace("Ö", "OE")
        message = message.replace(".", "").replace("?", "").replace("!", "").replace(",", "X")

        message = re.sub(r"[^A-Z]", "", message)
        
        set_start_rotor = rotor_start[1][:]
        # set check key
        rotor_start[1] = self.encrypt_decrypt_rotor_start(*rotor_start)

        for i, rotor in enumerate(self.rotors):  # set rotor_start
            rotor.set_start(set_start_rotor[i])

        encrypted_text = ALPHABET[random.randint(0, 25)] + ALPHABET[random.randint(0, 25)] + authorization

        for char in message:  # encrypt message
            encrypted_text += self.encrypt_decrypt_char(char)

        length = len(encrypted_text)

        return Message(
            {
                "time": time,
                "length": length,
                "check_key": rotor_start
            },
            encrypted_text
        )

    def decrypt(self, message: Message, authorization: str) -> str:
        if message.header.get("length") != len(message.text):
            raise Exception("The length of the message does not match the length inside the message header :(")
        
        if "".join(sorted(message.text[2:5])) != authorization:
            raise Exception("Your authorization code is not high enough to decrypt the message.")
        
        text = message.text[5:]
        
        rotor_start = message.header.get("check_key")
        rotor_start[1] = self.encrypt_decrypt_rotor_start(*rotor_start)

        for i, rotor in enumerate(self.rotors):  # set rotor_start
            rotor.set_start(rotor_start[1][i])
        
        decrypted_text = ""

        for char in text:  # decrypt message
            decrypted_text += self.encrypt_decrypt_char(char)
            
        decrypted_text = decrypted_text.replace("X", " ").replace("Q", "CH").replace("Q", "CK")
        decrypted_text = decrypted_text.replace("UE", "Ü").replace("AE", "Ä").replace("OE", "Ö")

        return decrypted_text



