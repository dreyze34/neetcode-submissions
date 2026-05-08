class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = {}
        for ch in t:
            freqT[ch] = freqT.get(ch, 0) + 1
        m = len(freqT)
        n = len(s)
        if n == 1:
            return s if s == t else ""
        freqS = {s[0]: 1}
        matched = 1 if freqT.get(s[0], 0) == 1 else 0
        result = ""
        i, j = 0, 0
        while j < n:
            if matched != m and j == n-1:
                break
            
            elif matched != m:
                j += 1
                ch = s[j]
                if ch in freqT:
                    freqS[ch] = freqS.get(ch, 0) + 1
                    if freqS[ch] == freqT[ch]:
                        matched += 1
            else:
                if j-i+1 < len(result) or result == "":
                    result = s[i:j+1]
                ch = s[i]
                i += 1
                if ch in freqT:
                    freqS[ch] -= 1
                    if freqS[ch] < freqT[ch]:
                        matched -= 1
        return result