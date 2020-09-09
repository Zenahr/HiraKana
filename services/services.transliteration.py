# coding=utf8



# API ------------------------------------------------------------------------------------------------

class Transliterator:
    def __init__(self, input):
        self.__init_translators()
        self.input = input
        self.output = self.input # so that show() prints the input when no translator has yet been applied to self.input

    def __init_translators(self):
        katakana_syllables = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
        hiragana_syllables = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
        self.hiragana_to_katakana_table = str.maketrans(hiragana_syllables, katakana_syllables)
        self.katakana_to_hiragana_table = str.maketrans(katakana_syllables, hiragana_syllables)

    def hiragana_to_katakana(self):
        self.output = self.input.translate(self.hiragana_to_katakana_table)
        return self.output

    def katakana_to_hiragana(self):
        self.output = self.input.translate(self.katakana_to_hiragana_table)
        return self.output

    def show(self):
        print("RESULT:", self.output)

# Testing Zone --------------------------------------------------------------------------------------

obj = Transliterator("TESTSTRING")
obj.show()
print(obj.hiragana_to_katakana())
obj.hiragana_to_katakana
obj.show()