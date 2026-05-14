class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        cur = s[0]
        for i in range(1, n):
            if s[i].isdigit() and s[i-1].isalpha():
                stack.append(cur)
                cur = s[i]
            elif s[i] == '[':
                stack.append(int(cur))
                cur = ""
            elif s[i] == ']':
                stack.append(cur)
                cur = ""
                while stack and type(stack[-1]) == str:
                    cur = stack.pop() + cur
                cur *= stack.pop()
                stack.append(cur)
                cur = ""
            else:
                cur += s[i]
        stack.append(cur)
        return "".join(stack)
            

        

