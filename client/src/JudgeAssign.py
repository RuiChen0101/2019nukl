from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.JudgeAssignDialog import Ui_judge_assign_dialog

class JudgeAssign(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_judge_assign_dialog()
        self.ui.setupUi(self)
        self._judge=0
        self.ui.ok_btn.clicked.connect(self.onOkClick)
        self.ui.cancel_btn.clicked.connect(self.onCancelClick)

    def getResult(self):
        return self._judge

    def onOkClick(self):
        self._judge=self.ui.judge.text()
        if self._judge!="":
            self.accept()

    def onCancelClick(self):
        self.reject()
