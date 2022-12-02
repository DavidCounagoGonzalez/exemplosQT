import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextFrame
from ExemploGridLayout2 import Calculadora
from ExemploQVBoxLayout import Color
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTabWidget


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exemplo QTabWidget')

        caixaV = QVBoxLayout()

        panelTab = QTabWidget()
        calc = Calculadora()
        panelColor = Color("red")
        panelTab.addTab(calc, "calculadora")
        panelTab.addTab(panelColor, "Vermello")


        self.setCentralWidget(panelTab)
        self.show()


if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()