class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        d_queue = [i for i in range(n) if senate[i] == 'D']
        r_queue = [i for i in range(n) if senate[i] == 'R']
        i, j = 0, 0
        while i < len(d_queue) and j < len(r_queue):
            d, r = d_queue[i], r_queue[j]
            if d < r:
                d_queue.append(d + n)
            else:
                r_queue.append(r + n)
            i += 1
            j += 1
        return "Radiant" if i == len(d_queue) else "Dire"

