#! /bin/python3

""" selecciona el valor mas pequeño de cada columna y lo resta con la columna """
def paso1(matriz):
    tam = len(matriz)

    min_col = []  # para almacenar los minimos
    for i in range(tam):
       min_col.append(min([c[i] for c in matriz]))  # obtiene el val minimo de cada columna 
    
    nueva_m = []
    for i in range(tam):  # resta el minimo de cada columna con toda la columna
        fila = [int(f) - int(m) for f, m in zip(matriz[i], min_col)] 

        nueva_m.append(fila)

    return nueva_m
    
""" selecciona el valor mas pequeño de cada fila y lo resta con la fila """
def paso2(matriz):
    tam = len(matriz)
    min_fil = []  # para almacenar los minimos de cada fila

    for fila in matriz:
        min_fil.append(min(fila))  # obtiene el min valor de cada fila
    
    nueva_m = []
    for i in range(tam):  # resta el minimo de cada fila con toda la fila
        fila = [int(f) - min_fil[i] for f in matriz[i]]

        nueva_m.append(fila)

    return nueva_m

""" realiza todas las asignaciones posibles """
def paso3(matriz, meta):
    tam = len(matriz)
    exito = False

    for i in range(tam):  # recorre toda la matriz
        for j in range(tam):
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
    
""" marca filas y columnas cuando no se encuentra una solución para la matriz en el paso 3 """
def paso4(matriz):
    tam = len(matriz)
    matriz, e = paso3(matriz, tam-1)  # obtiene una matriz con las asignaciones requeridas -1
    
    marca_a = []  # filas que no tienen asignaciones
    for i in range(tam):
        if matriz[i].count("x") == 0:
            marca_a.append(i)

    marca_b = []  # columnas con 0 en las filas de la marca a
    for i in range(tam):
        for j in range(len(marca_a)):
            if matriz[marca_a[j]][i] == 0:
                marca_b.append(i)
    
    marca_c = []  # filas con asignacion de las col de la marca b
    for i in range(tam):
        for j in range(len(marca_b)):
            if matriz[i][marca_b[j]] == "x":
                marca_c.append(i)

    # linea en las casillas de filas que no estan marcadas y columnas marcadas
    nueva_m = []
    for i in range(tam):
        fila = []
        for j in range(tam):
            if (i in marca_a or i in marca_c) and j not in marca_b:
                fila.append(matriz[i][j])
            
            else:
                fila.append("-")
        
        nueva_m.append(fila)

    return nueva_m, marca_b

""" resta el valor menor a las casillas sin '-' y lo suma a los demas """
def paso5(matriz_ref, matriz_ray, marca_b):  # se reciben dos matrices para comparar la matriz rayada con la original
    tam = len(matriz_ref)
    nueva_m = []

    val_min = []  # almacena todos los valores que no sean '-' ni 'x'

    for i in range(tam):  # obtiene el minimo excluyendo "-"
        for j in range(tam):
            if matriz_ray[i][j] != "-":
                val_min.append(matriz_ray[i][j])

    val_min = min(val_min)  # obtiene el valor minimo de la matriz

    for i in range(tam):
        fila = []
        for j in range(tam):  # llenado de la nueva matriz
            if matriz_ray[i][j] != "-":  # si la casilla de la matriza rayada es una '-'
                if matriz_ref[i][j] == "x":  # casillas asignadas = 0
                    fila.append(0)

                else:
                    fila.append(matriz_ref[i][j] - val_min)  # casillas no rayadas, val - val min


            else: 
                if matriz_ref[i][j] == "x":  # si la casilla en la matriz ref tiene una asignacion
                    fila.append(0)  # val = 0

                elif j in marca_b and matriz_ref[i][j] != 0:  # si la la columna tiene la marca b y la casilla no es cero en la matriz ref
                    fila.append(matriz_ref[i][j] + val_min)  # val - val min

                else:
                    fila.append(matriz_ref[i][j]) 
        
        nueva_m.append(fila)

    return nueva_m

