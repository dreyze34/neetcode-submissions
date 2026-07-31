class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(s: str, t: str):
            n, m = len(s), len(t)
            if n != m:
                return False
            d_s, d_t = {}, {}
            for i in range(n):
                d_s[s[i]] = d_s.get(s[i], 0) + 1
                d_t[t[i]] = d_t.get(t[i], 0) + 1
            for k, v in d_s.items():
                if k not in d_t or d_t[k] != v:
                    return False
            return True
        result = []
        for s in strs:
            test = False
            for group in result:
                if isAnagram(s, group[0]):
                    group.append(s)
                    test = True
                    break
            if not test:
                result.append([s])
        return result


        
                    
