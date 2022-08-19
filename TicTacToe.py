import numpy as np

FILAS = 3
COLUMNAS = 3
board = np.full((FILAS, COLUMNAS), "-", dtype=object)


def print_board():
    next_line = 0

    for i in range(3):

        print(*board[i])

        next_line += 1
        if next_line == 3:
            print("\n")
            next_line = 0


def choose():
    turno = 0
    print_board()
    while turno < FILAS**2:

        print("Turno: " + str(turno + 1))
        turno_jugador("x")
        print_board()
        turno += 1

        if turno < FILAS:
            print("Turno: " + str(turno + 1))
            turno_jugador("o")
            turno += 1

        print_board()


def turno_jugador(letra_jugador):
    while True:
        try:
            print("Turno del jugador " + str(letra_jugador) + " : ", end=' ')
            player_pos_r, player_pos_c = int(input()), int(input())
        except:
            print("Por favor introduzca números enteros en un rango válido")
            continue

        while not (FILAS > player_pos_c >= 0 and FILAS > player_pos_r >= 0):
                print("Valores fuera de rango, por favor introduce nuevos: ")
                player_pos_r, player_pos_c = int(input()), int(input())

        if board[player_pos_r, player_pos_c] != "-":
            print("Esa posicion ya está ocupada")

        else:
            board[player_pos_r, player_pos_c] = letra_jugador
            comprobar_tablero(player_pos_r, player_pos_c)
            break


# Comprueba si existe una jugada ganadora
def comprobar_tablero(f, c):  # f = filas, c = columnas.
    comprobar_filas(f)
    comprobar_columnas(c)
    comprobar_diagonales()


def comprobar_filas(r):
    if np.all(board[r] == board[r][0]):
        print("Fila completa")
        print_board()
        exit(0)


def comprobar_columnas(c):
    transposed_matrix = board.transpose()
    if np.all(transposed_matrix[c] == transposed_matrix[c][0]):
        print("Columna completa!")
        print_board()
        exit(0)


def comprobar_diagonales():
    if np.all(board.diagonal() == "x") or np.all(np.diagonal(np.fliplr(board)) == "x") or \
            np.all(board.diagonal() == "o") or np.all(np.diagonal(np.fliplr(board)) == "o"):
        print("Diagonal completa!")
        print_board()
        exit(0)


choose()
