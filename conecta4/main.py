tablero = [[" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "]]

users = ["red", "yellow"]

def imprimir_matriz_con_lineas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    print("+" + "   +" * columnas)
    for fila in matriz:
        print("|", end=" ")
        for elemento in fila:
            print(f"{elemento} |", end=" ")
        print()
        print("+" + "   +" * columnas)

def poner_ficha_user(user):
    while True:
        column_user = int(input(f"{user} Ingresa la columna donde deseas poner tu ficha: "))
        column_user -= 1
        if column_user > 7 or column_user < 0 :
            input("El numero de columna que elegiste es incorrecto, solo hay 7 columnas. Pulsa enter para continuar")
        else:
            if tablero[0][column_user] != " ":
                imprimir_matriz_con_lineas(tablero)
                input("A esta columna ya no le caben fichas, prueba con otra. Pulsa enter para continuar")
            else:
                for i in range(5,-1,-1):
                    print(i)
                    if tablero[i][column_user] != " ":
                        pass
                    else:
                        if user == "red":
                            tablero[i][column_user] = "r"
                            break
                        else:
                            tablero[i][column_user] = "y"
                            break
                imprimir_matriz_con_lineas(tablero)
                break

def revisar_vertical(tablero):
    for i in range(len(tablero)):
        for j in range(5,-1,-1):
            c = str()
            countvr = 0
            countvy = 0
            print("awo1")
            while countvr > 4 or countvy > 4:
                print("awo2")
                if tablero[j][i] == "r":
                    countvy = 0
                    countvr += 1
                    c = "r"
                if tablero[j][i] == "y":
                    countvr = 0
                    countvy += 1
                    c = "y"
                if j == 5 and i == 0:
                    c = None
                    break
            print(f"Verticalmente ganó: {c}")
            

def turnos():
    turno = 0
    while True:
        if turno == 0:
            poner_ficha_user(users[turno])
            turno = 1
        else:
            poner_ficha_user(users[turno])
            turno = 0

revisar_vertical(tablero)