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

class test_list_all_deceased_individuals(unittest.TestCase):
    def test_list_all_deceased_individuals_1(self):
        individuals,_ = GEDCOMFileParser(fileName)
        self.assertFalse(us_29_list_all_deceased_individuals(individuals))

class test_list_living_married_people(unittest.TestCase):
    def test_list_living_married_people_1(self):
        individuals,families = GEDCOMFileParser(fileName)
        self.assertFalse(us30_list_living_married_people(individuals,families))

class test_people_born_in_30days(unittest.TestCase):
    def test_people_born_in_30days_1(self):
        individuals,_ = GEDCOMFileParser(fileName)
        self.assertFalse(us35_people_born_in_30days(individuals))

class test_people_died_in_last30_days(unittest.TestCase):
    def test_people_died_in_last30_days_1(self):
        individuals,_ = GEDCOMFileParser(fileName)
        self.assertFalse(us36_people_died_in_last30_days(individuals))




if __name__ == '__main__':
    unittest.main()
