class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        i = 0
        while True:
            ch = None
            for j in range(n):
                s = strs[j]
                if i == len(s):
                    return s
                elif j == 0:
                    ch = s[i]
                elif ch != s[i]:
                    return s[:i]
            i += 1

                
