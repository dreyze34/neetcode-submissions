class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for ch in s:
            if ch in d:
                stack.append(ch)
            elif not stack:
                return False
            else:
                last = stack.pop()
                if d[last] != ch:
                    return False
        if stack:
            return False
        return True
