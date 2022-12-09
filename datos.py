""" obtiene los datos por teclado """
def obtnrTabla():
    dim = int(input("Dimensiones de la tabla(NxN) N: "));

    matriz = []
    tmp = []
    
    for i in range(dim):
        row = input(f"Valores de la fila {i} (1,2,..,n): ")
        
        # separa los numeros de cada fila y los pone en una lista como enteros
        matriz.append([int(x) for x in row.split(",")])

    return matriz

""" datos precargados """
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

