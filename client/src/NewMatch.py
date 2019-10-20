from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.NewMatchDialog import Ui_new_match_dialog
from src.model.firedb import firedb

class NewMatch(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_new_match_dialog()
        self.ui.setupUi(self)
