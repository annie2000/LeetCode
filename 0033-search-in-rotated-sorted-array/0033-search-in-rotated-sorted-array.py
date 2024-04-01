class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:  # Left side is sorted
                if nums[l] <= target < nums[mid]:  # Target is in the left side
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # Right side is sorted
                if nums[mid] < target <= nums[r]:  # Target is in the right side
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
