import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableView, QWidget

class ModeloTaboa (Qt.QAbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self._datos = datos

    def data (self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            return self._datos[indice.row()][indice.column()]

    def rowCount(self, indice):
        return len(self._datos)

    def columnCount(self, indice ):
        return len (self._datos[0])

class FiestraTable (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QTableView")

        caixaV = QVBoxLayout()

        tlvTaboa = QTableView()
        caixaV.addWidget(tlvTaboa)

        contidoTaboa = [["Luns", "martes", "mércores", "Xoves", "venres", "Sábado", "Domingo"],
                        [3, 5, 6, 8, 3, 9, 0],
                        [3, 2, 5, 7, 2, 3, 0]
                        ]


        contedor = QWidget()
        contedor.setLayout(caixaV)

        self.setLayoutWidget(contedor)

        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ModeloTaboa()
    aplicacion.exec()