import unittest
import deep_translator

def FrenchToEnglish(str: str) -> str:
    retStr = deep_translator.GoogleTranslator(source='fr', target='en').translate(str)
    return retStr

class TestToEnglishTranslations(unittest.TestCase):
    def test_toenglish(self):
        self.assertEqual(FrenchToEnglish('pain'), 'bread')
        self.assertEqual(FrenchToEnglish('montagne'), 'mountain')
        self.assertEqual(FrenchToEnglish('cornichon'), 'pickle')

        self.assertNotEqual(FrenchToEnglish('pain'), 'pain')
        self.assertNotEqual(FrenchToEnglish('former'), 'former')
        self.assertNotEqual(FrenchToEnglish('cornichon'), 'cornichon')
    