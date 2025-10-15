class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #kadanes algorithm
        # initialize my max_sum = nums[0]
        # current_sum = 0
        # for num in nums:
        # if current sum < 0: reset it to 0
        # current_sum += num
        # get the max between the max and current

        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0
            
            current_sum += num
            max_sum = max(max_sum, current_sum)
        
        return max_sum
            
        