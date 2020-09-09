# coding=utf8

from components.transliteration import Transliterator as tl
from components.texts import urashimatarou as test_story

transliterator = tl()
katakana = transliterator.hiragana_to_katakana(test_story)
transliterator.show()
transliterator.write_to_file("test.txt", katakana)