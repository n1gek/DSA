class Solution:
    def isPalindrome(self, s: str) -> bool:

        path = [char.lower() for char in s if char.isalnum()]
        print(path)
        
        left, right = 0, len(path) - 1

        while left < right:
            if path[left] != path[right]:
                return False
            
            left += 1
            right -= 1
        

        return True
        