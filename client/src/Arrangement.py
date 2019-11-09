from pytz import timezone
from datetime import datetime
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.ArrangementDialog import Ui_arrangement_dialog

class Arrangement(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_arrangement_dialog()
        self.ui.setupUi(self)
        self.dateTime=0
        self.ui.date.showToday()
        self.ui.ok_btn.clicked.connect(self.onOkClick)
        self.ui.cancel_btn.clicked.connect(self.onCancelClick)

    def getResult(self):
        return self.dateTime

    def onOkClick(self):
        date=self.ui.date.selectedDate().toPyDate()
        time=self.ui.time.time().toPyTime()
        self.dateTime=datetime.combine(date,time, tzinfo=timezone('Etc/GMT-8'))
        self.accept()

    def onCancelClick(self):
        self.reject()
