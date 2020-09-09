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
        print(self.output)

# Testing Zone --------------------------------------------------------------------------------------

# With the 4 lines defining our translations tables we can now easily translate between hiragana and katakana
# mixed_string = 'きゃりーぱみゅぱみゅは日本の歌手です。'
# print(mixed_string.translate(hiragana_to_katakana))
# print(mixed_string.translate(hiragana_to_katakana).translate(katakana_to_hiragana))
# out: きゃりーぱみゅぱみゅは日本の歌手です。

obj = Transliterator('きゃりーぱみゅぱみゅは日本の歌手です。')
obj.hiragana_to_katakana()
obj.show()
obj.katakana_to_hiragana()
obj.show()