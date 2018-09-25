

_CHARACTER_REPLACEMENTS = {
        "Â": "A",
        "â": "a",
        "î": "i",
        "û": "u"
    }


def _get_cleansed_text(text: str) -> str:
    output = text
    for replacement in _CHARACTER_REPLACEMENTS:
        output = output.replace(replacement, _CHARACTER_REPLACEMENTS[replacement])
    return output


class Ayet:

    def __init__(self, text:str):
        self._text = _get_cleansed_text(text)

    def get_text(self) -> str:
        return self._text

    def set_text(self, text:str):
        self._text = text