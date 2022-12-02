import sys

from PyQt6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget, QLineEdit, QMainWindow


class Calculadora (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exemplo QTGridLayout')
        grid = QGridLayout()
        grid.addWidget(QLineEdit(), 0, 0, 1, 3)
        grid.addWidget(QPushButton('1'), 1, 0)
        grid.addWidget(QPushButton('2'), 1, 1)
        grid.addWidget(QPushButton('3'), 1, 2)
        grid.addWidget(QPushButton('4'), 2, 0)
        grid.addWidget(QPushButton('5'), 2, 1)
        grid.addWidget(QPushButton('6'), 2, 2)
        grid.addWidget(QPushButton('7'), 3, 0)
        grid.addWidget(QPushButton('8'), 3, 1)
        grid.addWidget(QPushButton('9'), 3, 2)
        grid.addWidget(QPushButton('0'), 4, 0, 1, 3)

        grid.addWidget(QPushButton('+'), 0, 3)
        grid.addWidget(QPushButton('-'), 1, 3)
        grid.addWidget(QPushButton('X'), 2, 3)
        grid.addWidget(QPushButton('/'), 3, 3)
        grid.addWidget(QPushButton('='), 4, 3)

        contedor = QWidget()
        contedor.setLayout(grid)
        self.setCentralWidget(contedor)

        self.show()

if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    fiestra = Calculadora()
    aplicacion.exec()