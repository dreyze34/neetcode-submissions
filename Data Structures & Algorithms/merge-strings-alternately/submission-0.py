class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i, j = 0, 0
        s = ""
        while i < n or j < m:
            if i == n:
                s += word2[j]
                j += 1
            elif j == m:
                s += word1[i]
                i += 1
            elif i <= j:
                s += word1[i]
                i += 1
            else:
                s += word2[j]
                j += 1
        return s
            