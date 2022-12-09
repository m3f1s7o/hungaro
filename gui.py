import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from resolucion import resolver

class hungaroGui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("hungaro.ui", self)

        # botones
        self.botonResolver.setEnabled(True)
        self.botonResolver.clicked.connect(self.resolverHungaro)
        self.botonCrear.clicked.connect(self.crearTabla)
        

    def crearTabla(self):
        # establece las filas y columnas de la tablas
        tam = int(self.spinMatriz.text())

        self.tablaOriginal.setRowCount(tam)
        self.tablaOriginal.setColumnCount(tam)
        # asigna nombres dinamicamente
        self.tablaOriginal.setHorizontalHeaderLabels(["C" + str(x+1) for x in range(tam)])
        self.tablaOriginal.setVerticalHeaderLabels(["F" + str(x+1) for x in range(tam)])

        self.tablaSolucion.setRowCount(tam)
        self.tablaSolucion.setColumnCount(tam)
        self.tablaSolucion.setHorizontalHeaderLabels(["C" + str(x+1) for x in range(tam)])
        self.tablaSolucion.setVerticalHeaderLabels(["F" + str(x+1) for x in range(tam)])
        
        self.tablaExplicacion.setRowCount(tam)
        self.tablaExplicacion.setVerticalHeaderLabels(["F" + str(x+1) for x in range(tam)])

        # establece los encabezados de las columnas para la explicacion
        self.tablaExplicacion.setHorizontalHeaderLabels([self.fieldEjeY.text(), self.fieldEjeX.text(), self.fieldMedida.text()])
        
    def resolverHungaro(self):
        tam = self.tablaOriginal.columnCount()
        matriz = []
        row = []

        # obtiene la matriz original
        for i in range(tam):
            for j in range(tam):
                v = int(self.tablaOriginal.item(i, j).text())
                row.append(v)

            matriz.append(row)
            row = []

        sol, expli, z = resolver(matriz)

        # llena la matriz de solucion
        for i in range(tam):
            for j in range(tam):
                self.tablaSolucion.setItem(i, j, QTableWidgetItem(str(sol[i][j])))

        for i in range(tam):
            for j in range(3):
                self.tablaExplicacion.setItem(i, j, QTableWidgetItem(str(expli[i][j])))

        self.fieldZ.setText(str(z))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = hungaroGui()
    
    gui.show()
    sys.exit(app.exec_())
