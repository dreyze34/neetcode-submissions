class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        indexes = (0, 0)
        for i in range(n-1):
            k = 0
            while i - k >= 0 and i + k < n and s[i-k] == s[i+k]:
                k += 1
            if 2 * (k-1) >= indexes[1] - indexes[0]:
                indexes = (i-k+1, i+k)
            k = 0
            j = i + 1
            while i - k >= 0 and j + k < n and s[i-k] == s[j+k]:
                k += 1
            if 2 * k >= indexes[1] - indexes[0]:
                indexes = (i-k+1, j+k)
        return s[indexes[0]:indexes[1]]
