"""
Sample test
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module """

    def test_add(self):
        """ Test add function """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_add_strings(self):
        """ Test add strings function """

        res = calc.add_strings("Hello", "World")
        self.assertEqual(res, "HelloWorld")
