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
    while turno < FILAS ** 2:

        print("Turno: " + str(turno + 1))
        turno_jugador("x")
        print_board()
        turno += 1
        if(turno<FILAS**2):
            print("Turno: " + str(turno + 1))
            turno_jugador("o")
            turno += 1
            print_board()

    print("Tablas")
    print("No se puede continuar")
    exit(0)


def turno_jugador(letra_jugador):
    while True:
        try:
            print("Turno del jugador " + str(letra_jugador) + " : ", end=' ')
            player_pos_r, player_pos_c = int(input()), int(input())
        except ValueError:
            print("Por favor introduzca números enteros en un rango válido")
            continue

        while not (FILAS > player_pos_c >= 0 and FILAS > player_pos_r >= 0):
            print("Valores fuera de rango, por favor introduce nuevos: ")
            player_pos_r, player_pos_c = int(input()), int(input())

        if board[player_pos_r, player_pos_c] != "-":
            print("Esa posicion ya está ocupada")

        else:
            board[player_pos_r, player_pos_c] = letra_jugador
            comprobar_tablero(player_pos_r, player_pos_c, letra_jugador)
            break


# Comprueba si existe una jugada ganadora
def comprobar_tablero(f, c, letra_jugador):  # f = filas, c = columnas.
    comprobar_filas(f, letra_jugador)
    comprobar_columnas(c,letra_jugador)
    comprobar_diagonales(letra_jugador)


def comprobar_filas(r, letra_jugador):
    if np.all(board[r] == board[r][0]):
        print_board()
        print("Fila completa")
        print("Gana el jugador " + letra_jugador.upper())
        exit(0)


def comprobar_columnas(c, letra_jugador):
    transposed_matrix = board.transpose()
    if np.all(transposed_matrix[c] == transposed_matrix[c][0]):
        print_board()
        print("Columna completa!")
        print("Gana el jugador "+ letra_jugador.upper())
        exit(0)


def comprobar_diagonales(letra_jugador):
    if np.all(board.diagonal() == letra_jugador) or np.all(np.diagonal(np.fliplr(board)) == letra_jugador):

        print_board()
        print("Diagonal completa!")
        print("Gana el jugador "+ letra_jugador.upper())
        exit(0)


choose()
