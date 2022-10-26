""" Test functions """
import unittest
from translator import english_to_french
from translator import french_to_english

class TestEnglis2French(unittest.TestCase):
    """ English to French."""
    def test_e2f1(self):
        #self.assertEqual(english_to_french('Hello'), 'Bonjour') #E2F
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #E2F
    def test_e2f_bonjour1(self):
        self.assertNotEqual(english_to_french(0), 0)            #Null
    def test_e2f_bonjour2(self):
        self.assertNotEqual(english_to_french('None'), ' ')     #Null

class TestFrench2English(unittest.TestCase):
    """ french to english """
    def test_f2e1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  #F2E
    def test_f2e_bonjour1(self):
        self.assertNotEqual(french_to_english(0), 0)             #Null
    def test_f2e_bonjour2(self):
        self.assertNotEqual(french_to_english('None'), ' ')      #Null
if __name__=="__main__":
    pass
unittest.main()
