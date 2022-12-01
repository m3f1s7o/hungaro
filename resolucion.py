#! /bin/python3
from tabulate import tabulate
from pasos import *
from explicacion import *

def main():
   # matriz = obtnrTabla()
    matriz = defTabla()

    print_t = lambda matriz_n: print(tabulate(matriz_n, headers=["C" + str(i) for i in range(len(matriz))], tablefmt="psql"))  # imprime la matriz en una tabla con formato


    # tabla original
    print_t(matriz)

    # tabla original - min c columna
    matriz_a = paso1(matriz)
    print("Paso 1")
    #print_t(matriz_a)

    # tabla - min c fila
    matriz_b = paso2(matriz_a)
    print("Paso 2")
    #print_t(matriz_b)

    # tabla asignaciones
    matriz_c, exito = paso3(matriz_b, len(matriz))
    print("Paso 3")
    #print_t(matriz_c)

    # termina con la solucion del problema o cuando se agoten los intentos
    intentos = 0
    while(not exito and intentos <= 10):
        if intentos != 0:
            print(f"\n\nIntento {intentos}")

        # tabla rayada
        matriz_d, col_m = paso4(matriz_c)
        print("Paso 4")
        #print_t(matriz_d)

        # menor de las no rayadas
        matriz_e = paso5(matriz_b, matriz_d, col_m)
        print("Paso 5")
        #print_t(matriz_e)
       
        # asignaciones
        matriz_c, exito = paso3(matriz_e, len(matriz))
        print("Paso 3")
        #print_t(matriz_c)
        
        intentos += 1

    if exito:
        print("Solucion")
        print_t(matriz_c)
        explicacion(matriz, matriz_c)

    else:
        print("No se pudo dar solucion al problema")

def resolver(matriz):
    # tabla original - min c columna
    matriz_a = paso1(matriz)

    # tabla - min c fila
    matriz_b = paso2(matriz_a)

    # tabla asignaciones
    matriz_c, exito = paso3(matriz_b, len(matriz))

    # termina con la solucion del problema o cuando se agoten los intentos
    intentos = 0
    while(not exito and intentos <= 10):
        # tabla rayada
        matriz_d, col_m = paso4(matriz_c)

        # menor de las no rayadas
        matriz_e = paso5(matriz_b, matriz_d, col_m)
       
        # asignaciones
        matriz_c, exito = paso3(matriz_e, len(matriz))
        
        intentos += 1

    if exito:
        expli, z = explicacion(matriz, matriz_c)

        return matriz_c, expli, z

    else:
        #print("No se pudo dar solucion al problema")

        return matriz_c, None, None



if __name__ == "__main__":
    main()
