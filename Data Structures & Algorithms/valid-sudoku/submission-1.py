class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            dl = set()
            dc = set()
            for j in range(n):
                if board[i][j] in dl:
                    return False
                elif board[j][i] in dc:
                    return False
                if board[i][j] != '.':
                    dl.add(board[i][j])
                if board[j][i] != '.':
                    dc.add(board[j][i])
        blocs = [(i, j) for i in (0, 3, 6) for j in (0, 3, 6)]
        deltas = [(i, j) for i in (0, 1, 2) for j in (0, 1, 2)]
        for i, j in blocs:
            db = set()
            for di, dj in deltas:
                if board[i+di][j+dj] in db:
                    return False
                if board[i+di][j+dj] != '.':
                    db.add(board[i+di][j+dj])

        return True
                
        