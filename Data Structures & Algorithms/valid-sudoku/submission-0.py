class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                currentVal = board[r][c]
                if currentVal == ".":
                    continue
                if (currentVal in cols[c] or
                    currentVal in rows[r] or
                    currentVal in squares[(r//3,c//3)]):
                    return False
                cols[c].add(currentVal)
                rows[r].add(currentVal)
                squares[(r//3,c//3)].add(currentVal)

        
        return True 