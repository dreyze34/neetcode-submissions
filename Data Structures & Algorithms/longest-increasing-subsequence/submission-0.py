class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(1, nums[0])]
        for i in range(1, n):
            maxLenght = 1
            for j in range(i):
                lenght, maxEl = dp[j]
                if nums[i] > maxEl and lenght + 1 > maxLenght:
                    maxLenght = lenght + 1
            dp.append((maxLenght, nums[i]))
        return max(dp)[0]

                

