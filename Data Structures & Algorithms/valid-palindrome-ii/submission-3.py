class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s: str):
            n = len(s)
            i, j = 0, n-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        n = len(s)
        i, j = 0, n-1
        state = False
        while i < j:
            if s[i] != s[j]:
                left = checkPalindrome(s[i:j])
                right = checkPalindrome(s[i+1:j+1])
                return left or right
            i += 1
            j -= 1
        return True