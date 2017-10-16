import unittest
from gedcomFileParser import GEDCOMFileParser
from userStory import *
fileName = "falsetree.ged"

class test_birth_before_marriage(unittest.TestCase):
    def test_birth_before_marriage_1(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertFalse(US05_marriage_before_death(individuals, families))

class test_divorce_before_death(unittest.TestCase):
    def test_divorce_before_death_1(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertTrue(US06_divorce_before_death(individuals, families))

class test_more_siblings(unittest.TestCase):
    def test_more_siblings(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertTrue(US14_mutiple_birth_5(individuals,families))
class test_males_same_lastname(unittest.TestCase):
    def test_males_same_lastname(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertFalse(US16_males_same_lastname(individuals,families))

class test_correct_gender(unittest.TestCase):
    def test_us21_correct_gender(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertFalse(us21_correct_gender(individuals,families))

class test_marriage_after_14yrs(unittest.TestCase):
    def test_marriage_after_14yrs(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertFalse(us10_marriage_after_14yrs(individuals,families))



if __name__ == '__main__':
    unittest.main()
