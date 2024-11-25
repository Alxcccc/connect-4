from Connect4.modules.board import board, print_board

def put_token_user(user: str):
    while True:
        position_token_user = int(input(f"{user} Ingresa la columna donde deseas poner tu ficha: "))
        position_token_user -= 1
        if position_token_user > 7 or position_token_user < 0 :
            input("El numero de columna que elegiste es incorrecto, solo hay 7 columnas. Pulsa enter para continuar")
        else:
            if board[0][position_token_user] != " ": 
                input("A esta columna ya no le caben fichas, prueba con otra. Pulsa enter para continuar")
            else:
                for columns in range(5,-1,-1): 
                    if board[columns][position_token_user] != " ": 
                        pass
                    else:
                        if user == "red":
                            board[columns][position_token_user] = "r"
                            print_board(board) 
                            break
                        else:
                            board[columns][position_token_user] = "y"
                            print_board(board) 
                            break
                break