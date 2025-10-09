class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    self.helper(grid, row, col, visited)
                    count += 1
        return count 
    
    
    def helper(self, grid, row, col, visited):
        
        row_inbound = 0 <= row < len(grid)
        col_inbound = 0 <= col < len(grid[0])
        
        if not row_inbound or not col_inbound:
            return 
        if grid[row][col] == "0":
            return 
        
        pos = (row, col)
        if pos in visited:
            return 
        visited.add(pos)
        
        self.helper(grid, row+ 1, col, visited)
        self.helper(grid, row-1, col, visited)
        self.helper(grid, row, col-1, visited)
        self.helper(grid, row, col + 1, visited)
        