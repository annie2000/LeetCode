class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r 
        
        while l <= r:
            m = (l + r)//2
            acc_hour = 0
            
            for p in piles:
                acc_hour += math.ceil(p/m)
            
            if acc_hour <= h:
                r = m - 1
                res = min(res, m)
            else:
                l = m +1
        
        return res
            
                
        