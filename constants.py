ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ROTOR_IN = {
    "I": ["E", "K", "M", "F", "L", "G", "D", "Q", "V", "Z", "N", "T", "O", "W", "Y", "H", "X", "U", "S", "P", "A", "I", "B", "R", "C", "J"],
    "II": ["A", "J", "D", "K", "S", "I", "R", "U", "X", "B", "L", "H", "W", "T", "M", "C", "Q", "G", "Z", "N", "P", "Y", "F", "V", "O", "E"],
    "III": ["B", "D", "F", "H", "J", "L", "C", "P", "R", "T", "X", "V", "Z", "N", "Y", "E", "I", "W", "G", "A", "K", "M", "U", "S", "Q", "O"],
    "IV": ["E", "S", "O", "V", "P", "Z", "J", "A", "Y", "Q", "U", "I", "R", "H", "X", "L", "N", "F", "T", "G", "K", "D", "C", "M", "W", "B"],
    "V": ["V", "Z", "B", "R", "G", "I", "T", "Y", "U", "P", "S", "D", "N", "H", "L", "X", "A", "W", "M", "J", "Q", "O", "F", "E", "C", "K"],
}
REFLECTOR_IN = {
    "A": ["E", "J", "M", "Z", "A", "L", "Y", "X", "V", "B", "W", "F", "C", "R", "Q", "U", "O", "N", "T", "S", "P", "I", "K", "H", "G", "D"],
    "B": ["Y", "R", "U", "H", "Q", "S", "L", "D", "P", "X", "N", "G", "O", "K", "M", "I", "E", "B", "F", "Z", "C", "W", "V", "J", "A", "T"],
    "C": ["F", "V", "P", "J", "I", "A", "O", "Y", "E", "D", "R", "Z", "X", "W", "G", "C", "T", "K", "U", "Q", "S", "B", "N", "M", "H", "L"],
}

plug_connections28 = {
    "C": "R",
    "R": "C",
    "V": "P",
    "P": "V",
    "A": "I",
    "I": "A",
    "K": "D",
    "D": "K",
    "O": "T",
    "T": "O",
    "M": "Q",
    "Q": "M",
    "E": "U",
    "U": "E",
    "B": "X",
    "X": "B",
    "L": "P", 
    "P": "L",
    "G": "J",
    "J": "G",
}
plug_connections29 = {
    "A": "D",
    "D": "A",
    "C": "N",
    "N": "C",
    "E": "T",
    "T": "E",
    "F": "L",
    "L": "F",
    "G": "I",
    "I": "G",
    "J": "V",
    "V": "J",
    "K": "Z",
    "Z": "K",
    "P": "U",
    "U": "P",
    "Q": "Y",
    "Y": "Q",
    "W": "X",
    "X": "W"
}

number_repr = {
    "0": "NULL",
    "1": "EINS",
    "2": "ZWEI",
    "3": "DREI",
    "4": "VIER",
    "5": "FÜNF",
    "6": "SECHS",
    "7": "SIEBEN",
    "8": "ACHT",
    "9": "NEUN"
}