import unittest
import deep_translator

def EnglishToFrench(str: str) -> str:
    retStr = deep_translator.GoogleTranslator(source='en', target='fr').translate(str)
    return retStr

class TestToEnglishTranslations(unittest.TestCase):
    def test_tofrench(self):
        self.assertEqual(EnglishToFrench('bread'), 'pain')
        self.assertEqual(EnglishToFrench('mountain'), 'montagne')
        self.assertEqual(EnglishToFrench('pickle'), 'cornichone')

        self.assertNotEqual(EnglishToFrench('bread'), 'bread')
        self.assertNotEqual(EnglishToFrench('train'), 'train')
        self.assertNotEqual(EnglishToFrench('pickle'), 'pickle')
    