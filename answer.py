"""Math 019"""
import datetime
from solver import solver


def answer():
    """Returns the number of sundays from 1901-01-01 to 2000-12-31"""

    return solver(datetime.date(1901, 1, 1), datetime.date(2000, 12, 31))
