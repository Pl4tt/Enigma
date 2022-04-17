from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from constants import ROTOR_IN, REFLECTOR_IN, plug_connections28, plug_connections29, number_repr


def test_single_char():
    # INITIAL SETUP
    reflector_b = Reflector(REFLECTOR_IN["B"])

    rotor5 = Rotor("Z", ROTOR_IN["V"])
    rotor3 = Rotor("V", ROTOR_IN["III"])
    rotor2 = Rotor("E", ROTOR_IN["II"])
    
    rotor5.set_start("C")
    rotor3.set_start("B")
    rotor2.set_start("A")

    enigma = Enigma([rotor5, rotor3, rotor2], reflector_b, plug_connections28, number_repr)

    # TESTS
    assert enigma.encrypt_decrypt_char("K") == "P"
    assert enigma.encrypt_decrypt_char("R") == "Y"

def test_text_encryption_decryption():
    # INITIAL SETUP
    reflector_b = Reflector(REFLECTOR_IN["B"])

    rotor3 = Rotor("H", ROTOR_IN["III"])
    rotor4 = Rotor("Z", ROTOR_IN["IV"])
    rotor1 = Rotor("P", ROTOR_IN["I"])

    enigma = Enigma([rotor3, rotor4, rotor1], reflector_b, plug_connections29, number_repr)

    # TEST 1
    raw = "Das Oberkommando der Wehrmacht gibt bekannt: Aachen ist gerettet. Durch gebündelten Einsatz der Hilfskräfte konnte die Bedrohung abgewendet und die Rettung der Stadt gegen 18:00 Uhr sichergestellt werden."
    msg = enigma.encrypt(raw, 2040, "OVW", ["QWE", "RTZ"])
    
    assert msg.header == {"time": 2040, "length": 214, "check_key": ["QWE", "HGR"]}
    
    dec_msg = enigma.decrypt(msg, "OVW")
    
    assert dec_msg == "DAS OBERKOMMANDO DER WEHRMACHT GIBT BEKANNT AACHEN IST GERETTET DURCH GEBÜNDELTEN EINSATZ DER HILFSKRÄFTE KONNTE DIE BEDROHUNG ABGEWENDET UND DIE RETTUNG DER STADT GEGEN EINSACHTNULLNULL UHR SICHERGESTELLT WERDEN"
    
    # TEST 2
    raw = "This is a message written by me to test the encryption/decryption algorithm."
    msg = enigma.encrypt(raw, 1830, "ZWF", ["ABC", "WWZ"])

    assert msg.header == {"time": 1830, "length": 79, "check_key": ["ABC", "KKW"]}

    dec_msg = enigma.decrypt(msg, "FWZ")

    assert dec_msg == "THIS IS A MESSAGE WRITTEN BY ME TO TEST THE ENCRYPTIONDECRYPTION ALGORITHM"

    

if __name__ == "__main__":
    test_single_char()
    test_text_encryption_decryption()
