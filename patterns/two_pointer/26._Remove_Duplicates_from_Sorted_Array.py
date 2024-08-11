class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0, 0
        while j < len(nums):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
            j+=1
        return i+1


        