class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        d_s, d_t = {}, {}
        for i in range(len(s)):
            d_s[s[i]] = d_s.get(s[i], 0) + 1
            d_t[t[i]] = d_t.get(t[i], 0) + 1

        for ch, f_s in d_s.items():
            f_t = d_t.get(ch)
            if f_t is None or f_t != f_s:
                return False
        return True
