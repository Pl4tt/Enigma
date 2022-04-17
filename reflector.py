from constants import ALPHABET


class Reflector:
    def __init__(self, in_order: list[str], out_order: list[str]=None) -> None:
        if out_order is None:
            out_order = list(ALPHABET)

        if len(in_order) != len(out_order):
            del self
            return
        
        self.in_order = in_order
        self.out_order = out_order