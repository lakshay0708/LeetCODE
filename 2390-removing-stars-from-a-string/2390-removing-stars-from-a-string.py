class Solution:
    def removeStars(self, s: str) -> str:
        t = []
        for i in range(len(s)):
         if s[i]!="*":
            t.append(s[i])
         else:
            t.pop()
        atu = "".join(t)   
        return atu           


        