class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    self.helper(x,y,grid)
                    count += 1
        return count
    def helper(self, row, col, grid):
        if grid[row][col] != '2':
            grid[row][col] = '2'
            if row > 0 and grid[row-1][col] == '1':
                self.helper(row - 1,col,grid)
            if row < len(grid) - 1 and grid[row+1][col] == '1':
                self.helper(row + 1,col,grid)
            if col > 0 and grid[row][col-1] == '1':
                self.helper(row,col-1,grid)
            if col < len(grid[0]) - 1 and grid[row][col+1] == '1':
                self.helper(row,col + 1,grid)
    