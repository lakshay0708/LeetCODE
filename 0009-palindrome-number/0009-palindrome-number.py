class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = str(x)
        return str(x) == r[::-1]