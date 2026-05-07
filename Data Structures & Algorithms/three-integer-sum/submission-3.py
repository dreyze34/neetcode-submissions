class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        l = sorted(nums)
        result = []
        for k in range(n-2):
            i, j = k+1, n-1
            if k >= 1 and l[k] == l[k-1]:
                continue
            while i < j:
                s = l[i]+l[j]+l[k]
                if i >= k+2 and l[i] == l[i-1]:
                    i += 1
                elif j <= n-2 and l[j] == l[j+1]:
                    j -= 1
                elif s < 0:
                    i += 1
                elif s > 0:
                    j -= 1
                else:
                    result.append([l[i], l[j], l[k]])
                    i += 1
                    j -= 1
        return result