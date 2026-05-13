class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        for i in range(n):
            asteroid = asteroids[i]
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] > 0 and abs(stack[-1]) == abs(asteroid):
                    stack.pop()
        return stack
                
