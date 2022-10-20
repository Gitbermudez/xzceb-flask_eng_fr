import unittest

from translator import english_to_french, french_to_english


class test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")
        self.assertNotEqual(english_to_french("None"), '')

class test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Au revoi"), "Goodbye")
        self.assertNotEqual(french_to_english("None"), '')

#frenchToEnglish(frenchText):
#frenchToEnglish(Bonjour)
#englishToFrench(Hello)

#if__name__=='__main__':
unittest.main()
