from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.SetReplayDialog import Ui_set_replay_dialog

class SetReplay(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_set_replay_dialog()
        self.ui.setupUi(self)
        self._url=0
        self.ui.ok_btn.clicked.connect(self.onOkClick)
        self.ui.cancel_btn.clicked.connect(self.onCancelClick)

    def getResult(self):
        return self._url

    def onOkClick(self):
        self._url=self.ui.url.text()
        if self._url!="":
            self.accept()

    def onCancelClick(self):
        self.reject()
