class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create a hash map (like a notepad)
        hash_map = {}

        # Do an  enumerate for loop to use the index ability
        for i, n in enumerate(nums):

            # Get the differance you need to find
            diff = target - n

            # If the differance in your notepad (hash map)
            if diff in hash_map:

                # return the 2 numbers that make the differance and 
                # their index which the first 1 is "diff" and the second is "i"
                return [hash_map[diff], i]


            # Add n and his value is his index in nums
            hash_map[n] = i


