class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkUnits(units: List[List[str]]):
            for unit in units:
                h = set()
                for el in unit:
                    if el == ".":
                        continue
                    elif el not in h:
                        h.add(el)
                    else:
                        return False
            return True
        n = len(board)
        cols, blocks = [], []
        for j in range(n):
            col = []
            for i in range(n):
                col.append(board[i][j])
            cols.append(col)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                block = []
                for l in range(3):
                    block.extend(board[i+l][j:j+3])
                blocks.append(block)
        return checkUnits(board) and checkUnits(cols) and checkUnits(blocks)
        
