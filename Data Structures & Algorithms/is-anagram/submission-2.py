class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False
        s_d, t_d = {}, {}
        for i in range(n):
            s_d[s[i]] = s_d.get(s[i], 0) + 1
            t_d[t[i]] = t_d.get(t[i], 0) + 1
        for k, v in s_d.items():
            if k not in t_d or t_d[k] != v:
                return False
        return True