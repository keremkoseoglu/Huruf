from model import huruf, kuran
import os
import nltk
from nltk.corpus import stopwords

class HurufWordCount:

    _HTML_PATH = "/Users/Kerem/Downloads/hwc.html"
    _IGNORE_WORDS = {
        "a",
        "allah",
        "among",
        "and",
        "are",
        "at",
        "away",
        "be",
        "behold",
        "besides",
        "brought",
        "but",
        "came",
        "do",
        "ever",
        "every",
        "for",
        "from",
        "hast",
        "hath",
        "have",
        "he",
        "his",
        "if",
        "in",
        "indeed",
        "is",
        "it",
        "lord",
        "made",
        "may",
        "no",
        "nor",
        "not",
        "of",
        "on",
        "one",
        "people",
        "said",
        "say",
        "says",
        "see",
        "sent",
        "shall",
        "take",
        "that",
        "the",
        "thee",
        "their",
        "them",
        "they",
        "things",
        "those",
        "thou",
        "thy",
        "to",
        "truly",
        "unto",
        "upon",
        "us",
        "we",
        "well",
        "what",
        "who",
        "will",
        "with",
        "would",
        "ye",
        "yea",
        "you"
    }

    def __init__(self):
        self._huruf = huruf.get_huruf_list()
        self._sure = kuran.Kuran().get_sure_with_any_huruf()
        self._html_content = ""

    def execute(self):
        self._open_html()
        self._verse_based_count()

        # todo 550
        # huruf bazında toplam kelime sayıları

        self._close_html()
        self._write_html()
        self._show_html()

    def _close_html(self):
        self._html("</body></html>")

    def _html(self, text:str):
        self._html_content += text

    def _open_html(self):
        self._html("<html><head></head><body>")

    def _show_html(self):
        os.system("open " + self._HTML_PATH)

    def _verse_based_count(self):
        self._html("<hr><h1>Verse based count</h1>")

        #nltk.download("stopwords")
        sw = set(stopwords.words("english"))

        for s in self._sure:
            self._html("<hr><br>")
            self._html("<h2>" + s.get_name() + "</h2>")

            for huruf in s.get_hurufs():
                self._html(huruf.get_letter() + " ")
            self._html("<br><br>")

            word_count = s.get_word_occurrence_count(language="EN")
            max_count = 0
            for word in word_count:
                if word in sw or word in self._IGNORE_WORDS:
                    continue
                count = word_count[word]
                if count > max_count:
                    max_count = count

            for word in word_count:
                if word in sw or word in self._IGNORE_WORDS:
                    continue
                count = word_count[word]
                font_size = int((count / max_count) * 28)
                if font_size < 1:
                    font_size = 1
                self._html("<span style='font-size:" + str(font_size) + "px'>" + word + " </span>")
                #<sup><font size=1>(" + str(count) + ")</font></sup>

        # todo 450
        pass

    def _write_html(self):
        file = open(self._HTML_PATH, "w")
        file.write(self._html_content)
        file.close()
