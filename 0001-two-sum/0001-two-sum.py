class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mydic = collections.defaultdict(int)

        for id, num in enumerate(nums):
            diff = target - num #[7, 2, -2, -6]
            if diff in mydic:
                return [id, mydic[diff]]
            mydic[num] = id
            


         