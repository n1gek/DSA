class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def helper(arr, index):
            if len(arr) == k:
                res.append(arr[:])
                return 
            
            for i in range(index, n + 1):
                arr.append(i)
                helper(arr, i + 1)
                arr.pop()
        
        helper([], 1)
        return res

        