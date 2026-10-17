class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count_zero=0
        count_one = 1
        l=0
        res=0

        for r in range(len(nums)):
            if nums[r]==0:
                count_zero+=1

            while l<r and count_zero > 1:
                if nums[l] == 0:
                    count_zero+=1
                l+=1

            res = max(res, r-l+1)

        return res        