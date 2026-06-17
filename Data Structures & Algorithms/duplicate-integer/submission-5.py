class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        ary = []

        for n in nums:
            if n in ary:
                return True
            
            ary.append(n)

        return False
