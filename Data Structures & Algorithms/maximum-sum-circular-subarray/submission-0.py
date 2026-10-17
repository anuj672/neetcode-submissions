class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cmin, cmax = 0,0

        gmax, gmin = nums[0], nums[0]
        total = 0

        for n in nums:
            cmin  = min(0,cmin)
            cmax  = max(0,cmax)
            cmin+=n
            cmax+=n
            total+=n

            gmax = max(cmax,gmax)
            gmin  = min(gmin, cmin)


        return max(gmax, total - gmin) if total > 0 else gmax