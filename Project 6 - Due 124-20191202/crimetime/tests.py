# Project 6
# Name: John Wright
# Instructor: Sussan Einakian
# Section: 101-05
import unittest
from crimetime import *


class TestCases(unittest.TestCase):
   def test_get_lines(self):
      file = open('crimes.tsv', 'r')
      lines = get_lines('crimes.tsv')
      self.assertEqual(lines[1],'150017276\tNON-CRIMINAL\tAIDED CASE, MENTAL DISTURBED\n')
   def test_create_crimes(self):
      file = open('crimes.tsv', 'r')
      lines = create_crimes('crimes.tsv')
      self.assertEqual(lines,[])

   def test_update_crimes(self):
      pass


if __name__ == '__main__':
   unittest.main()