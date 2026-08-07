class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ""
        for k in range(len(s)):
            if s[k].isalnum():
                cleanStr += s[k].lower()
        n = len(cleanStr)
        i, j = 0, n-1
        while i < j:
            if cleanStr[i] != cleanStr[j]:
                return False
            i += 1
            j -= 1
        return True