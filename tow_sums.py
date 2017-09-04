class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [[nums[i], i] for i in range(len(nums))]
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while(j>i):
            if nums[i][0] + nums[j][0] < target:
                i+=1
            elif nums[i][0] + nums[j][0] > target:
                j-=1
            else:
                return [nums[i][1],nums[j][1]]