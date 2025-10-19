class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums) - 1

        def helper(index):
            res = [index]

            # Expand left
            l = index - 1
            while l >= 0 and nums[l] == target:
                res.append(l)
                l -= 1

            # Expand right
            r = index + 1
            while r < len(nums) and nums[r] == target:
                res.append(r)
                r += 1

            return [min(res), max(res)]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return helper(mid)

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return [-1, -1]
