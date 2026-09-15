class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        h = {5: 0, 10: 0, 20: 0}
        for i in range(n):
            change = bills[i] - 5
            bill = 20
            while bill >= 5 and change != 0:
                c = change // bill
                if h[bill] and c:
                    change -= min(h[bill], c) * bill
                    h[bill] -= min(h[bill], c)
                bill = bill // 2
            if change != 0:
                return False
            h[bills[i]] += 1
        return True