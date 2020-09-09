# coding=utf8

katakana_syllables = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
hiragana_syllables = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
syllable_mapping = {'ァ': 'ぁ', 'ア': 'あ', 'ィ': 'ぃ', 'イ': 'い', 'ゥ': 'ぅ', 'ウ': 'う', 'ェ': 'ぇ', 'エ': 'え', 'ォ': 'ぉ', 'オ': 'お', 'カ': 'か', 'ガ': 'が', 'キ': 'き', 'ギ': 'ぎ', 'ク': 'く', 'グ': 'ぐ', 'ケ': 'け', 'ゲ': 'げ', 'コ': 'こ', 'ゴ': 'ご', 'サ': 'さ', 'ザ': 'ざ', 'シ': 'し', 'ジ': 'じ', 'ス': 'す', 'ズ': 'ず', 'セ': 'せ', 'ゼ': 'ぜ', 'ソ': 'そ', 'ゾ': 'ぞ', 'タ': 'た', 'ダ': 'だ', 'チ': 'ち', 'ヂ': 'ぢ', 'ッ': 'っ', 'ツ': 'つ', 'ヅ': 'づ', 'テ': 'て', 'デ': 'で', 'ト': 'と', 'ド': 'ど', 'ナ': 'な', 'ニ': 'に', 'ヌ': 'ぬ','ネ': 'ね', 'ノ': 'の', 'ハ': 'は', 'バ': 'ば', 'パ': 'ぱ', 'ヒ': 'ひ', 'ビ': 'び', 'ピ': 'ぴ', 'フ': 'ふ', 'ブ': 'ぶ', 'プ': 'ぷ', 'ヘ': 'へ', 'ベ': 'べ', 'ペ': 'ぺ', 'ホ': 'ほ', 'ボ': 'ぼ', 'ポ': 'ぽ', 'マ': 'ま', 'ミ': 'み', 'ム': 'む', 'メ': 'め', 'モ': 'も', 'ャ': 'ゃ', 'ヤ': 'や', 'ュ': 'ゅ', 'ユ': 'ゆ', 'ョ': 'ょ', 'ヨ': 'よ', 'ラ': 'ら', 'リ': 'り', 'ル': 'る', 'レ': 'れ', 'ロ': 'ろ', 'ヮ': 'ゎ', 'ワ': 'わ', 'ヰ': 'ゐ', 'ヱ': 'ゑ', 'ヲ': 'を', 'ン': 'ん', 'ヴ': 'ゔ', 'ヵ': 'ゕ', 'ヶ': 'ゖ', 'ヽ': 'ゝ', 'ヾ': 'ゞ'}

hiragana_to_katakana = str.maketrans(hiragana_syllables, katakana_syllables)
katakana_to_hiragana = str.maketrans(katakana_syllables, hiragana_syllables)

# With the 4 lines defining our translations tables we can now easily translate between hiragana and katakana
mixed_string = 'きゃりーぱみゅぱみゅは日本の歌手です。'
print(mixed_string.translate(hiragana_to_katakana))
# out: キャリーパミュパミュハ日本ノ歌手デス。

# translating back to hiragana gives us the expected result, because we didn't add every katakana and hiragana code block to the translation charts
print(mixed_string.translate(hiragana_to_katakana).translate(katakana_to_hiragana))
# out: きゃりーぱみゅぱみゅは日本の歌手です。

# API ------------------------------------------------------------------------------------------------

class Transliterator:
    def __init__(self, input):
        self.input = input

    def katakana_to_hiragana(self, input):
        pass

    def show(self):
        print("Input String:", self.input)

# Testing Zone --------------------------------------------------------------------------------------

obj = Transliterator("TESTSTRING")
obj.show()