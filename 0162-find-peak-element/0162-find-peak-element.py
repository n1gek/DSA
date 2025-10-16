class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                # moving uphill
                left = mid + 1
            else:
                # moving downhill or peak
                right = mid
        
        return left  # or right, same at this point
