# coding=utf8



# API ------------------------------------------------------------------------------------------------

class Transliterator:
    def __init__(self, input):
        self.__init_translators()
        self.input = input

    def __init_translators(self):
        katakana_syllables = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
        hiragana_syllables = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
        self.hiragana_to_katakana_table = str.maketrans(hiragana_syllables, katakana_syllables)
        self.katakana_to_hiragana_table = str.maketrans(katakana_syllables, hiragana_syllables)

    def hiragana_to_katakana(self):
        return self.input.translate(hiragana_to_katakana_table)

    def katakana_to_hiragana(self):
        return self.input.translate(katakana_to_hiragana_table)

    def show(self):
        print("Input String:", self.input)

# Testing Zone --------------------------------------------------------------------------------------

obj = Transliterator("TESTSTRING")
obj.show()