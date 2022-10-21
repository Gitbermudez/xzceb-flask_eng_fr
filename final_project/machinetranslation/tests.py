"""
test
"""
import unittest
#import translator
from translator import en_to_fr, fr_to_en

class TestTransLator(unittest.TestCase):
    """
    english to french
    """
    def test_en_to_fr(self):
        self.assertEqual(en_to_fr("Hello"), "Bonjour")
        self.assertNotEqual(en_to_fr(0), 0)
        self.assertNotEqual(en_to_fr("None"), '')

class TestFrtoen(unittest.TestCase):
#class test_fr_to_en(unittest.TestCase):
    """
    french to english
    """
    def test_fr_to_en(self):
        self.assertEqual(fr_to_en("Bonjour"), "Hello")
        self.assertNotEqual(fr_to_en(0), 0)
        self.assertNotEqual(fr_to_en("None"), '')

if __name__=="__main__":
    pass
unittest.main()
