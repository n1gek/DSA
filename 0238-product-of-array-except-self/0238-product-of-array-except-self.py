class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        answer = [1] * length

        left_product = 1
        for x in range(length ):
            answer[x] = left_product
            left_product *= nums[x]
        
        right_product = 1
        for x in range(length - 1, -1, -1):
            answer[x] *= right_product
            right_product *= nums[x]
        
        return answer
