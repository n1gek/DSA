from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-num for num in nums]
        heapq.heapify(nums)

        for i in range(k):
            j = heapq.heappop(nums)
        
        return -j
    




        