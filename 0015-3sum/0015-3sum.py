class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue 
            
            l, r = i + 1, len(nums) -1

            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum < 0 :
                    l += 1
                elif threesum > 0:
                    r -= 1
                else: 
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result 