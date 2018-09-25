from model import arabic_alphabet

_HURUFS = [
    "ayn",
    "elif",
    "ha",
    "kaf",
    "lam",
    "mim",
    "nun",
    "ra",
    "ta",
    "sad",
    "sin",
    "ya"
]


def get_huruf_list() -> []:
    output = []
    for letter in _HURUFS:
        output.append(Huruf(letter))
    return output


def get_hurufs_in_text(text: str) -> []:
    output = []

    words = text.split(" ")
    for word in words:
        cleansed_word = word.replace(".", "").replace(",", "").lower()
        if cleansed_word in _HURUFS:
            output.append(Huruf(cleansed_word))

    return output


class Huruf:

    def __init__(self, letter: str):
        self._letter = letter
        self._alphabet_order = arabic_alphabet.get_order_of_letter(self._letter)

    def get_alphabet_order(self) -> int:
        return self._alphabet_order

    def get_letter(self) -> str:
        return self._letter