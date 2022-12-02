import sys

from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit, QMainWindow, QHBoxLayout, \
    QVBoxLayout, QListView
from ModeloListaTarefas import ModeloListaTarefas

class ListaTarefas (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo lista tarefas")

        self.modelo = ModeloListaTarefas ([(False, "Miña primeira tarefa")])
        self.lstTarefas = QListView()
        self.lstTarefas.setModel(self.modelo)

        caixaV = QVBoxLayout()

        caixaV.addWidget(self.lstTarefas)

        caixaH = QHBoxLayout()
        caixaV.addLayout(caixaH)
        self.btnBorrar = QPushButton("Borrar")
        self.btnBorrar.pressed.connect(self.on_btnBorrar_pressed)
        caixaH.addWidget(self.btnBorrar)
        self.btnFeito = QPushButton("Feito")
        self.btnFeito.pressed.connect(self.on_btnFeito_pressed)
        caixaH.addWidget(self.btnFeito)

        self.lneNovaTarefa = QLineEdit()
        self.lneNovaTarefa.returnPressed.connect(self.on_btnEngadirTarefa_pressed)
        self.lneNovaTarefa.setPlaceholderText("Escribe aquí o teu texto")
        caixaV.addWidget(self.lneNovaTarefa)

        self.btnEngadirTarefa = QPushButton("Enagdir tarefa")
        self.btnEngadirTarefa.pressed(self.on_btnEngadirTarefa_pressed)
        caixaV.addWidget(self.btnEngadirTarefa)

        contenedor = QWidget()
        contenedor.setLayout(caixaV)

        self.setCentralWidget(contenedor)

        self. show()

    def on_btnEngadirTarefa_pressed(self):
        novaTarefa = self.lneNovaTarefa.text()
        novaTarefa = novaTarefa.strip()

        if novaTarefa:
            self.modelo.listaTarefa.append(False, novaTarefa)
            self.modelo.layoutChanged.emit()
            self.lneNovaTarefa.setText("")

    def on_btnBorrar_pressed(self):
        indices = self.lstTarefas.selectedIndexes()
        if indices:
            indice = indices[0]
            del self.modelo.listaTarefa[indice.row()]
            #self.modelo.listaTarefa.remove(self.modelo.listaTarefa [indice.row()])
            self.modelo.layoutChanged.emit()
            self.lstTarefas.clearSelection()

    def on_btnFeito_pressed(self):
        indices = self.lstTarefas.selectedIndexes()
        if indices:
            indice = indices[0]
            fila = indice.row()
            estado, descripcionTarefa = self.modelo.listaTarefa[fila]
            self.modelo.listaTarefa[fila] = (True, descripcionTarefa)
            self.modelo.dataChanged.emit(indice, indice)
            self.lstTarefas.clearSelection()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ListaTarefas()
    aplicacion.exec()