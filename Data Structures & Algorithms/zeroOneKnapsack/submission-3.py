class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        M = capacity
        N = len(profit)

        #i am maximizing profits

        ans = [[0] * (M+1) for _ in range(N)]

        for i in range(N):
            ans[i][0]=0

        for i in range(M+1):
            if i >= weight[0]:
                ans[0][i] = profit[0] 


        for i in range(1, N):
            for j in range(1,M+1):
                exclude = ans[i-1][j]
                include = 0
                if j - weight[i] >=0:
                    include = profit[i] + ans[i-1][j - weight[i]]
                ans[i][j] = max(exclude,include)    

        return ans[N-1][M]


