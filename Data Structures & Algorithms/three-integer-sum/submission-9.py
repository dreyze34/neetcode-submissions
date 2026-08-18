class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = sorted(nums)
        print(arr)
        result = []
        for k in range(n):
            target = arr[k]
            if k >= 1 and arr[k] == arr[k-1]:
                continue
            i, j = k+1, n-1
            while i < j:
                s = -(arr[i] + arr[j])
                if s == target:
                    result.append([arr[i], arr[j], arr[k]])
                    c = 1
                    while i+c < j-c and arr[i+c] == arr[i] and arr[j-c] == arr[j]:
                        c += 1
                    i += c
                    j -= c
                elif s > target:
                    i += 1
                else:
                    j -= 1
        return result
            

