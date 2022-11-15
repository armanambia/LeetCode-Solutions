class Solution {
public:
    
    void dfs(vector<vector<char>>& grid, int r, int c){
        // base case
        // std::cout << r << "\n";
        if(r >= grid.size() || c >= grid[0].size()) return; 
        if(grid[r][c] == '0') return;
        // are we a piece of land?
        grid[r][c] = '0';// sink ourselves
        // call on all neighbours to sink their land
        
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        /* DFS ideas */
        int count{};
        //iterate through each grid cell
        for(int r{}; r < grid.size(); ++r){
            for(int c{}; c < grid[r].size(); ++c){
                if(grid[r][c] == '1'){
                    dfs(grid, r, c);
                    ++count;
                }
            }
        }//end outer for
        return count;
    }
};