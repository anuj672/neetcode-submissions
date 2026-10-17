class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def helper(grid, r, c, visit):

            if r < 0 or c<0 or ((r,c) in visit)or r == ROWS or c==COLS or (grid[r][c]==1): 
                return 0

            if r == ROWS -1 and c == COLS-1:
                return 1

            visit.add((r,c))
            
            count = 0
            
            count += helper(grid, r,c+1,visit)
            count += helper(grid, r+1,c,visit)
            count += helper(grid, r-1,c,visit)
            count += helper(grid, r,c-1,visit)

            visit.remove((r,c))
            return count

        return helper(grid, 0,0,set())    

                        
