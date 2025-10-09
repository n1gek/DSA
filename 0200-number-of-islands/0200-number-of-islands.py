class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()

        def explore(row, col):
            rowInbound = 0 <= row < rows
            colInbound = 0 <= col < cols

            if not rowInbound or not colInbound:
                return
            
            if grid[row][col] == "0":
                return
            
            pos = (row, col)
            if pos in seen:
                return
            
            seen.add(pos)
            
            explore(row + 1, col),
            explore(row, col + 1),
            explore(row - 1, col),
            explore(row, col - 1)

        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for row in range(rows):
            for col in range(cols):
                pos = (row, col)
                if grid[row][col] == "1" and pos not in seen:
                    explore(row, col)
                    count += 1
        
        return count
                    

        