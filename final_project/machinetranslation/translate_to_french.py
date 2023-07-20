import unittest
from deep_translator import MyMemoryTranslator

def EnglishToFrench(str: str) -> str:
    retStr = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(str)
    return retStr

class TestToEnglishTranslations(unittest.TestCase):
    def test_assertEq(self):
        self.assertEqual(EnglishToFrench('bread').lower(), 'pain')
        self.assertEqual(EnglishToFrench('mountain').lower(), 'montagne')

    def test_assertNotEq(self):
        self.assertNotEqual(EnglishToFrench('bread').lower(), 'bread')
        self.assertNotEqual(EnglishToFrench('train').lower(), 'train')
    