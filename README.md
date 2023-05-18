# Antiguos proyectos: 
- Imagenes borrosas, latencia en servidor y clasificador de tweets.
- Ejercicios cortos en Python del libro: "Python Workout: 50 ten-minute exercises"

# 19/08/2022:
- TicTacToe / Tres en raya para dos jugadores.

# 06/09/2022:
- Aplicación en Flask con SQLAlchemy (no Frontend).

  Aplicación extremadamente sencilla realizada en Flask para aprender sus pilares. Está conectada con a una BD usando SQLAlchemy.
  Se trata de una página de venta de tickets, donde el usuario selecciona origen y destino y obtiene un ticket; pero debe haber iniciado sesión previamente.
  Se da la opción de comprar ticket, ver los tickets comprados, iniciar sesión y salir.
  Estoy al tanto de los bugs (se comparten los tickets entre usuarios), pero esto es una primera fase experimental.


# 02/10/2022:
- Aplicación que resuelve sudokus a partir de backtracking

  Solo lo he testeado con la version 9x9 que es, a mi parecer la más clasica. 
  Mi idea es añadir una UI para introducir números.
  # 09/10/2022:
    - (NUEVO): Interface implementada:
     - Añadido un sistema para añadir numeros con clicks:
        - Click izquierdo para sumar 1 a la casilla
        - Click derecho para poner a 0 la casilla
        - "Roll" de la rueda del ratón para sumar 1 a la casilla en cada click (es un poco más rapido)
     - Añadido un botón para resolver el sudoku una vez puestos los números.
     - En caso de no tener solución salta un mensaje de error.
     
     La base de la interfaz fue construida a partir de este tutorial: http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

# 18/05/2023:
  Actualizado el proyecto Blur_detector. Se trata de un gestor de imagenes que, dada una ruta con images y una ruta "papelera", mueve todas las imagenes borrosas del primer directorio al segundo.
