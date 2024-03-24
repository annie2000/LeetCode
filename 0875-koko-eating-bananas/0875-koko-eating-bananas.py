class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 풀어야 하는 것: 주어진 h 의 시간동안에 파일을 먹을 수 있는 가장 min(속도)
        # max(속도) = max(piles) 의 min(속도)
        
        ls = 1
        rs = max(piles)
        mins = rs
        
        while ls <= rs:
            ms = (ls + rs)//2
            totalH = 0
            
            
            for p in piles: 
                totalH += math.ceil(p/ms)
                # print("totalH: ", totalH)
            if totalH <= h:
                rs = ms -1
                mins = min(mins, ms)
                # print("mins: ", mins)
            else: 
                ls = ms +1
                
        return mins

                
                
            
            
        
        