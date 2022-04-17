from constants import ALPHABET
from reflector import Reflector


class Rotor(Reflector):
    def __init__(self, ring_settings: str, in_order: list[str], out_order: list[str]=None) -> None:
        super().__init__(in_order, out_order)
        self.ring_settings = ring_settings

    def rotate(self) -> bool:
        self.in_order.append(self.in_order[0])
        self.in_order.remove(self.in_order[0])
        
        self.out_order.append(self.out_order[0])
        self.out_order.remove(self.out_order[0])
        
        return True if self.ring_settings == self.in_order[0] else False
    
    def set_start(self, start: str) -> None:
        if start not in ALPHABET:
            raise ValueError("start must be a capital letter in the alphabet.")

        while self.out_order[0] != start:
            self.rotate()