from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if i < 2 or nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i+=1
        return i
