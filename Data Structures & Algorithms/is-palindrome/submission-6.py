class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        newStr = "".join([c for c in s if c.isalnum()]).lower()
        print(newStr)
        return newStr[::-1] == newStr