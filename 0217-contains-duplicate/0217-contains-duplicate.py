class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        setlen = len(numset)
        
        if setlen != len(nums):
            return True
        else:
            return False
        