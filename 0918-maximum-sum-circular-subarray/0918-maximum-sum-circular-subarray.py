class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        curr_sum = 0
        min_sum = float("inf")

        for num in nums:
            curr_sum += num
            min_sum = min(min_sum, curr_sum)

            if curr_sum > 0:
                curr_sum = 0
        
        currMax = 0
        max_sum = nums[0]

        for num in nums:
            currMax += num
            max_sum = max(currMax, max_sum)

            if currMax < 0:
                currMax = 0
        

        print("The min sum is", min_sum)
        print("The circular sum is", sum(nums) - min_sum)
        print("The max sum is", max_sum)
        # if they are all negative
        if max_sum < 0:
            return max_sum
        
        circular = sum(nums) - min_sum


        return max(circular, max_sum)