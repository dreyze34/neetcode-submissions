class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        m, n = len(s1), len(s2)
        for ch in s1:
            freq1[ch] = freq1.get(ch, 0) + 1
        
        freq2 = {}
        i, j = 0, 0
        while j < n:
            if s2[j] not in freq1:
                j += 1
                i = j
                freq2 = {}
            else:
                freq2[s2[j]] = freq2.get(s2[j], 0) + 1
                if j-i+1 == m:
                    perm = True
                    for k2, v2 in freq2.items():
                        v1 = freq1.get(k2)
                        if v1 != v2:
                            freq2[s2[i]] -= 1
                            i += 1
                            perm = False
                            break
                    if perm:
                        return True
                j += 1
        return False
                        

