class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        result = []
        for i in range(n):
            s = strs[i]
            new = True
            for j in range(len(result)):
                t = result[j][0]
                ds = {}
                dt = {}
                n, m = len(s), len(t)
                if n == m:
                    for idx in range(n):
                        ds[s[idx]] = ds.get(s[idx], 0)+1
                        dt[t[idx]] = dt.get(t[idx], 0)+1
                    anagram = True
                    for k, v in ds.items():
                        l = dt.get(k)
                        if l != v:
                            anagram = False
                            break
                    if anagram:
                        result[j].append(s)
                        new = False
            if new:
                result.append([s])

        return result
                
                


