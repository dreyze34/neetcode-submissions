class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = sorted(nums)
        result = []
        for i in range(n):
            l, r = i + 1, n-1
            if i > 0 and arr[i] == arr[i-1]:
                continue
            while l < r:
                if l > i + 1 and arr[l] == arr[l-1]:
                    l += 1
                elif r < n-1 and arr[r] == arr[r+1]:
                    r -= 1
                else:
                    s = arr[i] + arr[l] + arr[r]
                    if s == 0:
                        result.append([arr[i], arr[l], arr[r]])
                        l += 1
                        r -= 1
                    elif s > 0:
                        r -= 1
                    else:
                        l += 1
        return result
            


