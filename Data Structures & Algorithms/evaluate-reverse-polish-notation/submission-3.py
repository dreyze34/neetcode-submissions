class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+", "-", "*", "/"])
        stack = []
        for ch in tokens:
            if ch not in operators:
                stack.append(int(ch))
            else:
                a, b = stack.pop(), stack.pop()
                print(a, b, ch)
                if ch == "+":
                    stack.append(a+b)
                elif ch == "-":
                    stack.append(b-a)
                elif ch == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
        return stack[0]
                        