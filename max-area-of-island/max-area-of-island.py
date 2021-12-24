class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.count = 0
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count = self.dfs(r,c)
                if self.count > res:
                    res = self.count
                self.count = 0
        return res
    def dfs (self,r, c):
        if r < 0 or r > len(self.grid) -1:
            return 0
        if c < 0 or c > len(self.grid[0]) -1:
            return 0
        if self.grid[r][c] != 1:
            return 0
        self.grid[r][c] = 2      
        self.count += 1
        self.dfs(r-1,c)
        self.dfs(r+1,c)
        self.dfs(r,c-1)
        self.dfs(r,c+1)
    
    # def maxAreaOfIsland(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     self.grid = grid
    #     count = 0
    #     res = 0
    #     for r in range(len(grid)):
    #         for c in range(len(grid[0])):
    #             if grid[r][c] == 1:
    #                 print(count)
    #                 print('starting dfs')
    #                 self.dfs(r,c, count)
    #                 print('ending dfs')
    #                 print(count,'\n--------------------')
    #             if count > res:
    #                 res = count
    #     return res
    # def dfs (self,r, c, count):
    #     if r < 0 or r > len(self.grid) -1:
    #         return 
    #     if c < 0 or c > len(self.grid[0]) -1:
    #         return 
    #     if self.grid[r][c] != 1:
    #         return 
    #     self.grid[r][c] = 2      
    #     count += 1
    #     print(count)
    #     self.dfs(r-1,c,count)
    #     self.dfs(r+1,c,count)
    #     self.dfs(r,c-1,count)
    #     self.dfs(r,c+1,count)