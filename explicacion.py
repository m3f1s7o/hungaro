#! /bin/python3
from tabulate import tabulate

def explicacion(matriz, matriz_c):
    sol = []
    titulos = ["Depósitos", "Localidad", "km"]

    for row in range(len(matriz_c)):
        col = matriz_c[row].index("x")

        row_s = [row+1, col+1, matriz[row][col]]
        sol.append(row_s)
        
    #print(tabulate(sol, titulos, tablefmt="psql"))
    #print(f"z = {}sum([x[2] for x in sol])")
    z = sum([x[2] for x in sol])

    return sol, z

