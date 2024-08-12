class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Solution Steps:
        # 1. Create a hashmap (dictionary) to store counts of elements in nums1
        # 2. Iterate over nums2 and check if the element exists in the hashmap.
        #   i) if element exists and its count is greater than 0 then add element 
        #        in the result array and reduce the count by 1
        # 3. Return the result

        # Step1:
        hashmap = {}
        for num in nums1:
            hashmap[num] = hashmap.get(num,0) + 1

        # Step2:
        result = []
        for num in nums2:
            if num in hashmap and hashmap.get(num) > 0:
                result.append(num)
                hashmap[num] = hashmap.get(num) - 1

        # Step3:
        return result
        
########### Complexity ####################
# Time Complexity: The overall time complexity is O(n + m):

# O(n) for creating the hashmap from nums1.
# O(m) for iterating over nums2 and checking/updating the hashmap.

# Space Complexity: The overall space complexity is O(n + min(n, m)):

# O(n) for storing elements of nums1 in the hashmap.
# O(min(n, m)) for storing the intersection in the result list.