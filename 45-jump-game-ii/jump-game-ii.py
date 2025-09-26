from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        reach = 0

        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            
            if i == end:  # need to jump
                jumps += 1
                end = reach

        return jumps
