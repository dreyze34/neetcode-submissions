class Solution:

    def encode(self, strs: List[str]) -> str:
        s = "é".join([t+"è" for t in strs])
        print(s, type(s))
        return s

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        else:
            l = s.split("é")
            return [t[:-1] for t in l]