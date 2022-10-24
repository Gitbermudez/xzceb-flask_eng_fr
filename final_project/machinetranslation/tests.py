"""
test
"""
import unittest
#import translator
from translator import englishToFrench, frenchToEnglish

class TestTransLator(unittest.TestCase):
    """
    english to french
    """
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertNotEqual(englishToFrench(0), 0)
        self.assertNotEqual(englishToFrench("None"), '')

class TestFrtoen(unittest.TestCase):
#class test_fr_to_en(unittest.TestCase):
    """
    french to english
    """
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish(0), 0)
        self.assertNotEqual(frenchToEnglish("None"), '')

if __name__=="__main__":
    pass
unittest.main()
