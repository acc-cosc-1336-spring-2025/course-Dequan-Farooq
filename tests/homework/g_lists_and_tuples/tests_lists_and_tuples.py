import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value


class TestListValues(unittest.TestCase):
    def test_lowest_list_value(self):
        numbers=[8 ,10 ,1 ,50 ,20]
        result=get_lowest_list_value(numbers)
        self.assertEqual(result,1)

    def test_highest_list_value(self):
        numbers=[8 ,10 ,1 ,50 ,20]
        result=get_highest_list_value(numbers)
        self.assertEqual(result,50)
