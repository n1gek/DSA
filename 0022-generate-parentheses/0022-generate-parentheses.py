class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def helper(path, pre, post): # takes in what we are building and the controllers
            if len(path) == n * 2:    # base case
                res.append(path)
                return 
            
            open = "("
            close = ")"
            # now building the path 
            if pre < n:
                new_path = path + open
                helper(new_path, pre + 1, post)
            if post < pre:
                new_path = path + close
                helper(new_path, pre, post + 1)
        
        helper("", 0, 0)
        return res


            
