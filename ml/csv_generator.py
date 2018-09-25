from model import huruf, kuran
import random
import os

class CsvGenerator:

    _DATA_PATH = "/Users/kerem/Dropbox/Software/Kerem/Development/Huruf/data"
    _ALL_FILE = "ml_all.csv"
    _TEST_FILE = "ml_test.csv"
    _TRAIN_FILE = "ml_train.csv"
    _TEST_PERCENTAGE = 20

    def __init__(self):
        self._all_content  =""
        self._test_content = ""
        self._train_content = ""

        self._all_sure = []
        self._train_sure = []
        self._test_sure = []

        self._huruf = huruf.get_huruf_list()
        self._kuran = kuran.Kuran()
        self._sure_with_huruf = self._kuran.get_sure_with_any_huruf()

    def generate(self):
        self._train_test_split()

        self._all_content = self._get_content(self._all_sure)
        self._train_content = self._get_content(self._train_sure)
        self._test_content = self._get_content(self._test_sure)

        self._write_file(self._ALL_FILE, self._all_content)
        self._write_file(self._TRAIN_FILE, self._train_content)
        self._write_file(self._TEST_FILE, self._test_content)

    def _get_content(self, sures: []) -> str:

        output = '"sure","content"'

        for h in self._huruf:
            output += ',"' + h.get_letter() + '"'

        for sure in sures:
            ayet_text = sure.get_ayets_as_text(with_line_break=False, language="EN")
            ayet_text = ayet_text.replace('"', '')

            output += "\n"
            output += '"' + sure.get_name() + '"'
            output += ',"' + ayet_text + '"'
            for h in self._huruf:
                output += ','
                if sure.has_huruf(h.get_letter()):
                    output += "1"
                else:
                    output += "0"

        return output

    def _train_test_split(self):
        self._all_sure = []
        self._train_sure = []
        self._test_sure = []

        sure_with_huruf = self._kuran.get_sure_with_any_huruf()

        test_count = int(len(self._sure_with_huruf) * self._TEST_PERCENTAGE / 100)
        train_count = len(self._sure_with_huruf) - test_count

        for i in range(train_count):
            random_pos = random.randint(0, len(sure_with_huruf) - 1)
            train_sure = sure_with_huruf.pop(random_pos)
            self._all_sure.append(train_sure)
            self._train_sure.append(train_sure)

        for remain_sure in sure_with_huruf:
            self._all_sure.append(remain_sure)
            self._test_sure.append(remain_sure)

    def _write_file(self, name: str, content: str):
        full_path = os.path.join(self._DATA_PATH, name)
        file = open(full_path, "w")
        file.write(content)
        file.close()
