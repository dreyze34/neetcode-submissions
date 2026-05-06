class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join([ch for ch in s if ch.isalnum()]).lower()
        n = len(t)
        if n == 0:
            return True
        i = 0
        while i <= n//2:
            if t[i] != t[n-i-1]:
                return False
            i += 1
        return True