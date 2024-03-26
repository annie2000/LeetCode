class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        
        for ele in accounts:
            temSum = 0
            for i in range(len(ele)):
                temSum += ele[i]
            res.append(temSum)
            
        return max(res)
            
        
        
        