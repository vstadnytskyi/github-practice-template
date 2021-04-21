"""test_multiply function uncommented, error corrected"""

import unittest
from numpy.testing import assert_array_equal

class NumericalTest(unittest.TestCase):
    def test_sum(self):
        from ..numerical import algorithms
        self.assertEqual(algorithms.sum(1,2), 3)

    def test_multiply(self):
        from ..numerical import algorithms
        self.assertEqual(algorithms.multiply(3,4), 12)
