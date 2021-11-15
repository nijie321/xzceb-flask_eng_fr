import unittest
from translator import  english_to_french, french_to_english
class TestTranslationE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("World"), "Monde")

class TestTranslationF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Monde"), "World")

unittest.main()