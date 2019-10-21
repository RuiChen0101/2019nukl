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
        self.ui.match_list.itemSelectionChanged.connect(self.onMatchListSelectionChange)
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
        self.ui.set_replay_btn.setEnabled(False)
        idList=self.matchInfo.getMatchList(self.ui.catgory_list.currentText(), self.ui.round_list.currentText())
        table=self.ui.match_list
        for id in idList:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.matchInfo.getGroup(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.matchInfo.getCatogoryName(id)))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(self.matchInfo.getStatusName(id)))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(id))

    def onCatOrRoundChange(self):
        self.ui.match_list.clearSelection()
        self.ui.player_list.setRowCount(0)
        self.ui.advance_player_list.setRowCount(0)
        self.setUpUi()

    def onMatchListSelectionChange(self):
        docId=self.ui.match_list.item(self.ui.match_list.currentRow(),3).text()
        self.ui.group.setText(self.matchInfo.getGroup(docId))
        self.ui.catgory.setText(self.matchInfo.getCatogoryName(docId))
        self.ui.round.setText(self.matchInfo.getRound(docId))
        self.ui.status.setText(self.matchInfo.getStatusName(docId))
        self.ui.arranged_time.setText(self.matchInfo.getTime(docId))
        self.ui.delete_match_btn.setEnabled(True)
        self.ui.set_arrangement_btn.setEnabled(self.matchInfo.isArrangable(docId))
        self.ui.match_finish_btn.setEnabled(self.matchInfo.isFinishable(docId))
        self.ui.set_replay_btn.setEnabled(self.matchInfo.isReplaySetable(docId))
        self.setUpPlayerList(docId)
        self.setUpAdvancedList(docId)

    def setUpPlayerList(self, docId):
        palyerId=self.matchInfo.getPlayerList(docId)
        table=self.ui.player_list
        for id in palyerId:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.matchInfo.getPlayerScore(docId,id)))

    def setUpAdvancedList(self, docId):
        palyerId=self.matchInfo.getAdvanceList(docId)
        table=self.ui.advance_player_list
        for id in palyerId:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.matchInfo.getPlayerScore(docId,id)))

    def onNewMatchClick(self):
        dialog=NewMatch(self.matchInfo,self.enrollInfo,self.ui.catgory_list.currentText(), self.ui.round_list.currentText())
        dialog.exec()

    def onSetArrangementClick(self):
        dialog=Arrangement()
        dialog.exec()

    def onMatchFinishClick(self):
        dialog=MatchFinish()
        dialog.exec()
