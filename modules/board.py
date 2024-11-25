rows = 6
columns = 7
board = [[" " for _ in range(columns)] for _ in range(rows)]

def print_matrix(matrix: list):
    columns = len(matrix[0])
    print("+" + "   +" * columns)
    for row in matrix:
        print("|", end=" ")
        for element in row:
            print(f"{element} |", end=" ")
        print()
        print("+" + "   +" * columns)
        
def reset_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != " ":
                board[i][j] = " "
            else:
                continue
    return board