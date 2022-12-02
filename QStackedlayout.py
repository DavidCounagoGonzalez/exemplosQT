import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow, QHBoxLayout, QStackedLayout, QPushButton

from VentanaColor import Color

class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo QStackedLayout")

        caixaV = QVBoxLayout()
        caixaH = QHBoxLayout()
        btnRojo = QPushButton("Rojo")
        btnRojo.pressed.connect(self.activa_tarxeta_1)
        caixaH.addWidget(btnRojo)

        btnVerde = QPushButton("verde")
        btnVerde.pressed.connect(self.activa_tarxeta_2)
        caixaH.addWidget(btnVerde)

        btnAzul = QPushButton("Azul")
        btnAzul.pressed.connect(self.activa_tarxeta_3)
        caixaH.addWidget(btnAzul)

        self.esquema = QStackedLayout()

        caixaH.addWidget(btnRojo)
        caixaV.addLayout(caixaH)
        caixaV.addLayout(self.esquema)

        self.esquema.addWidget(Color ("red"))
        self.esquema.addWidget(Color ("green"))
        self.esquema.addWidget(Color ("blue"))
        self.esquema.addWidget(Color ("purple"))

        self.esquema.setCurrentIndex(3)

        widget = QWidget()
        widget.setLayout(caixaV)
        self.setCentralWidget(widget)

        self.show()

        def activa_tarxeta_1(self):
            self.esquema.setCurrentIndex(0)

        def activa_tarxeta_2(self):
            self.esquema.setCurrentIndex(1)

        def activa_tarxeta_3(self):
            self.esquema.setCurrentIndex(2)

if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()
