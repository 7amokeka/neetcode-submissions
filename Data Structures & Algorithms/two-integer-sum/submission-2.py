class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {n: target - n for n in nums if n < target }
        
        hash_map = {}
        for i, n in enumerate(nums):
            
            if target - n in hash_map:
                return [hash_map[target - n], i]  # Returns the two indices!
            hash_map[n] = i


