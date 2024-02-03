# CI5651 - Diseño de Algoritmos I. Trimestre Enero - Marzo 2024
# Roberto Gamboa, 16-10394
# Tarea 3. Ejercicio 2

import numpy as np 

# Función para calcular la potencia de una matriz.
# Se utiliza la estrategia de "Divide y Conquista" para calcular la potencia de una matriz
# Cuando la potencia es par, se divide el problema a la mitad y se resuelve el subproblema de tamaño n/2.
# Para luego hallar el resultado multiplicando la matriz resultante por sí misma.
# Cuando la potencia es impar, se resta 1 y se divide el problema a la mitad para resolver el subproblema de tamaño n-1 
# (que será par y se procede como en el caaso anterior).
# Luego se multiplica la matriz por el resultado del subproblema de tamaño n-1.
# De esta manera se asegura que la potenciacion de matriz tome tiempo Θ(log n).
def potenciacion_matriz(matriz, potencia):
    if potencia == 1:
        return matriz
    # Si n es par, se divide el problema a la mitad.
    elif potencia % 2 == 0:  
        mitad_potencia = potenciacion_matriz(matriz, potencia // 2)
        # Multiplica las dos matrices.
        return np.dot(mitad_potencia, mitad_potencia)  
    # Si n es impar, se resta 1 y se divide el problema a la mitad.
    else:  
        # Multiplica la matriz por el resultado del subproblema de tamaño n-1.
        return np.dot(matriz, potenciacion_matriz(matriz, potencia - 1))

# Función para calcular el n-ésimo número de Perrin
# siguiendo la definición: 
    #P(0) = 3, P(1) = 0, P(2) = 2
    #P(n) = P(n-2) + P(n-3) para n >= 3
def perrin(n):

    # Casos base
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    else:
        # Matriz de transición de los numeros de Perrin
        matriz_trans = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 0]], dtype=np.int64)
        # Calcula la potencia (n-1) de la matriz de transición
        matriz_resultante = potenciacion_matriz(matriz_trans, n)
        vector_inic = np.array([3, 0, 2])
        # Multiplica la matriz resultante por el vector inicial y devuelve el primer elemento P(n)
        return np.dot(matriz_resultante, vector_inic)[0]  



for i in [2,3,4,5,6,7,10,12,20,21,24,34,38,75,100]:
    print(f'P({i}) = {perrin(i)}')

