import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextFrame
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, \
    QCheckBox, QGroupBox, QGridLayout, QComboBox, QTabWidget, QSlider


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exemplo QTGridLayout')

        caixaP = QVBoxLayout()
        caixaH1 = QHBoxLayout()
        boton = QPushButton("Botón")
        caixaH1.addWidget(boton)
        checkBox = QCheckBox("Selecciona")
        caixaH1.addWidget(checkBox)
        caixaP.addLayout(caixaH1)

        caixaH2 = QHBoxLayout()
        caixaP.addLayout(caixaH2)
        caixaV1 = QVBoxLayout()
        caixaH2.addLayout(caixaV1)
        grid = QGridLayout()
        contedor = QWidget()
        contedor.setLayout(grid)
        caixaG = QGroupBox("QGroupBox", contedor)
        caixaV1.addWidget(caixaG)

        cadroTexto1 = QLineEdit()
        caixaV1.addWidget(cadroTexto1)
        cadroTexto2 = QLineEdit()
        caixaV1.addWidget(cadroTexto2)
        combo = QComboBox()
        caixaV1.addWidget(combo)

        caixaV2 = QVBoxLayout()
        caixaH1.addLayout(caixaV2)
        grid = QGridLayout()
        casiña1 = QCheckBox("Opción 1")
        casiña2 = QCheckBox("Opción 2")
        casiña3 = QCheckBox("Opción 3")
        deslizador = QSlider(Qt.Orientation.Horizontal)
        grid.addWidget(casiña1 , 0, 0)
        grid.addWidget(casiña2, 1, 0)
        grid.addWidget(casiña3, 2, 0)
        grid.addWidget(deslizador, 5, 0, 1, 2)
        contedor1 = QWidget()
        contedor1.setLayout(grid)
        tab = QTabWidget()
        tab.addTab(contedor1, "Primeira solapa")
        caixaV2.addWidget(tab)


        contenedor = QWidget()
        contenedor.setLayout(caixaP)
        self.setCentralWidget(contenedor)
        self.show()


if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()