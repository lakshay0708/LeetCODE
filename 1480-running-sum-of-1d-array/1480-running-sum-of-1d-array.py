class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        t = 0
        for i in range(len(nums)):
            nums[i] = nums[i]+t
            t = nums[i]
        return nums    