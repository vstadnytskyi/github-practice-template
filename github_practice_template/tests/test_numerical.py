import unittest
from numpy.testing import assert_array_equal

class NumericalTest(unittest.TestCase):
    def test_sum(self):
        from ..numerical import algorithms
        self.assertEqual(algorithms.sum(1,2), 3)
