class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        mydic = collections.defaultdict(int)
        res = []
        
        for i, num in enumerate(nums):
            mydic[num] = i
            tempS = 0
            for i in range(mydic[num]+1):
                tempS += nums[i]
            res.append(tempS)
        
        return res
                
            
            
        