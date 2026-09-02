class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m = len(word), len(abbr)
        i, j = 0, 0
        num = ""
        while i < m:
            ch = abbr[i]
            if ch.isdigit():
                num += ch
                i += 1
            else:
                if num:
                    if num[0] == "0" and len(num) > 0:
                        return False
                    if j + int(num) >= n:
                        return False
                    if ch != word[j+int(num)]:
                        return False
                    j += int(num)+1
                    i += 1
                    num = ""
                else:
                    if ch != word[j]:
                        return False
                    i += 1
                    j += 1
        if num:
            if j + int(num) != n:
                return False
        return True
            

                