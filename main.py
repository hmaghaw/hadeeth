# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Hadith():
    def __init__(self):
        self.ommhat_elmoamneen = ["أم سلمة",
                             "عائشة"
                             ]

        self.hadeeth_starter = ["أن النبي",
                           "قال النبي",
                           "أن رسول",
                           "أن النبي",
                           "كان النبي",
                           "خرج علينا رسول",
                           "خرج رسول",
                                "أنه قال"
                            ]
        self.from_words = ["حدثنا",
                           "أخبرنا",
                           "أخبرني",
                           "سمعت",
                           "سمع",
                           "حدثته",
                           "أن "
                           ]
        self.bukhary_text = self.read_bukhary()
        self.bukhary = {}

    def read_bukhary(self):
        file_name = "data/bukhary.txt"
        f = open(file_name, encoding='utf8')
        data = f.read()
        ahadeeth = data.split("#")
        return ahadeeth

    def get_sanad(self,sanad_text):
        result = sanad_text
        for from_word in self.from_words:
            result = result.replace(from_word, "عن")
        result = result.replace(":","").replace("،","").replace(" قال","").replace("يقول","")
        res = result.split("عن")
        response = []
        for rawy in res:
            if len(rawy.strip())>0:
                response.append(rawy.strip())
        return response

    def ommahat_elmoameneen_hadeeth(self, om, text):
        sanad_text = text[1:text.rindex(om)+len(om)]
        sanad = self.get_sanad(sanad_text)
        nass = text[text.rindex(om)+len(om):]
        return sanad, nass

    def split_hadeeth(self,text):
        found=False
        for starter in self.hadeeth_starter:
            try:
                index = text.index(starter)
                sanad_text = text[1:index]
                sanad = self.get_sanad(sanad_text)
                nass = text[index:]
                found = True
                break
            except Exception as e:
                pass
        if not found:
            index = text.rindex("قال:")
            sanad_text = text[1:index]
            sanad = self.get_sanad(sanad_text)
            nass = text[index:]

        return sanad,nass

    def is_om_hadeeth(self, text):
        result = None
        for om in self.ommhat_elmoamneen:
            if om in text:
                result = om
                break
        return result

    def process_hadeeth(self, hadeeth):
        x = hadeeth.split("-")
        rest = x[1]
        hadith_number = x[0].strip()
        om = self.is_om_hadeeth(rest)
        if om != None:
            sanad, nass = self.ommahat_elmoameneen_hadeeth(om, rest)
        else:
            sanad, nass = self.split_hadeeth(rest)
        return hadith_number, sanad, nass

    def process_bukhary(self):
        for hadeeth in self.bukhary_text:
            hadith_number, sanad, nass = self.process_hadeeth(hadeeth.replace("\n",""))
            self.bukhary[hadith_number]={"full":hadeeth,"sanad":sanad,"nass":nass}


def run(name):
    h = Hadith()
    h.process_bukhary()
    print("")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
