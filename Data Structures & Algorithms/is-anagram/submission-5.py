class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        COUNTER_S = Counter(s)
        COUNTER_T = Counter(t)
        if len(s)!= len(t):
            return False
        return COUNTER_S == COUNTER_T
                
            
        
        