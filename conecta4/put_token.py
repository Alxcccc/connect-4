from board import board, print_matrix

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