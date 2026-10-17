class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        M = len(profit)
        N = capacity

        cache = [[-1] * (N+1) for _ in range(M)]


        def helper(profit,weight,capacity,cache,i):

            if i == len(profit):
                return 0

            if cache[i][capacity] != -1:
                return cache[i][capacity]

            cache[i][capacity] = helper(profit,weight,capacity,cache,i+1)

            newCap = capacity - weight[i]
            if newCap >=0:
                p = profit[i] + helper(profit,weight,newCap,cache,i+1)        

                cache[i][capacity] = max(cache[i][capacity], p)

            return cache[i][capacity]    

        return helper(profit,weight,capacity,cache,0)    