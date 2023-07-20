import unittest
from deep_translator import MyMemoryTranslator

def FrenchToEnglish(str: str) -> str:
    retStr = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(str)
    return retStr

class TestToEnglishTranslations(unittest.TestCase):
    def test_assertEq(self):
        self.assertEqual(FrenchToEnglish('pain').lower(), 'bread')
        self.assertEqual(FrenchToEnglish('montagne').lower(), 'mountain')

    def test_assertNotEq(self):
        self.assertNotEqual(FrenchToEnglish('pain').lower(), 'pain')
        self.assertNotEqual(FrenchToEnglish('former').lower(), 'former')
    