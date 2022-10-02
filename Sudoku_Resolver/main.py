import numpy as np
import PySimpleGUI as sg

global grid


def solution():
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                for k in range(1, 10):
                    if comprobar(i, j, k):
                        grid[i][j] = k
                        solution()
                        grid[i][j] = 0
                return
    print("Solucion: ")
    print(np.matrix(grid))
    exit()

def comprobar(x, y, numero):
    for i in range(0, 9):
        if grid[x][i] == numero or grid[i][y] == numero:
            return False

    # Ya que dentro de los cuadrados 3x3 que componen el mayor 9x9 no se pueden repetir numeros,
    # se obtiene en que cuadrado 3x3 se encuentra el numero candidato
    # con "//" nos asegura un valor entero, despues se multiplica por 3 para obtener la casilla en la que empieza la que
    #  comienza la celda
    # Por ejemplo, casilla (5,6), se obtiene Cuadrado(1,2), es decir:  _ _ _  donde cada "_" es 3x3
    #                                                                  _ _ _
    #                                                                  _ _ X

    cuadricula_x = (x // 3) * 3
    cuadricula_y = (y // 3) * 3

    for i in range(cuadricula_x, cuadricula_x+2):
        for j in range(cuadricula_y, cuadricula_y+2):
            if grid[i][j] == numero:
                return False
    return True



if __name__ == '__main__':
    grid =\
             [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    print(np.matrix(grid))
    solution()
    print("No tiene solucion")
















def interface():
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Some text on Row 1')],
              [sg.Text('Enter something on Row 2'), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()
