
class Sudoku:

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(board, to_fill, filled):
            if not to_fill:
                return
            i, j = to_fill.pop()
            filled.append((i, j))

            row = [board[i][k] for k in range(9)]
            col = [board[k][j] for k in range(9)]
            square_3by3 = [board[i//3*3 + x][j//3*3 + y] for x in range(3) for y in range(3)]

            for x in "123456789":
                if not (x in square_3by3 or x in row or x in col):
                    board[i][j] = x
                    dfs(board, to_fill, filled)
                    print(len(to_fill))
                    if not to_fill:
                        return
            position = filled.pop()
            to_fill.append(position)
            board[i][j] = "."



        to_fill = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]
        filled = []
        dfs(board, to_fill, filled)





def main():
    s = Sudoku()

    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(board)

if __name__ == "__main__":
    main()