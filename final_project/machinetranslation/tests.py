""" Test functions """
import unittest
from translator import english_to_french, french_to_english

#class TestFrtoen(unittest.TestCase):
class TestEnglis2French(unittest.TestCase):
    """ English to French."""
    def test1(self):
        """ function."""
        #English to French."""
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #E2F
        self.assertNotEqual(english_to_french(0), 0)            #Null
        self.assertNotEqual(english_to_french('None'), ' ')      #Null

#class TestFrtoen(unittest.TestCase):
class TestFrench2English(unittest.TestCase):
    """ french to english """
    def test2(self):
        """ french to english """
        #french to english """
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # F2E
        self.assertNotEqual(french_to_english(0), 0)            #Null
        self.assertNotEqual(french_to_english('None'), ' ')      #Null
if __name__=="__main__":
    pass
unittest.main()
