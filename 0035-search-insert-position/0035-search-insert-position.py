class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        h = len(nums)-1
       
           
        while l<=h:
            m = (l+h)//2
            if nums[m]==target:
                return m
            elif target>nums[m]:
                l = m+1
            else:
                h= m -1
        return h+1               

