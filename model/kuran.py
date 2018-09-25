from xml.dom import minidom
from model.sure import Sure
from model.ayet import Ayet
from model import huruf as model_huruf

class Kuran:

    _DATA_FILE_EN = "/Users/kerem/Dropbox/Software/Kerem/Development/Huruf/data/kuran-en.xml"
    _DATA_FILE = "/Users/kerem/Dropbox/Software/Kerem/Development/Huruf/data/kuran.xml"

    def __init__(self):
        self._sure = self._get_sure_list_from_file(self._DATA_FILE)
        self._sure_en = self._get_sure_list_from_file(self._DATA_FILE_EN)

    def get_huruf_tuple_alphabet_order(self) -> {}:
        output = {}
        for sure in self.get_sure_with_any_huruf():
            huruf_tuple = sure.get_hurufs_as_str_tuple()
            if huruf_tuple in output:
                continue
            alphabet_order_list = []
            for huruf_obj in sure.get_hurufs():
                alphabet_order_list.append(huruf_obj.get_alphabet_order())
            output[huruf_tuple] = alphabet_order_list
        return output

    def get_huruf_tuple_sure_dict(self) -> {}:
        output = {}
        for sure in self.get_sure_with_any_huruf():
            huruf_tuple = sure.get_hurufs_as_str_tuple()
            if huruf_tuple not in output:
                output[huruf_tuple] = []
            output[huruf_tuple].append(sure)
        return output

    def get_huruf_sure_dict(self) -> {}:
        output = {}
        for huruf_obj in model_huruf.get_huruf_list():
            huruf_letter = huruf_obj.get_letter()
            output[huruf_letter] = []
            for sure in self.get_sure_with_huruf(huruf_letter):
                output[huruf_letter].append(sure)
        return output

    def get_single_sure(self, index: int, language="TR") -> Sure:
        return self.get_sure(language)[index]

    def get_sure(self, language="TR") -> []:
        if language == "TR":
            return self._sure
        elif language == "EN":
            return self._sure_en
        else:
            assert False

    def get_sure_and_huruf_analysis(self) -> []:
        output = []
        for sure in self.get_sure_with_any_huruf():
            output_dict = {
                "sure_obj": sure,
                "sure_name": sure.get_name(),
                "has_single_huruf": sure.has_single_huruf(),
                "hurufs": sure.get_hurufs(),
                "huruf_count": sure.get_huruf_count(),
                "huruf_alphabet_order_count": sure.get_sum_of_huruf_alphabet_order()
            }
            output.append(output_dict)
        return output

    def get_sure_with_any_huruf(self) -> []:
        output = []
        for sure in self._sure:
            if sure.has_any_huruf():
                output.append(sure)
        return output

    def get_sure_with_huruf(self, huruf: str) -> []:
        output = []
        for sure in self._sure:
            if sure.has_huruf(huruf):
                output.append(sure)
        return output

    def get_sure_with_single_huruf(self) -> []:
        output = []
        for sure in self.get_sure_with_any_huruf():
            if sure.has_single_huruf():
                output.append(sure)
        return output

    def _get_sure_list_from_file(self, file_name: str) -> []:
        output = []
        book_xml = minidom.parse(file_name)
        chapters = book_xml.getElementsByTagName("Chapter")
        index = 0
        for chapter in chapters:
            sure = Sure(index, name=chapter.attributes["ChapterName"].nodeValue)
            for verse in chapter.getElementsByTagName("Verse"):
                sure.append_ayet(Ayet(verse.childNodes[0].data))
            output.append(sure)
            index = index + 1
        return output
