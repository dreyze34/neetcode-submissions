class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        ops = set(["+", "C", "D"])
        for op in operations:
            print(record, op)
            if op not in ops:
                record.append(int(op))
            elif op == "+":
                record.append(record[-1]+record[-2])
            elif op == "C":
                record.pop()
            else:
                record.append(2*record[-1])
        return sum(record)