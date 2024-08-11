class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # define variable to store disappeared number
        sol = []

        # sort the array using cyclic sort
        i = 0
        while i < len(nums):
            if nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i+=1
        # find the disappeared numbers
        for i in range(len(nums)):
            if nums[i] != i+1:
                sol.append(i+1)
        # return solution array
        return sol
