class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        i, j = 0, 1
        h = set(s[0])
        maxL = 0
        while j < n:
            print(i, j, h, maxL)
            if s[j] in h:
                h.remove(s[i])
                i += 1
            else:
                h.add(s[j])
                j += 1
            maxL = max(maxL, j-i)        
        return maxL