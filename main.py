#!/bin/python3

from tabulate import tabulate

def obtnrTabla():
    dim = int(input("Dimensiones de la tabla(NxN) N: "));

    matriz = []
    tmp = []
    
    for i in range(dim):
        row = input(f"Valores de la fila {i} (1,2,..,n): ")
        
        matriz.append(row.split(","))

    return matriz

def defTabla():
    return[[230,200,210,240],
           [190,210,200,200],
           [200,180,240,220],
           [220,180,210,230]]


""" seleccionar el valor mas pequeño de cada columna y restarlo con la columna """
def paso1(matriz):

    min_col = []
    for i in range(len(matriz)):
       min_col.append(min([c[i] for c in matriz]))  # obtiene el val minimo de cada columna 
    
    matriz_a = []
    for i in range(len(matriz)):  # resta el minimo de cada columna con toda la columna
        fila = [int(f) - int(m) for f, m in zip(matriz[i], min_col)] 

        matriz_a.append(fila)

    return matriz_a
    
""" seleccionar el valor mas pequeño de cada fila y restarlo con la fila """
def paso2(matriz_a):
    min_fil = []

    for fila in matriz_a:
        min_fil.append(min(fila))  # obtiene el min valor de cada fila
    
    matriz_b = []
    for i in range(len(matriz_a)):  # resta el minimo de cada fila con toda la fila
        fila = [int(f) - min_fil[i] for f in matriz_a[i]]

        matriz_b.append(fila)

    return matriz_b

""" realiza todas las asignaciones posibles """
def paso3(matriz_a, recursivo):
    exito = False

    for i in range(len(matriz_a)):
        for j in range(len(matriz_a)):
            if matriz_a[i][j] == 0:
                
                if posibleAsg(matriz_a, i, j):
                    matriz_a[i][j] = "x";
                   
                    if(recursivo):
                        paso3(matriz_a, recursivo)
                    
                        # si hay igual de asignaciones que el tamaño de la tabla, termina
                        if sum([x.count("x") for x in matriz_a]) == len(matriz_a):
                            exito = True
                            break

                            matriz_a[i][j] = 0

    return matriz_a, exito


""" identifica si la casilla es apta para asignacion """
def posibleAsg(matriz_b, x, y): 
    for i in range(len(matriz_b)):
        if matriz_b[x][i] == "x": 
            return False
        
        if matriz_b[i][y] == "x":
            return False

    return True
    
""" marca filas y columnas """
def paso4(matriz_a):
    matriz_a, e = paso3(matriz_a, False)
    
    m_a = []  # filas que no tienen asignaciones
    for i in range(len(matriz_a)):
        if matriz_a[i].count("x") == 0:
            m_a.append(i)

    m_b = []  # columnas con 0 en las filas de la marca a
    for i in range(len(matriz_a)):
        for j in range(len(m_a)):
            if matriz_a[m_a[j]][i] == 0:
                m_b.append(i)
    
    m_c = []  # filas con asignacion de las col de la marca b
    for i in range(len(matriz_a)):
        for j in range(len(m_b)):
            if matriz_a[i][m_b[j]] == "x":
                m_c.append(i)

    # linea en las casillas de filas que no estan marcadas y columnas marcadas
    matriz_b = []
    for i in range(len(matriz_a)):
        fila = []
        for j in range(len(matriz_a)):
            if (i in m_a or i in m_c) and j not in m_b:
                fila.append(matriz_a[i][j])
            
            else:
                fila.append("-")
        
        matriz_b.append(fila)

    return matriz_b



def main():
   #matriz = obtnrTabla()
   matriz = defTabla()
   titulos = ["C" + str(i) for i in range(len(matriz))]

   print(tabulate(matriz, headers=titulos, tablefmt="psql"))

   matriz_a = paso1(matriz)
   print(tabulate(matriz_a, headers=titulos, tablefmt="psql"))

   matriz_a = paso2(matriz_a)
   print(tabulate(matriz_a, headers=titulos, tablefmt="psql"))

   matriz_a, exito = paso3(matriz_a, True)

   if not exito:
       matriz_b = paso4(matriz_a)
       print(tabulate(matriz_b, headers=titulos, tablefmt="psql"))

   else:
       print(tabulate(matriz_a, headers=titulos, tablefmt="psql"))






if __name__ == "__main__":
    main()
