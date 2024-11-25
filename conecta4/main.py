from board import reset_board
from check_player_win import *
from put_token import *
import os   

tokens = ["red", "yellow"]

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
        option = int(input("Ingrese la opcion que desea: "))
        if option == 1:
            os.system("cls")
            play()
        elif option == 2:
            if reset_score(points):
                print("\nSe ha reiniciado correctamente la puntuacion")
                input()
        elif option == 3:
            break
        else:
            os.system("cls")
            input(f"Ingresaste {option}, este numero no está en nuestras opciones, presiona enter para volver al menu")
            continue


if __name__ == "__main__":
    menu()