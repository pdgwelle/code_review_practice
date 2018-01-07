"""Tests for practice problems."""

import unittest

import practice_problems

class CountAppearancesTest(unittest.TestCase):
    def test(self):
        self.assertEqual(practice_problems.count_appearances([1, 1, 3]),
        	             {1: 2, 3: 1})

if __name__ == '__main__':
    unittest.main()