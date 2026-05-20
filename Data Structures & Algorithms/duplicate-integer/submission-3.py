class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        e = set()
        for n in nums: 
            if n in e:
                return True
            e.add(n)
        
        return False