class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = collections.defaultdict(int)
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in mydic:
                return [i, mydic[diff]]
            mydic[num] = i
        