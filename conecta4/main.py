from board import reset_board
from check_player_win import *
from put_token import *
import os   

tokens = ["red", "yellow"] # Esto simboliza las fichas que están disponibles en este conecta 4 en este caso es red y yellow

def play():
    """
    Esta funcion se encarga de ir poniendo las fichas de acuerdo al turno
    """
    turn = 0 # Turno 0 que en este caso representa la posicion 0 de la lista token de la linea 6, lo cual turn = 0 es lo mismo que decir que el turno es del rojo
    print_matrix(board) # Mostramos el tablero antes de colocar las fichas
    print(points) # Mostramos los puntos antes de colocar las fichas
    while True: # Bucle que se mantiene en True si no se cierra con un break
        opcion = input("Si deseas reiniciar la partida escribe 'r' o deseas salir de la partida escribe 'e' , si solo quiere continuar con la partida presiona enter: ") # Entrada de usuario
        if opcion == "r": # Si la opcion que escogio el usuario es r procedemos a reiniciar la partida
            input("Se reinicio la partida, porfavor presiona enter") # Mostramos un mensaje avisando que reiniciamos la partida
            reset_board(board) # Llamamos la funcion reset_board y le pasamos como parametro el tablero que estabamos utilizando
            turn = 0 # Como siempre empieza el rojo por lo tanto ponemos turn en 0
            print_matrix(board) # Utilizamos la funcion print_matrix para mostrar el tablero reiniciado
            print(points) # Mostramos en pantalla como va el puntaje
        elif opcion == "e": # Si la opcion que escogio el usuario es e procedemos a reiniciar el tablero y cerrar el bucle
            reset_board(board) # Reiniciamos el tablero
            break # Salimos del bucle para volver al menu
        else: # Si por el contrario presionó enter o alguna otra tecla simplemente iniciamos a poner las fichas
            if turn == 0: # Si turn es 0 osea rojo
                put_token_user(tokens[turn]) # Llamamos la funcion put_token_user y como parametro le damos el usuario que tiene el turno
                win = score(board, points) # Creamos una varible win y como valor llamanos la funcion score, como parametros le damos nuestra tablero y los puntos que tiene cada usuario
                if win != None: # Si la funcion score retorna que hay un ganador
                    print(points) # Mostramos los puntos
                    input() # Dejamos un espacio en blanco para que el usuario pueda ver la informacion anterior y cuando presione enter continuar con lo demas
                    reset_board(board) # Reiniciamos el tablero porque se inicia una partida nueva
                    break # Detenemos el while provocando que volvamos al menu
                else: # Si la funcion no retorna ningun ganador simplemente seguimos alternando entre turnos
                    turn = 1 # Le damos como valor a turno el numero uno, indicando que el turno es para amarillo
            else:
                put_token_user(tokens[turn]) # Llamamos la funcion put_token_user y como parametro le damos el usuario que tiene el turno
                win = score(board, points) # Creamos una varible win y como valor llamanos la funcion score, como parametros le damos nuestra tablero y los puntos que tiene cada usuario
                if win != None: # Si la funcion score retorna que hay un ganador
                    print(points) # Mostramos los puntos
                    input() # Dejamos un espacio en blanco para que el usuario pueda ver la informacion anterior y cuando presione enter continuar con lo demas
                    reset_board(board) # Reiniciamos el tablero porque se inicia una partida nueva
                    break # Detenemos el while provocando que volvamos al menu
                else: # Si la funcion no retorna ningun ganador simplemente seguimos alternando entre turnos
                    turn = 0 # Le damos como valor a turno el numero uno, indicando que el turno es para amarillo
                    

def conecta4():
    while True:
        os.system("cls") # De la clase os importamos la funcion system que nos permite poner comandos del cmd, con esto limpiamos la terminal
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
        


              """) # Mostramos un menu de opciones
        option = input("Ingrese la opcion que desea: ") # Ya al dejar que el usuario vea las opciones procedemos a pedir la opcion
        if option == "1": # Si el usuario ingresa 1
            os.system("cls") # Limpiamos la consola
            play() # llamamos la funcion play para empezar a jugar conecta 4
        elif option == "2": # Si el usuario ingresa 2
            if reset_score(points): # Si la funcion reset_score nos devuelve un true
                print("\nSe ha reiniciado correctamente la puntuacion") # Mostramos al usuario que la puntuacion se reinicio correctamente
                input() # Dejamos un espacio en blanco para que el usuario vea la informacion antes de presionar enter
        elif option == "3": # Si el usuario ingresa 3
            break # Salimos del bucle del menu y se cierra automaticamente el juego
        else: # Si el usuario no ingresa ninguna opcion valida
            os.system("cls") # Limpiamos la terminal 
            input(f"Ingresaste {option}, este numero no está en nuestras opciones, presiona enter para volver al menu") # Le indicamos al usuario que la opcion que puso no pertenece a nuestro menu de opciones
            continue # Simplemente continuamos el while sin ningun cambio para que vuelva a ingresar una opcion


if __name__ == "__main__":
    conecta4() # Inicializamos el juego