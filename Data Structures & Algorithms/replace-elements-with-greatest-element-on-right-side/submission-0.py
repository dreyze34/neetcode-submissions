class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            greatest = 0
            for j in range(i+1, n):
                greatest = max(greatest, arr[j])
                arr[i] = greatest
        arr[-1] = -1
        return arr