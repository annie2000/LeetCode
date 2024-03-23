import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPri = math.inf
        maxPro = -(math.inf)
        diffP = 0
        
# [7,1,5,3,6,4] -> {0:7, 1:1, 2:5, 3:3, 4:6, 5:4}
# determine -> buy when : sofarMin(currPrices) if prices is not the last item :: update maxprofit
# determine -> sell when

        for p in prices:
            minPri = min(minPri, p)
            maxPro = max(maxPro, (p - minPri))
        return maxPro
        

        
        