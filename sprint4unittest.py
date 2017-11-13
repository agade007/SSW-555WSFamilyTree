import unittest
from gedcomFileParser import GEDCOMFileParser
from userStory import *
fileName = "falsetree.ged"

class test_us31_single_over_30years(unittest.TestCase):
    def test_us31_single_over_30years_1(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertFalse(us31_single_over_30years(individuals, families))

class test_us33_list_orphans_below18years(unittest.TestCase):
    def test_us33_list_orphans_below18years_1(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertFalse(us33_list_orphans_below18years(individuals, families))

class test_us38_upcoming_birthdays(unittest.TestCase):
    def test_us38_upcoming_birthdays_1(self):
        individuals,_ = GEDCOMFileParser(fileName)
        self.assertFalse(us38_upcoming_birthdays(individuals))

class test_us39_upcoming_anniversaries(unittest.TestCase):
    def test_us39_upcoming_anniversaries_1(self):
        _,families = GEDCOMFileParser(fileName)
        self.assertFalse(us39_upcoming_anniversaries(families))

class test_us32_multiple_births_in_family(unittest.TestCase):
    def test_us32_multiple_births_in_family_1(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertFalse(us32_multiple_births_in_family(individuals,families))

class test_us37_list_living_spouses_descendents(unittest.TestCase):
    def test_us37_list_living_spouses_descendents_1(self):
        individuals, families = GEDCOMFileParser(fileName)
        self.assertFalse(us37_list_living_spouses_descendents(individuals,families))


if __name__ == '__main__':
    unittest.main()
