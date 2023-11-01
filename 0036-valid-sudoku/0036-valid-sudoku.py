class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setRows =   collections.defaultdict(set)
        setCols = collections.defaultdict(set)
        setSquares = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in setRows[i]) or (board[i][j] in setCols[j]) or (board[i][j] in setSquares[(i // 3, j // 3)]):
                    return False
                else:   
                   setRows[i].add(board[i][j])
                   setCols[j].add(board[i][j])
                   setSquares[i//3, j//3].add(board[i][j])
        
        return True