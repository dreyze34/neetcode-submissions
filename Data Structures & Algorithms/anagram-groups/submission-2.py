class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        d = {}
        for s in strs:
            t = ''.join(sorted(s))
            if t in d:
                d[t].append(s)
            else:
                d[t] = [s]
        return list(d.values())
                
                


