import datetime
import unittest
from more_fun_with_collections import date_time

""" This is a test file for date_time.py file"""


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        """ tests half_birthday."""
        birthday = datetime.date()
        later_half_birthday = datetime.date(2020, 7, 1)
        self.assertEqual(date_time.half_birthday(birthday), later_half_birthday)


if __name__ == '__main__':
    unittest.main()
