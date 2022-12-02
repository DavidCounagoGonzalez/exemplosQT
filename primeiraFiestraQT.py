import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A miña primeira fiestra con PyQt6")

        self.pulsado = 0
        self.caracteres = 0
        self.cadroTexto = QLineEdit()
        self.cadroTexto.setMaxLength(10)
        self.cadroTexto.setPlaceholderText("Escribe o teu nome")

        self.cadroTexto.returnPressed.connect(self.on_boton_clicked)
        self.cadroTexto.selectionChanged(self.on_cadroTexto_selectionChanged)
        #self.cadroTexto.textChanged(self.on_cadroTexto_textChanged)
        self.cadroTexto.textChanged(self.on_cadroTexto_textEdited)
        #self.cadroTexto.keyPressEvent(self.on_cadroTexto_keyPressEvent)


        boton = QPushButton("Saúdo")
        boton.clicked.connect (self.on_boton_clicked)
        self.etiqueta = QLabel("")

        caixaV = QVBoxLayout()
        caixaV.addWidget(self.cadroTexto)
        caixaV.addWidget(boton)
        caixaV.addWidget(self.etiqueta)

        contenedor = QWidget()
        contenedor.setLayout(caixaV)

        self.setCentralWidget(contenedor)
        self.show()

    def on_boton_clicked (self):
        #print("O botón foi pulsado")
        if self.pulsado>0:
            self.etiqueta.setText("Ola! "+self.cadroTexto.text() + " O botón foi pulsado: " + str(self.pulsado) + " veces.")
        else:
            self.etiqueta.setText("Ola " + self.cadroTexto.text())
            #self.cadroTexto.setReadOnly(True)
            self.caracteres = 0
            self.cadroTexto.setText("")
        self.pulsado = self.pulsado + 1

    def on_cadroTexto_textEdited(self):
        self.caracteres += 1
        print("Pulsaronse " + self.caracteres + " caracteres")

    def on_cadroTexto_selectionChanged(self):
        print("Texto seleccionado: " + self.cadroTexto.selectedText())

if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()