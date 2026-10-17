class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = []
        output_list = {}
        for i in range(len(nums)):
            
            diff = target - nums[i]

            if diff in output_list:
                return [output_list[diff], i]

            output_list[nums[i]] = i


