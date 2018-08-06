from collections import Counter

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.is_row_valid(board) and self.is_col_valid(board) and self.is_3by3_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_valid(col):
                return False
        return True

    def is_3by3_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                row_or_col = [board[m][n] for m in range(i, i+3) for n in range(j, j+3)]
                print(row_or_col)
                if not self.is_valid(row_or_col):
                    return False
        return True

    def is_valid(self, row_or_col):
        row_or_col = [x for x in row_or_col if x != "."]
        return len(set(row_or_col)) == len(row_or_col)



def main():
    s = Solution()
    print(s.isValidSudoku([["5","3","5","6","7","6","4","2","1"],["6","4","2","1","9","5","4","3","2"],["1","9","8","4","3","2","2","6","1"],["8","5","4","5","6","4","2","1","3"],["4","4","3","8","4","3","3","2","1"],["7","2","1","3","2","1","2","1","6"],["3","6","3","3","3","2","2","8","1"],["2","2","2","4","1","9","2","1","5"],["1","1","1","2","8","1","1","7","9"]]))

if __name__ == "__main__":
    main()