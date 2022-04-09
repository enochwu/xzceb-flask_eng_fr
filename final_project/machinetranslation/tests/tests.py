import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(
            "I am very well."), "Je suis très bien.")
        self.assertNotEqual(english_to_french(
                "ca va bien"), "I am well")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonne nuit"), "Good night")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(
            "C'est un ordinateur!"), "It's a computer!")
        self.assertNotEqual(french_to_english(
            "Salut"), "Goodbye")


print("\nIBM Watson Translation API Tests:")
unittest.main()
