class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        j = 0
        for i in range(n):
            if j < m and s[i] == t[j]:
                j += 1
        return m - j