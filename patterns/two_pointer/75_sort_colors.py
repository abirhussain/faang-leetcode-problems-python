from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high],nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1

        return nums

################ Complexity ###################
# Time Complexity:𝑂(n), where n  is the number of elements in nums. The array is traversed once.

# Space Complexity: 𝑂(1), as the sorting is done in place.


        