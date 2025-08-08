class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])      
                squares[(r//3, c//3)].add(board[r][c])
        return True
    

# also:
class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            row = set()
            col = set()
            square = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
                br = (i // 3) * 3 + (j // 3)
                bc = (i % 3)  * 3 + (j % 3)
                if board[br][bc] != ".":
                    if board[br][bc] in square:
                        return False
                    square.add(board[br][bc])

        return True
