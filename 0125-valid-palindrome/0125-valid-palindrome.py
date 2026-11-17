class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in reversed(s.lower()):
            if i.isalnum():
               s1= s1+i
        a= 0
        b= len(s1)-1
        while a<=b:
            if s1[a] == s1[b]:
                a+=1
                b-=1
            else:
                return False
        return True            

