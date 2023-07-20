import unittest

class TestToEnglishTranslations(unittest.TestCase):
    def test_assert_eq(self):
        self.assertEqual(french_to_english('pain').lower(), 'bread')
        self.assertEqual(french_to_english('montagne').lower(), 'mountain')

    def test_assert_not_eq(self):
        self.assertNotEqual(french_to_english('pain').lower(), 'pain')
        self.assertNotEqual(french_to_english('former').lower(), 'former')

        
class TestToEnglishTranslations(unittest.TestCase):
    def test_assert_eq(self):
        self.assertEqual(english_to_french('bread').lower(), 'pain')
        self.assertEqual(english_to_french('mountain').lower(), 'montagne')

    def test_assert_not_eq(self):
        self.assertNotEqual(english_to_french('bread').lower(), 'bread')
        self.assertNotEqual(english_to_french('train').lower(), 'train')
