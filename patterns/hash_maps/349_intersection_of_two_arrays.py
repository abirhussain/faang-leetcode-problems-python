from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # solution steps
        # 1. convert the smaller array to a set to minimize space and time complexity
        # 2. Iterate over the larger array and collect the intersection
        # 3. Convert the result to a list and return result

        # step:1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        set_nums1 = set(nums1)

        # step:2
        result = {num for num in nums2 if num in set_nums1}

        # step:3
        return list(result)
        
        ##### Complexity ########
        # The time complexity is O(n + m)
        # The space complexity is reduced to O(min(n, m))