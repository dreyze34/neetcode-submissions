class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x // 2
        if x == 1 or x == 0:
            return x
        while left <= right:
            mid = (right + left) // 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                left = mid + 1
            else:
                right = mid - 1
        return right