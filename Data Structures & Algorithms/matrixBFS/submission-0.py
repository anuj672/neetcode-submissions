class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        q = deque()
        visit = set()

        count = 0

        R,C = len(grid), len(grid[0])

        q.append((0,0))
        visit.add((0,0))

        while q:
            for i in range(len(q)):

                r,c = q.popleft()

                if r==R-1 and c==C-1:
                    return count

                range_ = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr, dc in range_:
                    if r+dr<0 or c+dc<0 or c+dc==C or r+dr==R:
                        continue

                    if (r+dr,c+dc) in visit or grid[r][c]==1:
                        continue
                    q.append((r+dr,c+dc))
                    visit.add((r+dr,c+dc))
            count+=1

        return -1        



        