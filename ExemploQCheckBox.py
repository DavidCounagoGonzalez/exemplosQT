import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QCheckBox


class FiestraCheckBox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A miña fiestra checkbox")

        caixaV = QVBoxLayout()

        self.chkHome = QCheckBox("Home")
        self.chkHome.setCheckState(Qt.CheckState.Checked)
        self.chkHome.clicked.connect(self.on_chkHome_stateChanged)

        self.chkMuller = QCheckBox("Muller")
        self.chkMuller.clicked.connect(self.on_chkMuller_StateChanged)

