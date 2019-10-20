from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.MatchFinishDialog import Ui_match_finish_dialog
from src.model.firedb import firedb

class MatchFinish(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_match_finish_dialog()
        self.ui.setupUi(self)
