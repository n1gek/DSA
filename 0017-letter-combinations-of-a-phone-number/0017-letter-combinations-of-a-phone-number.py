from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        # 8 digits
        # 1 digit maps to 3 => 24
        # create a map to represent the relationships
        mapp = {'2': ["a", 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
        }
        
        # use recursion to build the strings
        res = []
        def helper(path, index): # takes in what we are currently building and any constraints
            if len(path) == len(digits):
                res.append(path)
                return 
            
            digit = digits[index]
            for char in mapp[digit]: # iteration over the letters
                new_path = path + char
                helper(new_path, index + 1)
            
        helper("", 0)

        return res







        
        
        
        