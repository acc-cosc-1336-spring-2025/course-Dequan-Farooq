#
import unittest
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

    
class Test_Config(unittest.TestCase):

    def get_options_ratio(self):
        self.assertEqual(5,20)
        return 0.25
    def get_options_ratio_1(self):
        self.assertEqual(10,20)
        return 0.5
    
    def get_faculty_rating(self):
        self.assertEqual(get_faculty_rating(0.91),'Excellent')
        self.assertEqual(get_faculty_rating(0.85),'Very Good')
        self.assertEqual(get_faculty_rating(0.71),'Good')
        self.assertEqual(get_faculty_rating(0.66),'Needs Improvement')
        self.assertEqual(get_faculty_rating(0.45),'Unacceptable')
                        