class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for i,w in enumerate(strs):
            
            sort_value = "".join(sorted(w))
            
            if sort_value in hash_map:
                hash_map[sort_value].append(w)
                
            else:
                hash_map[sort_value] = [w]
            

        return list(hash_map.values())
    
        