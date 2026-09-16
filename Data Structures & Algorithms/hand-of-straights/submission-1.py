class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        hand.sort()
        h = {}
        for i in range(n):
            h[hand[i]] = h.get(hand[i], 0) + 1
            
        for i in range(n):
            start = hand[i]
            if not h[start]:
                continue
            for j in range(groupSize):
                if not start + j in h or h[start + j] == 0:
                    return False
                h[start + j] -= 1
        return True



        