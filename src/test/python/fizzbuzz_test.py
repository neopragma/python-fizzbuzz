#!/usr/bin/env python3

import unittest
from fizzbuzz import process_number

class FizzBuzzTest(unittest.TestCase):

  def setUp(self):
    pass

  def test_number_3(self):
    '''
    It returns "Fizz" for the number 3
    '''
    self.assertEqual(process_number(3), 'Fizz')

if __name__ == '__main__':
    unittest.main()
