class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            if s == "":
                enc = "1a0"
            else:
                u = ""
                for ch in s:
                    u += f"0{ch}0"
                enc = u[:-1] + "1"
            res += enc
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        n = len(s)
        cur = ""
        for i in range(1, n-1, 3):
            print(i)
            if s[i-1] == "1":
                result.append("")
            else:
                cur += s[i]
                if s[i+1] == "1":
                    result.append(cur)
                    cur = ""
        return result
