from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Solution Steps:
        # 1. Compute the prefix sum array where each element at index 'i' contains 
        #    the sum of elements from index 0 to 'i' in the original array.
        # 2. Iterate over the array and for each element, check if the sum of elements
        #    to the left of the current index equals the sum of elements to the right:
        #    - If they are equal, return the current index as the pivot index.
        # 3. If no pivot index is found where the left and right sums are equal, return -1.

        # Step 1: Compute the prefix sum array
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        # Step 2: Iterate and find the pivot index
        for i in range(len(nums)):
            if i == 0:
                # If the first element is the pivot index, the sum to the right should equal zero
                if nums[len(nums)-1] - nums[i] == 0:
                    return i
            elif i == len(nums) - 1:
                # If the last element is the pivot index, the sum to the left should equal zero
                if nums[i-1] == 0:
                    return i
            else:
                # Calculate the left and right sums and check for equality
                left_sum = nums[i-1]
                right_sum = nums[len(nums)-1] - nums[i]
                if left_sum == right_sum:
                    return i
        
        # Step 3: If no pivot index is found, return -1
        return -1
        