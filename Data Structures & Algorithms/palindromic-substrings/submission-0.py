class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        c = 0
        for i in range(n):
            k = 0
            while i - k >= 0 and i + k < n and s[i-k] == s[i+k]:
                c += 1
                k += 1
            k = 0
            j = i + 1
            while i - k >= 0 and j + k < n and s[i-k] == s[j+k]:
                c += 1
                k += 1
        return c

            
