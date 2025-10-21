class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def helper(arr, index):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    helper(arr, index + 1)
                    arr.pop()
            
        
        helper([], 0)
        return res