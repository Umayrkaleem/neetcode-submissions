class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        length = 9

        #check rows
        for r in range(length):
            basket = set()
            for c in range(length):
                if board[r][c] == ".":
                    continue

                if board[r][c] in basket:
                    print("1")
                    return False
                basket.add(board[r][c])
        
        #check cols
        for c in range(length):
            basket = set()
            for r in range(length):
                if board[r][c] == ".":
                    continue
                if board[r][c] in basket:
                    print("2")
                    return False
                basket.add(board[r][c])

        #check squares
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True 
                    




