class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = 0
        start = 0
        for r in range(1, n):
            if chars[r] != chars[start]:
                count = r - start
                chars[l] = chars[start]
                l += 1
                if count > 1:
                    s = str(count)
                    for k in range(len(s)):
                        chars[l] = s[k]
                        l += 1
                start = r
        count = n - start
        chars[l] = chars[start]
        l += 1
        if count > 1:
            s = str(count)
            for k in range(len(s)):
                chars[l] = s[k]
                l += 1
        return l

                    
