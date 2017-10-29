import unittest
from gedcomFileParser import GEDCOMFileParser
from userStory import *
fileName = "falsetree.ged"

class test_unique_individual_family_id(unittest.TestCase):
    def test_unique_individual_family_id_1(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertFalse(us22_unique_indivdual_family_id(individuals,families))

class test_unique_name_birthday(unittest.TestCase):
    def test_unique_name_birthday_1(self):
        individuals,_ = GEDCOMFileParser(fileName)
        self.assertFalse(us23_unique_name_birthday(individuals))


if __name__ == '__main__':
    unittest.main()
