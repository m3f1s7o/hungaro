#! /bin/python3
from tabulate import tabulate
from pasos import *
from explicacion import *
from datos import *

""" funcion de testeo para resolver por terminal """
def main():
    tabla = obtnrTabla()
    #tabla = defTabla()

    print_t = lambda tabla_n: print(tabulate(tabla_n, headers=["C" + str(i) for i in range(len(tabla))], tablefmt="psql"))  # imprime la tabla en una tabla con formato


    # tabla original
    print_t(tabla)

    # tabla original - min c columna
    tabla1 = paso1(tabla)
    print("Paso 1")
    print_t(tabla1)

    # tabla - min c fila
    tabla2 = paso2(tabla1)
    print("Paso 2")
    print_t(tabla2)

    # tabla asignaciones
    tabla3, exito = paso3(tabla2, len(tabla))
    print("Paso 3")
    print_t(tabla3)

    # termina con la solucion del problema o cuando se agoten los intentos
    intentos = 0
    while(not exito and intentos <= 10):
        if intentos != 0:
            print(f"\n\nIntento {intentos}")

        # tabla rayada
        tabla4, col_m = paso4(tabla3)
        print("Paso 4")
        print_t(tabla4)

        # menor de las no rayadas
        tabla5 = paso5(tabla2, tabla4, col_m)
        print("Paso 5")
        print_t(tabla5)
       
        # asignaciones
        tabla3, exito = paso3(tabla5, len(tabla))
        print("Paso 3")
        print_t(tabla3)
        
        intentos += 1

    if exito:
        print("Solucion")
        print_t(tabla3)
        explicacion(tabla, tabla3)

    else:
        print("No se pudo dar solucion al problema")


""" funcion para resolver con gui """
def resolver(tabla):
    # tabla original - min c columna
    tabla1 = paso1(tabla)

    # tabla - min c fila
    tabla2 = paso2(tabla1)

    # tabla asignaciones
    tabla3, exito = paso3(tabla2, len(tabla))

    # termina con la solucion del problema o cuando se agoten los intentos
    intentos = 0
    while(not exito and intentos <= 10):
        # tabla rayada
        tabla4, col_m = paso4(tabla3)

        # menor de las no rayadas
        tabla5 = paso5(tabla2, tabla4, col_m)
       
        # asignaciones
        tabla3, exito = paso3(tabla5, len(tabla))
        
        intentos += 1

    if exito:
        expli, z = explicacion(tabla, tabla3)

        return tabla3, expli, z

    else:
        #print("No se pudo dar solucion al problema")

        return tabla3, None, None



if __name__ == "__main__":
    main()
