

_LETTERS = [
    "elif", # 1
    "be",   # 2
    "te",   # 3
    "se",   # 4
    "cim",  # 5
    "ha",   # 6
    "hı",   # 7
    "dal",  # 8
    "zel",  # 9
    "ra",   # 10
    "ze",   # 11
    "sin",  # 12
    "şın",  # 13
    "sad",  # 14
    "dad",  # 15
    "ta",   # 16
    "zı",   # 17
    "ayn",  # 18
    "gayn", # 19
    "fe",   # 20
    "kaf",  # 21
    "kef",  # 22
    "lam",  # 23
    "mim",  # 24
    "nun",  # 25
    "vav",  # 26
    "he",   # 27
    "ya"    # 28
]


def get_index_of_letter(letter: str) -> int:
    return _LETTERS.index(letter)

def get_order_of_letter(letter: str) -> int:
    return get_index_of_letter(letter) + 1