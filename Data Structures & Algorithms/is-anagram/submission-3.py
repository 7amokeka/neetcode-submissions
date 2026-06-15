class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        array = sorted([n for n in s])
        array2 = sorted([k for k in t])


        if array == array2:
            return True
        else:
            return False



        
        