import sys

from PyQt6.QtGui import QTextFrame
from PyQt6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit


class FiestraPrincipal (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exemplo QTGridLayout')
        grid = QGridLayout()

        grid.addWidget(QPushButton('1'), 0, 0)
        grid.addWidget(QPushButton('2'), 0, 1)
        grid.addWidget(QPushButton('3'), 0, 2)
        grid.addWidget(QPushButton('4'), 1, 0)
        grid.addWidget(QPushButton('5'), 1, 1)
        grid.addWidget(QPushButton('6'), 1, 2)
        grid.addWidget(QPushButton('7'), 2, 0)
        grid.addWidget(QPushButton('8'), 2, 1)
        grid.addWidget(QPushButton('9'), 2, 2)
        grid.setContentsMargins(0,0,0,10)

        contenedorGrid = QWidget()
        contenedorGrid.setLayout(grid)

        caixaV = QVBoxLayout()
        caixaV.addWidget(QLineEdit())
        caixaV.addWidget(contenedorGrid)
        caixaV.addWidget(QPushButton('0'))

        contenedor = QWidget()
        contenedor.setLayout(caixaV)

        oper = QGridLayout()
        oper.addWidget(QPushButton('+'), 0, 0)
        oper.addWidget(QPushButton('-'), 1, 0)
        oper.addWidget(QPushButton('X'), 2, 0)
        oper.addWidget(QPushButton('/'), 3, 0)
        oper.addWidget(QPushButton('='), 4, 0)

        cont = QWidget()
        cont.setLayout(oper)

        caixaH = QHBoxLayout()
        caixaH.addWidget(contenedor)
        caixaH.addWidget(cont)

        self.setLayout(caixaH)
        self.move(300, 150)
        self.show()

if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()
