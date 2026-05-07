class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = {}
        i, j = 0, 0
        maxL = 1
        while j < n:
            freq[s[j]] = freq.get(s[j], 0) + 1
            maxCh = max(freq, key=freq.get)
            maxF = freq[maxCh]
            nb = j-i+1 - maxF
            if nb > k:
                freq[s[i]] -= 1
                i += 1
            maxL = max(maxL, j-i+1)
            j += 1
            
        return maxL