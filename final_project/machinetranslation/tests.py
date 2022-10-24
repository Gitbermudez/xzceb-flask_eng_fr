""" Test functions """
import unittest
from translator import e2f, f2e

#class TestFrtoen(unittest.TestCase):
class TestEn2Frenc(unittest.TestCase):
    """ English to French."""
    def test1_e2f(self):
        """ function."""
        #English to French."""
        self.assertEqual(e2f("Hello"), "Bonjour") #E2F
        self.assertNotEqual(e2f(0), 0)            #Null
        self.assertNotEqual(e2f("None"), '')      #Null

#class TestFrtoen(unittest.TestCase):
class TestFrenc2En(unittest.TestCase):
    """ french to english """
    def test2_f2e(self):
        """ french to english """
        #french to english """
        self.assertEqual(f2e("Bonjour"), "Hello") # F2E
        self.assertNotEqual(f2e(0), 0)            #Null
        self.assertNotEqual(f2e("None"), '')      #Null

if __name__=="__main__":
    pass
unittest.main()
