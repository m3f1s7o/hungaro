#! /bin/python3

def obtnrTabla():
    dim = int(input("Dimensiones de la tabla(NxN) N: "));

    matriz = []
    tmp = []
    
    for i in range(dim):
        row = input(f"Valores de la fila {i} (1,2,..,n): ")
        
        # separa los numeros de cada fila y los pone en una lista como enteros
        matriz.append([int(x) for x in row.split(",")])

    return matriz

def defTabla():
    matriz1 = [[230,200,210,240],
           [190,210,200,200],
           [200,180,240,220],
           [220,180,210,230]]
    matriz2 = [[3,5,3,3],
           [5,14,10,10],
           [12,6,19,17],
           [2,17,10,12]]
    return matriz1

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
def paso3(matriz, meta):
    exito = False

    for i in range(len(matriz)):  # recorre toda la matriz
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                
                if posibleAsg(matriz, i, j):  # revisa que la casilla donde hay un 0 pueda asignarse
                    matriz[i][j] = "x";
                   
                    if not exito:  # recursividad
                        paso3(matriz, meta)
                    
                        # si hay igual de asignaciones que la meta, termina porque se encontro la solucion
                        if sum([x.count("x") for x in matriz]) == meta:
                            exito = True
                            break

                        # resetea la casilla a cero para poder seguir buscando soluciones
                        matriz[i][j] = 0

    return matriz, exito


""" identifica si la casilla es apta para asignacion (si no hay otra casilla asignada en la misma fila y columna) """
def posibleAsg(matriz_b, x, y):
    for i in range(len(matriz_b)):
        if matriz_b[x][i] == "x":  # si hay una x en la fila, no es posible
            return False
        
        if matriz_b[i][y] == "x":  # si hay una x en la columna, no es posible
            return False

    return True
    
""" marca filas y columnas """
def paso4(matriz_a):
    matriz_a, e = paso3(matriz_a, len(matriz_a)-1)
    
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

    return matriz_b, m_b

""" suma el menor val a las casillas sin - y lo suma a los demas """
def paso5(matriz_a, matriz_c, col_m):
    matriz_d = []

    min_mb = []

    for i in range(len(matriz_a)):  # obtiene el minimo excluyendo "-"
        for j in range(len(matriz_a)):
            if matriz_c[i][j] != "-":
                min_mb.append(matriz_c[i][j])

    min_mb = min(min_mb)

    for i in range(len(matriz_a)):
        fila = []
        for j in range(len(matriz_a)):
            if matriz_c[i][j] != "-":  # casillas no rayadas - val min
                if matriz_a[i][j] == "x":
                    fila.append(0)

                else:
                    fila.append(matriz_a[i][j] - min_mb)

            else:
                if matriz_a[i][j] == "x": 
                    fila.append(0)

                elif j in col_m and matriz_a[i][j] != 0: # col_m + val min
                    fila.append(matriz_a[i][j] + min_mb)

                else:
                    fila.append(matriz_a[i][j])

        
        matriz_d.append(fila)

    return matriz_d

