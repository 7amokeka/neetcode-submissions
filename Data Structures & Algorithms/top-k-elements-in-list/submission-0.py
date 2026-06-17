class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for n in nums:
            if n in hashMap:
                hashMap[n] = hashMap.get(n, 0) +1

            hashMap[n] = hashMap.get(n, 1)

        return sorted(hashMap, key=hashMap.get, reverse=True)[:k]