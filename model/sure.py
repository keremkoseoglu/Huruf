from model.ayet import Ayet
from model import huruf, kuran

class Sure:

    def __init__(self, index: int, name="", ayet=[]):
        self._name = name
        self._index = index
        self._ayet = []

        self._hurufs = []
        self._huruf_seeked = False

    def append_ayet(self, ayet: Ayet):
        self._ayet.append(ayet)

    def get_ayets(self) -> []:
        return self._ayet

    def get_ayets_as_text(self, with_line_break=True, language="TR") -> str:
        output = ""

        sure = kuran.Kuran().get_single_sure(self._index, language=language)

        for ayet in sure.get_ayets():
            output += ayet.get_text()
            if with_line_break:
                output += "\n"
            else:
                output += " "
        if not with_line_break:
            output = output.replace("\n", " ")
            output = output.replace("\r", " ")
        return output

    def get_huruf_count(self) -> int:
        return len(self.get_hurufs())

    def get_hurufs(self) -> []:
        if not self._huruf_seeked:
            self._hurufs = huruf.get_hurufs_in_text(self._ayet[0].get_text())
            self._huruf_seeked = True
        return self._hurufs

    def get_hurufs_as_str_tuple(self) -> ():
        hurufs = self.get_hurufs()
        huruf_list = []
        for huruf_obj in hurufs:
            huruf_list.append(huruf_obj.get_letter())
        return tuple(huruf_list)

    def get_name(self) -> str:
        return self._name

    def get_sum_of_huruf_alphabet_order(self) -> int:
        output = 0
        for h in self._hurufs:
            output += h.get_alphabet_order()
        return output

    def get_word_occurrence_count(self, language="TR") -> {}:
        output = {}
        text = self.get_ayets_as_text(language=language)
        word = ""

        for i in range(len(text)):
            letter = text[i:i+1]
            if letter.isalpha():
                word += letter
            else:
                if word != "":
                    word = word.lower()
                    if word in output:
                        count = output[word]
                        count += 1
                        output[word] = count
                    else:
                        output[word] = 1
                    word = ""

        return output

    def has_any_huruf(self) -> bool:
        return len(self.get_hurufs()) > 0

    def has_huruf(self, huruf: str) -> bool:
        for huruf_obj in self.get_hurufs():
            if huruf_obj.get_letter() == huruf:
                return True
        return False

    def has_single_huruf(self) -> bool:
        return self.get_huruf_count() == 1

    def set_name(self, name: str):
        self._name = name