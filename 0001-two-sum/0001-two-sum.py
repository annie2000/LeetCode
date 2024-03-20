class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = {}
        
        for i, n in enumerate(nums):
            goal = target - n
            if goal in mydic.keys() and i != mydic[goal]:
                return [i, mydic[goal]]
            mydic[n] = i
                

                
