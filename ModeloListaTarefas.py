
from PyQt6.QtCore import QAbstractListModel, Qt
from PyQt6.QtGui import QImage

tick = QImage ("tick.png")

class ModeloListaTarefas (QAbstractListModel):
    def __init__(self, listaTarefas=None):
        super().__init__()
        self.listaTarefa = listaTarefas or []

    def data (self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            estado, texto = self.listaTarefa [indice.row()]
            return  texto
        if rol == Qt.ItemDataRole.DecorationRole:
            estado, texto = self.listaTarefa[indice.row()]
            if estado:
                return tick

    def rowCount(self, index):
        return len (self.listaTarefa)