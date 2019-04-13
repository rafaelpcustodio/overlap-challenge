import unittest
from overlap.Overlap import Overlap

class OverlapTest(unittest.TestCase):

    def test_positive_ascending_overlap_success(self):
        line1 = [1, 2]
        line2 = [0, 1]
        overlap = Overlap()
        result = overlap.execute_overlap(line1, line2)
        print(result)
        self.assertTrue(result, 'Lines overlap at x-axis')

    def test_positive_descending_overlap_success(self):
        line1 = [2, 1]
        line2 = [1, 0]
        overlap = Overlap()
        result = overlap.execute_overlap(line1, line2)
        print(result)
        self.assertTrue(result, 'Lines overlap at x-axis')

    def test_negative_ascending_overlap_success(self):
        line1 = [-2, -1]
        line2 = [-5, -1]
        overlap = Overlap()
        result = overlap.execute_overlap(line1, line2)
        print(result)
        self.assertTrue(result, 'Lines overlap at x-axis')

    def test_negative_descending_overlap_success(self):
        line1 = [-1, -2]
        line2 = [-1, -5]
        overlap = Overlap()
        result = overlap.execute_overlap(line1, line2)
        print(result)
        self.assertTrue(result, 'Lines overlap at x-axis')

    def test_negative_positive_descending_overlap_success(self):
        line1 = [-1, -2]
        line2 = [1, -5]
        overlap = Overlap()
        result = overlap.execute_overlap(line1, line2)
        print(result)
        self.assertTrue(result, 'Lines overlap at x-axis')

    def test_negative_positive_ascending_overlap_success(self):
        line1 = [-2, 1]
        line2 = [-5, 1]
        overlap = Overlap()
        result = overlap.execute_overlap(line1, line2)
        print(result)
        self.assertTrue(result, 'Lines overlap at x-axis')

    def test_negative_positive_ascending_overlap_not_success(self):
        line1 = [-2, 0]
        line2 = [5, 1]
        overlap = Overlap()
        result = overlap.execute_overlap(line1, line2)
        print(result)
        self.assertFalse(result, 'Lines does not overlap at x-axis')

    def test_negative_positive_ascending_success(self):
        line1 = [-221, 2213]
        line2 = [55, 1]
        overlap = Overlap()
        result = overlap.execute_overlap(line1, line2)
        print(result)
        self.assertTrue(result, 'Lines overlap at x-axis')


if __name__ == '__main__':
    unittest.main()
