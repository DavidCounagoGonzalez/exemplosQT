import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableView, QWidget, QPushButton, QHBoxLayout


class FiestraTable(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QTableView")

        bd = QSqlDatabase("QSQLITE")
        bd.setDatabaseName("bbdd.dat")
        bd.open()


        caixaV = QVBoxLayout()

        tlvTaboa = QTableView()
        self.modelo = QSqlTableModel(db=bd)
        #Método manual de actualización:
        self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        #Métodos de edición automáticos:
        #QSqlTableModel.EditStrategy.OnRowChange
        #QSqlTableModel.EditStrategy.OnFieldChange
        tlvTaboa.setModel(self.modelo)
        self.modelo.setTable("usuarios")
        self.modelo.setSort(0, Qt.SortOrder.DescendingOrder)
        self.modelo.select()
        self.modelo.setHeaderData(0, Qt.Orientation.Horizontal, "DNI")
        self.modelo.setHeaderData(1, Qt.Orientation.Horizontal, "Nome Usuario")
        self.modelo.setHeaderData(2, Qt.Orientation.Horizontal, "Dirección")
        #self.modelo.removeColumns(2,1)

        caixaV.addWidget(tlvTaboa)

        caixaH = QHBoxLayout()
        caixaV.addLayout(caixaH)
        btnActualizarBD = QPushButton("Actualizar")
        btnActualizarBD.clicked.connect(self.on_btnActualizarBD_clicked)
        caixaH.addWidget(btnActualizarBD)

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.clicked.connect(self.on_btnCancelar_clicked)
        caixaH.addWidget(btnCancelar)



        contedor = QWidget()
        contedor.setLayout(caixaV)

        self.setCentralWidget(contedor)
        self.setMinimumSize(500, 400)
        self.show()

    def on_btnActualizarBD_clicked(self):
        self.modelo.submitAll()

    def on_btnCancelar_clicked(self):
        self.modelo.revertAll()



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraTable()
    aplicacion.exec()