class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        r = 0 
        l = 0 
        m = 0
        while r< len(s):
            if  s[r] in d:
                l = max(l , d[s[r]]+1) 
            m = max(m,r-l+1)
            d[s[r]] = r
            r+= 1
        return m          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
        