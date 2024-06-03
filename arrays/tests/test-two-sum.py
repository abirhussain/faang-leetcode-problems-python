import unittest
from arrays.solutions.two_sum import Solution 



class TestTwoSum(unittest.TestCase):
    def test_two_sum_example1(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(solution.twoSum(nums, target), [0, 1])

    def test_two_sum_example2(self):
        solution = Solution()
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(solution.twoSum(nums, target), [1, 2])

    # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()
