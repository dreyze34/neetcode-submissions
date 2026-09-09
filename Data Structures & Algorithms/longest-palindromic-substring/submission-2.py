class Solution:
    def longestPalindrome(self, s: str) -> str:
        def oddPalindrom(s):
            n = len(s)
            longestPalindrom = ""
            for i in range(n):
                j = 0
                while i - j >= 0 and i + j < n and s[i-j] == s[i+j]:
                    j += 1
                
                if not longestPalindrom:
                    longestPalindrom = s[i-j+1:i+j]
                if 2 * (j-1) >= len(longestPalindrom):
                    longestPalindrom = s[i-j+1:i+j]
            return longestPalindrom

        def evenPalindrom(s):
            n = len(s)
            longestPalindrom = ""
            for i in range(n-1):
                j = i + 1
                k = 0
                while i - k >= 0 and j + k < n and s[i - k] == s[j + k]:
                    k += 1

                if 2 * k > len(longestPalindrom):
                    longestPalindrom = s[i-k+1:j+k]
                
            return longestPalindrom
        print(evenPalindrom(s), oddPalindrom(s))
        return max(evenPalindrom(s), oddPalindrom(s), key=len)

