from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtCore
from src.ui.mainwindow import Ui_MainWindow
from src.model.MatchInfo import MatchInfo
from src.model.EnrollInfo import EnrollInfo
from src.Arrangement import Arrangement
from src.MatchFinish import MatchFinish
from src.NewMatch import NewMatch

class MatchControlPage():
    def __init__(self, uiRef, dbRef):
        self.ui=uiRef
        self.db=dbRef
        self.matchInfo=MatchInfo(dbRef)
        self.enrollInfo=EnrollInfo(dbRef)
        self.ui.new_match_btn.clicked.connect(self.onNewMatchClick)
        self.ui.set_arrangement_btn.clicked.connect(self.onSetArrangementClick)
        self.ui.match_finish_btn.clicked.connect(self.onMatchFinishClick)
        self.ui.catgory_list.currentIndexChanged.connect(self.onCatOrRoundChange)
        self.ui.round_list.currentIndexChanged.connect(self.onCatOrRoundChange)
        self.setUpUi()

    def setUpUi(self):
        self.ui.match_list.setRowCount(0)
        self.ui.group.setText("")
        self.ui.catgory.setText("")
        self.ui.round.setText("")
        self.ui.status.setText("")
        self.ui.arranged_time.setText("")
        self.ui.delete_match_btn.setEnabled(False)
        self.ui.set_arrangement_btn.setEnabled(False)
        self.ui.match_finish_btn.setEnabled(False)
        idList=self.matchInfo.getMatchList(self.ui.catgory_list.currentText(), self.ui.round_list.currentText())
        for id in idList:
            table=self.ui.match_list
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.matchInfo.getGroup(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.matchInfo.getCatogory(id)))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(self.matchInfo.getStatus(id)))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(id))

    def onCatOrRoundChange(self):
        self.setUpUi()

    def onNewMatchClick(self):
        dialog=NewMatch()
        dialog.exec()

    def onSetArrangementClick(self):
        dialog=Arrangement()
        dialog.exec()

    def onMatchFinishClick(self):
        dialog=MatchFinish()
        dialog.exec()
