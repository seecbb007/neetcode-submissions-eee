class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dit = {}
        for n in nums: 
            if n in dit:
                dit[n] = dit[n] + 1
            else:
                dit[n] = 1
        reverseList = sorted(dit, key = dit.get, reverse = True)
        return reverseList[:k]            
        