class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = 0
        m = x
        while x>0:
            r = x%10
            n = n*10 + r
            x = x//10
        return n == m   
