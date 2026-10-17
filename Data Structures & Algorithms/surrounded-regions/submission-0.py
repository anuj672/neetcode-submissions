class Solution:
    def solve(self, board: List[List[str]]) -> None:

        R,C = len(board), len(board[0])

        def capture(i,j):

            if i<0 or j<0 or i>=R or j>=C or board[i][j]!="O":
                return

            board[i][j]="A"

            capture(i+1,j)
            capture(i-1,j)
            capture(i,j+1)
            capture(i,j-1)    
        
        
        for i in range(R):
            if board[i][0]=="O":
                capture(i,0)
            if board[i][C-1]=="O":
                capture(i,C-1)

        for i in range(C):
            if board[0][i]=="O":
                capture(0,i)
            if board[R-1][i]=="O":
                capture(R-1,i)

        for i in range(R):
            for j in range(C):
                if board[i][j]=="A":
                    board[i][j]="O"
                elif board[i][j]=="O":
                    board[i][j]="X"            

