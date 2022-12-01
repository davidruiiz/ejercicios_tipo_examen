"""
EJERCICIO SUMA SIMPLE DE UNA MATRIZ
Dada una matriz de números enteros N, encuentre la suma de sus elementos.
Función descriptiva
Complete la función simpleArraySum . Debe devolver la suma de los elementos de la matriz como un número entero.
simpleArraySum tiene los siguientes parámetros:
ar : una matriz de números enteros
Formato de entrada
La primera línea contiene un número entero, N, que denota el tamaño de la matriz.
La segunda línea contiene N enteros separados por espacios que representan los elementos de la matriz.
Código Inicial
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the simpleArraySum function below.
def simpleArraySum(ar):
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()