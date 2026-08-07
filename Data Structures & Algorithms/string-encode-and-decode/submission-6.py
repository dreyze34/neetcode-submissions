class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}/" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        i = 0
        t = ""
        decoded = []
        while i < len(s):
            if s[i] == "/":
                l = int(t)
                decoded.append(s[i+1:i+l+1])
                i += l+1
                t = ""
            else:
                t += s[i]
                i += 1
        return decoded
