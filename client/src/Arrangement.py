from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.ArrangementDialog import Ui_arrangement_dialog
from src.model.firedb import firedb

class Arrangement(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_arrangement_dialog()
        self.ui.setupUi(self)
