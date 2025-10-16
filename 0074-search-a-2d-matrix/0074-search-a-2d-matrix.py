class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def helper(arr):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == target:
                    return True
            
                if arr[mid] > target: # search the lower half 
                    right = mid - 1
                else:
                    left = mid + 1
            
            return False
        
        rows = len(matrix) # the number of rows we have
        #check the first element of each row, if its target return it
        # if the target is smaller than mid row first element, then search

        left = 0
        right = rows - 1

        while left <= right:
            mid = (left + right) //  2

            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            
            elif matrix[mid][0] < target and matrix[mid][-1] > target: # our result lies in here
                return helper(matrix[mid])

            # result can either be entirely up or down
            # if the result is entirely down
            elif matrix[mid][0] > target and matrix[mid][-1] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
