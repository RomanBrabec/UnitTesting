import unittest
from integer import IntegerSet


class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        self.int_set = IntegerSet([1, 2, 3, 4, 5])
        self.empty_set = IntegerSet([])

    def test_sum(self):
        self.assertEqual(self.int_set.sum(), 15)
        self.assertEqual(self.empty_set.sum(), 0)

    def test_mean(self):
        self.assertEqual(self.int_set.mean(), 3.0)
        self.assertIsNone(self.empty_set.mean())

    def test_max(self):
        self.assertEqual(self.int_set.max(), 5)
        self.assertIsNone(self.empty_set.max())

    def test_min(self):
        self.assertEqual(self.int_set.min(), 1)
        self.assertIsNone(self.empty_set.min())

    def test_single_element(self):
        single_element_set = IntegerSet([10])
        self.assertEqual(single_element_set.sum(), 10)
        self.assertEqual(single_element_set.mean(), 10.0)
        self.assertEqual(single_element_set.max(), 10)
        self.assertEqual(single_element_set.min(), 10)

    def test_duplicate_elements(self):
        duplicate_elements_set = IntegerSet([1, 1, 2, 2, 3, 3])
        self.assertEqual(duplicate_elements_set.sum(), 6)
        self.assertEqual(duplicate_elements_set.mean(), 2.0)
        self.assertEqual(duplicate_elements_set.max(), 3)
        self.assertEqual(duplicate_elements_set.min(), 1)


if __name__ == '__main__':
    unittest.main()
