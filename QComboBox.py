import sys

from PyQt6.QtWidgets import QVBoxLayout, QMainWindow, QWidget, QComboBox, QApplication


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exemplo QTComboBox')
        caixaV = QVBoxLayout()
        lista = []

        self.cadroTexto = QVBoxLayout()


        self.combo = QComboBox()
        self.combo.addItems()
        self

        lista.addItems(["ocupado", "parado","pensionista"])
        lista.currentItemChanged.connect (self.on_lista_currentItemChanged)
        lista.currentTextChanged.connect (self.on_lista_currentTextChanged)
        caixaV.addWidget(lista)

        contedor = QWidget()
        contedor.setLayout(caixaV)

        self.setCentralWidget(contedor)

        self.show()

    def on_combo_currentIndexChanged(self, indice):
        print(indice)
        print(self.combo.itemText(indice))

    def on_combo_curentTextChanged(self, texto):
        print(texto)

    def on_lista_currentItemChanged(self, elemento):
        print(elemento.text)

    def on_lista_currentTextChanged(self, texto):
        print(texto)

    def on_cadroTexto_returnPresed(self):
        self.lista.addItem(self.cadroTexto.text())
        self.CadroTexto.setText("")

if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()