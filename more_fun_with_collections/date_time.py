"""
Program: date_time.py
Author: Ihsanullah Anwary
Last date modified: 10/15/2020
This program is an example of Python datetime.
"""
import datetime


def half_birthday(date_of_birth):
    """accepts datetime"""
    half_year = datetime.timedelta(days=365 / 2)  # calculates 6 months.
    return date_of_birth + half_year  # calculates  6 months later-half-birthday


if __name__ == '__main__':
    birth_day = datetime.date(2020, 1, 1)
    print(half_birthday(birth_day))
    """ calling the function."""
