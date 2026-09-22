class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        h = {order[k]: k for k in range(len(order))}
        i = 0
        while i < n - 1:
            word, next_word = words[i], words[i+1]
            for j in range(len(word)):
                if j >= len(next_word):
                    return False
                elif h[word[j]] > h[next_word[j]]:
                    return False
                elif h[word[j]] < h[next_word[j]]:
                    break
            i += 1
        return True


