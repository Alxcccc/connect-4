def check_diagonal_right(board):
    for rows in range(len(board)-1,-1,-1):
        for columns in range(len(board)+1):
            conr = 0
            cony = 0
            if board[rows][columns] != " ":
                if columns+3 > len(board): 
                    return False
                for i in range(4):
                    if board[rows][columns] == "r":
                        if board[rows-i][columns+i] == "r":
                            conr +=1
                            if conr == 4:
                                return "r"
                        else:
                            conr = 0
                    elif board[rows][columns] == "y":
                        if board[rows-i][columns+i] == "y":
                            cony +=1
                            if cony == 3:
                                return "y"
                        else:
                            cony = 0

def check_diagonal_left(board):
    for rows in range(len(board)-1,-1,-1):
        for columns in range(len(board), -1, -1):
            conr = 0
            cony = 0
            if board[rows][columns] != " ":
                if columns-3 < 0: 
                    return False
                for i in range(4):
                    if board[rows][columns] == "r":
                        if board[rows-i][columns-i] == "r":
                            conr +=1
                            if conr == 4:
                                return "r"
                        else:
                            conr = 0
                    elif board[rows][columns] == "y":
                        if board[rows-i][columns-i] == "y":
                            cony +=1
                            if cony == 3:
                                return "y"
                        else:
                            cony = 0


def check_vertical(board):
    for rows in range(len(board)+1):
        conr = 0
        cony = 0
        for columns in range(5,-1,-1):
            if board[columns][rows] == "r":
                cony = 0
                conr += 1
                if conr == 4:
                    return "r"
            elif board[columns][rows] == "y":
                conr = 0
                cony += 1
                if cony == 4:
                    return "y"
            else:
                conr = 0
                cony = 0
    return None

def check_horizontal(board):
    for columns in range(len(board)):
        conr = 0
        cony = 0
        for rows in range(len(board)+1):
            if board[columns][rows] == "r":
                cony = 0
                conr += 1
                if conr == 4:
                    return "r"
            elif board[columns][rows] == "y":
                conr = 0
                cony += 1
                if cony == 4:
                    return "y"
            else:
                conr = 0
                cony = 0
    return None

points = {
        "r": 0,
        "y": 0
    }  

def score(board, points):
    if check_vertical(board) == "r" or check_horizontal(board) == "r" or check_diagonal_right == "r" or check_diagonal_left == "r":
        points["r"] += 1
        print("El ganador de esta ronda es el rojo")
        return "r"
    elif check_vertical(board) == "y" or check_horizontal(board) == "y" or check_diagonal_right == "y" or check_diagonal_left == "y":
        points["y"] += 1
        print("El ganador de esta ronda es el amarillo")
        return "y"
    else:
        return None
    
def reset_score(points):
    points["r"] = 0
    points["y"] = 0
    return True