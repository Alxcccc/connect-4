import os

rows = 6
columns = 7
board = [[" " for _ in range(columns)] for _ in range(rows)]

points = {
        "r": 0,
        "y": 0
    }   

tokens = ["red", "yellow"]

def print_matrix(matrix: list):
    columns = len(matrix[0])
    print("+" + "   +" * columns)
    for row in matrix:
        print("|", end=" ")
        for element in row:
            print(f"{element} |", end=" ")
        print()
        print("+" + "   +" * columns)

def put_token_user(user: str):
    while True:
        position_token_user = int(input(f"{user} Ingresa la columna donde deseas poner tu ficha: ")) # Aqui el usuario ingresara la columna donde desea poner su ficha
        position_token_user -= 1 # Normalmente el usuario pondra la columna del 1 al 7 pero nuestro sistema funciona de 0 a 6 entonces le restamos 1 a la posicion
        if position_token_user > 7 or position_token_user < 0 : # Si la posicion del token es mayor que 7 o menor que 0 entonces la columnas es incorrecta
            input("El numero de columna que elegiste es incorrecto, solo hay 7 columnas. Pulsa enter para continuar")
        else:
            if board[0][position_token_user] != " ": # Si la primera fila en la columna donde ingreso el usuario la ficha se encuentra llena quiere decir que no caben mas fichas
                input("A esta columna ya no le caben fichas, prueba con otra. Pulsa enter para continuar")
            else:
                for columns in range(5,-1,-1): # Recorremos las columnas de abajo hacia arriba
                    if board[columns][position_token_user] != " ": # Si en la columna 
                        pass
                    else:
                        if user == "red":
                            board[columns][position_token_user] = "r"
                            print_matrix(board) # Nos muestra la board de una forma mas legible para el jugador
                            break
                        else:
                            board[columns][position_token_user] = "y"
                            print_matrix(board) # Nos muestra la board de una forma mas legible para el jugador
                            break
                break
            
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


def play():
    turn = 0
    print_matrix(board)
    print(points)
    while True:
        opcion = input("Si deseas reiniciar la partida escribe 'r' o deseas salir de la partida escribe 'e' , si solo quiere continuar con la partida presiona enter: ")
        if opcion == "r":
            input("Se reinicio la partida, porfavor presiona enter")
            reset_board(board)
            turn = 0
            print_matrix(board)
            print(points)
        elif opcion == "e":
            reset_board(board)
            break
        else:
            if turn == 0:
                put_token_user(tokens[turn])
                win = score(board, points)
                if win != None:
                    print(points)
                    input()
                    reset_board(board)
                    break
                else:
                    turn = 1
            else:
                win = None
                if win != None:
                    print(points)
                    input()
                    reset_board(board)
                    break
                else:
                    win = score(board, points)
                    put_token_user(tokens[turn])
                    turn = 0

def reset_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != " ":
                board[i][j] = " "
            else:
                continue
    return board

def reset_score(points):
    points["r"] = 0
    points["y"] = 0
    return True

def menu():
    while True:
        os.system("cls")
        print("""
              
              Conecta 4
              
              1: Jugar Conecta 4
              2: Reiniciar Puntuacion
              3: Salir
              
        
        By: 
                    
        ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
        ░▒▓████████▓▒░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░        
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
                                                            
                                                      

              """)
        option = int(input("Ingresa la opcion que quieras: "))
        if option == 1:
            os.system("cls")
            play()
        elif option == 2:
            if reset_score(points):
                print("\nSe ha reiniciado correctamente la puntuacion")
                input()
            else:
                print("Ocurrio un error al reiniciar puntuacion")
        elif option == 3:
            break
        else:
            os.system("cls")
            input(f"Ingresaste {option}, este numero no está en nuestras opciones, presiona enter para volver al menu")
            continue


if __name__ == "__main__":
    menu()