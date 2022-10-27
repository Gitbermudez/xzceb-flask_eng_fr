""" Test functions """
#import pdb
import unittest
from translator import english_to_french
from translator import french_to_english

#class TestEnglis2French(unittest.TestCase):
class TestModule(unittest.TestCase):    
    """ English to French."""
    def test_e2f(self):
        #self.assertEqual(english_to_french('Hello'), 'Bonjour') #E2F
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #E2F
    def test_e2f2(self):
        self.assertNotEqual(english_to_french(0), 0)            #Null
    def test_e2f3(self):
        self.assertNotEqual(english_to_french('None'), ' ')     #Null
#pdb.set_trace()
#class TestFrench2English(unittest.TestCase):
class TestModule1(unittest.TestCase):
    """ french to english """
    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  #F2E
    def test_f2e2(self):
        self.assertNotEqual(french_to_english(0), 0)             #Null
    def test_f2e3(self):
        self.assertNotEqual(french_to_english('None'), ' ')      #Null
if __name__=="__main__":
    pass
unittest.main()
