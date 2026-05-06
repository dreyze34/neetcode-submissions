class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n-1
        while i < j:
            skip = False
            if not s[i].isalnum():
                i += 1
                skip = True
            if not s[j].isalnum():
                j -= 1
                skip = True
            if not skip:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True