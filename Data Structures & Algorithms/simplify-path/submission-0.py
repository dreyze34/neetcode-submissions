class Solution:
    def simplifyPath(self, path: str) -> str:
        sep = ['/', '..', '.']
        stack = []
        strs = path.split('/')
        for s in strs:
            if s == '..':
                if stack:
                    stack.pop()
            elif s and s != '.':
                stack.append(s)
        return '/' + '/'.join(stack)

