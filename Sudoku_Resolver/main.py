import numpy as np
import pygame
import sys
import pygame_gui



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
    interface()
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



def interface():
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    WIDTH = 82
    HEIGHT = 82
    MARGIN = 2

    WINDOWS_SIZE = [760, 830]

    pygame.init()
    screen = pygame.display.set_mode(WINDOWS_SIZE)
    pygame.display.set_caption("Sudoku Resolver")




    color = (255, 255, 255)
    smallfont = pygame.font.Font(None, 35)
    text = smallfont.render('Resolve', True, color)





    click = False

    clock = pygame.time.Clock()
    pygame.init()
    while not click:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                click = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 320 <= pos[0] <= 320 + 140 and 760 <= pos[1] <= 760 + 60:
                    click = False
                    solution()
                if event.button != 3:
                    # User clicks the mouse. Get the position
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    try:
                        num = grid[row][column]
                        num += 1
                        grid[row][column] = num % 10
                    except:

                        smallfont = pygame.font.Font(None, 55)
                        error_text = smallfont.render('No tiene solucion', True, BLACK)
                        pygame.draw.rect(screen, RED, [225, 750/3, 400, 50])
                        screen.blit(error_text, (225+20, 750/3))

                        pygame.display.flip()
                        pygame.time.wait(1000)


                else:
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    grid[row][column] = 0

        # Set the screen background
        screen.fill(BLACK)

        # Draws button

        pygame.draw.rect(screen, GREEN, [320, 760, 140, 60])
        screen.blit(text, (345, 780))



        # Draw the grid
        for row in range(9):
            for column in range(9):
                color = WHITE
                if (row % 3 == 0) or (column % 3 == 0):
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
                else:
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])

                number_font = pygame.font.Font(None, 70)
                number_image = number_font.render(str(grid[row][column]), True, BLACK, WHITE)
                screen.blit(number_image, [30 + (MARGIN + WIDTH) * column + MARGIN,
                                  20 + (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        # Limit to 60 frames per second
        clock.tick(60)


        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()








if __name__ == '__main__':
    grid  =\
              [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    interface()
    #print(np.matrix(grid))
    print("No tiene solucion")

















