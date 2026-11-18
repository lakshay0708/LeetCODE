class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d ={}
        for i in nums:
            d[i] = d.get(i,0) +1
        t = 0
        n = 0
        for k in d:
            if d[k] > (len(nums)//2) and d[k]>t :
                n = k
                t = max(t,d[k])

                
        return n            
