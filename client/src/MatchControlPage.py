from PyQt5.QtWidgets import QMainWindow,QDialog,QMessageBox
from PyQt5 import QtWidgets, QtCore
from src.ui.mainwindow import Ui_MainWindow
from src.model.MatchInfo import MatchInfo
from src.model.EnrollInfo import EnrollInfo
from src.Arrangement import Arrangement
from src.MatchFinish import MatchFinish
from src.NewMatch import NewMatch
from src.SetReplay import SetReplay
from src.JudgeAssign import JudgeAssign

class MatchControlPage():
    def __init__(self, uiRef, matchInfoRef, enrollInfoRef, main):
        self.ui=uiRef
        self.main=main
        self.matchInfo=matchInfoRef
        self.enrollInfo=enrollInfoRef
        self.ui.new_match_btn.clicked.connect(self.onNewMatchClick)
        self.ui.set_arrangement_btn.clicked.connect(self.onSetArrangementClick)
        self.ui.match_finish_btn.clicked.connect(self.onMatchFinishClick)
        self.ui.delete_match_btn.clicked.connect(self.onDeleteMatchClick)
        self.ui.set_replay_btn.clicked.connect(self.onSetReplayClick)
        self.ui.judge_assign_btn.clicked.connect(self.onJudgeAssignClick)
        self.ui.catgory_list.currentIndexChanged.connect(self.onCatOrRoundChange)
        self.ui.round_list.currentIndexChanged.connect(self.onCatOrRoundChange)
        self.ui.match_list.itemSelectionChanged.connect(self.onMatchListSelectionChange)
        self.setUpUi()

    def setUpUi(self):
        self.ui.match_list.setRowCount(0)
        self.ui.player_list.setRowCount(0)
        self.ui.advance_player_list.setRowCount(0)
        self.ui.group.setText("")
        self.ui.catgory.setText("")
        self.ui.round.setText("")
        self.ui.status.setText("")
        self.ui.arranged_time.setText("")
        self.ui.delete_match_btn.setEnabled(False)
        self.ui.set_arrangement_btn.setEnabled(False)
        self.ui.match_finish_btn.setEnabled(False)
        self.ui.set_replay_btn.setEnabled(False)
        self.ui.judge_assign_btn.setEnabled(False)
        idList=self.matchInfo.getMatchList(self.ui.catgory_list.currentText(), self.ui.round_list.currentText())
        table=self.ui.match_list
        for id in idList:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(str(self.matchInfo.getGroup(id))))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.matchInfo.getCatogoryName(id)))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(self.matchInfo.getStatusName(id)))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(self.matchInfo.getJudge(id)))
            table.setItem(count, 4, QtWidgets.QTableWidgetItem(self.matchInfo.getTime(id)))
            table.setItem(count, 5, QtWidgets.QTableWidgetItem(id))

    def onCatOrRoundChange(self):
        self.ui.match_list.clearSelection()
        self.ui.player_list.setRowCount(0)
        self.ui.advance_player_list.setRowCount(0)
        self.setUpUi()

    def onMatchListSelectionChange(self):
        if self.ui.match_list.currentRow()==-1:
            return
        docId=self.ui.match_list.item(self.ui.match_list.currentRow(),5).text()
        self.ui.group.setText(str(self.matchInfo.getGroup(docId)))
        self.ui.catgory.setText(self.matchInfo.getCatogoryName(docId))
        self.ui.round.setText(self.matchInfo.getRound(docId))
        self.ui.status.setText(self.matchInfo.getStatusName(docId))
        self.ui.arranged_time.setText(self.matchInfo.getTime(docId))
        self.ui.delete_match_btn.setEnabled(True)
        self.ui.set_arrangement_btn.setEnabled(self.matchInfo.isArrangable(docId))
        self.ui.match_finish_btn.setEnabled(self.matchInfo.isFinishable(docId))
        self.ui.set_replay_btn.setEnabled(self.matchInfo.isReplaySetable(docId))
        self.ui.judge_assign_btn.setEnabled(self.matchInfo.isAssignable(docId))
        self.setUpPlayerList(docId)
        self.setUpAdvancedList(docId)

    def setUpPlayerList(self, docId):
        palyerId=self.matchInfo.getPlayerList(docId)
        table=self.ui.player_list
        table.setRowCount(0)
        for id in palyerId:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.matchInfo.getPlayerScore(docId,id)))

    def setUpAdvancedList(self, docId):
        palyerId=self.matchInfo.getAdvanceList(docId)
        table=self.ui.advance_player_list
        table.setRowCount(0)
        for id in palyerId:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.matchInfo.getPlayerScore(docId,id)))

    def onDeleteMatchClick(self):
        docId=self.ui.match_list.item(self.ui.match_list.currentRow(),5).text()
        reply = QMessageBox.information(self.main,'刪除','確認刪除?', QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.matchInfo.deleteMatch(docId)
            self.setUpUi()

    def onNewMatchClick(self):
        dialog=NewMatch(self.enrollInfo,self.ui.catgory_list.currentText(), self.ui.round_list.currentText())
        result=dialog.exec()
        if result==QDialog.Accepted:
            group, playerList=dialog.getResult()
            self.matchInfo.createNewMatch(self.ui.catgory_list.currentText(),self.ui.round_list.currentText(),group,playerList)
            self.setUpUi()

    def onSetArrangementClick(self):
        docId=self.ui.match_list.item(self.ui.match_list.currentRow(),5).text()
        dialog=Arrangement()
        result=dialog.exec()
        if result==QDialog.Accepted:
            dateTime=dialog.getResult()
            self.matchInfo.setArrangement(docId, dateTime)
            self.setUpUi()

    def onJudgeAssignClick(self):
        docId=self.ui.match_list.item(self.ui.match_list.currentRow(),5).text()
        dialog=JudgeAssign()
        result=dialog.exec()
        if result==QDialog.Accepted:
            judge=dialog.getResult()
            self.matchInfo.setJudge(docId,judge)
            self.setUpUi()

    def onSetReplayClick(self):
        docId=self.ui.match_list.item(self.ui.match_list.currentRow(),5).text()
        dialog=SetReplay()
        result=dialog.exec()
        if result==QDialog.Accepted:
            url=dialog.getResult()
            self.matchInfo.setReplay(docId,url)
            self.setUpUi()

    def onMatchFinishClick(self):
        docId=self.ui.match_list.item(self.ui.match_list.currentRow(),5).text()
        dialog=MatchFinish(self.enrollInfo, self.matchInfo.getPlayerList(docId), self.matchInfo.getCatogoryName(docId))
        result=dialog.exec()
        if result==QDialog.Accepted:
            scoreList, advanceList=dialog.getResult()
            self.matchInfo.setFinish(docId, scoreList, advanceList)
            self.setUpUi()
