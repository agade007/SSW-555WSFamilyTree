#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest import TestCase
from gedcomFileParser import GEDCOMFileParser
from classModels import gedcomLineClass, individualsClass, familiesClass
from main import *
from userStory import US05_marriage_before_death,US06_divorce_before_death

class test_birth_before_marriage(TestCase):
    def test_birth_before_marriage_1(self):
        individuals, families = GEDCOMFileParser('falsetree.ged')
        self.assertFalse(US05_marriage_before_death(individuals,families))
        
class  test_divorce_before_death(TestCase):
    def test_divorce_before_death_1(self):
        individuals, families = GEDCOMFileParser('familytree.ged')
        self.assertTrue(US06_divorce_before_death(individuals,families))
if __name__ == '__main__':
    unittest.main()
