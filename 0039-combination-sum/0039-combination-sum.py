class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(arr, curr_sum, index):
            if curr_sum == target:
                res.append(arr[:])
                return
            elif curr_sum > target:
                return
            
            for i in range(index, len(candidates)):
                curr_sum += candidates[i]
                arr.append(candidates[i])
                helper(arr, curr_sum, i)
                arr.pop()
                curr_sum -= candidates[i]
        
        res = []
        helper([], 0, 0)
        return res


        
        