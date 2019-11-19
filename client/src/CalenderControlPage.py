from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog
from src.model.firedb import firedb
from src.ui.mainwindow import Ui_MainWindow
from src.model.MatchInfo import MatchInfo
from src.model.EnrollInfo import EnrollInfo
from src.JudgeAssign import JudgeAssign

class CalenderControlPage():
    def __init__(self, uiRef, matchInfoRef, enrollInfoRef):
        self.ui=uiRef
        self.matchInfo=matchInfoRef
        self.enrollInfo=enrollInfoRef
        self.date=self.ui.calender.selectedDate().toPyDate()
        self.ui.calender.selectionChanged.connect(self.onCalenderDateChange)
        self.ui.match_view_list.itemSelectionChanged.connect(self.onMatchViewListSelectionChange)
        self.ui.judge_assign_view_btn.clicked.connect(self.onJudgeAssignClick)
        self.setUpUi()

    def setUpUi(self):
        idList=self.matchInfo.getMatchByDateList(self.date)
        table=self.ui.match_view_list
        table.setRowCount(0)
        self.ui.player_view_list.setRowCount(0)
        colorRef={"已建立":QtGui.QColor(255,51,51),"已約戰":QtGui.QColor(137,137,255),"已完成":QtGui.QColor(100,255,100)}
        for id in idList:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(str(self.matchInfo.getGroup(id))))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.matchInfo.getCatogoryName(id)))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(self.matchInfo.getStatusName(id)))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(self.matchInfo.getJudge(id)))
            table.setItem(count, 4, QtWidgets.QTableWidgetItem(self.matchInfo.getTime(id)))
            table.setItem(count, 5, QtWidgets.QTableWidgetItem(id))
            table.item(count, 2).setBackground(colorRef[self.matchInfo.getStatusName(id)])
        table.sortItems(4)

    def onMatchViewListSelectionChange(self):
        if self.ui.match_view_list.currentRow()==-1:
            return
        docId=self.ui.match_view_list.item(self.ui.match_view_list.currentRow(),5).text()
        self.setUpPlayerList(docId)

    def onJudgeAssignClick(self):
        docId=self.ui.match_view_list.item(self.ui.match_view_list.currentRow(),5).text()
        dialog=JudgeAssign()
        result=dialog.exec()
        if result==QDialog.Accepted:
            judge=dialog.getResult()
            self.matchInfo.setJudge(docId,judge)
            self.setUpUi()

    def setUpPlayerList(self, docId):
        palyerId=self.matchInfo.getPlayerList(docId)
        table=self.ui.player_view_list
        table.setRowCount(0)
        for id in palyerId:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.matchInfo.getPlayerScore(docId,id)))

    def onCalenderDateChange(self):
        self.date=self.ui.calender.selectedDate().toPyDate()
        self.setUpUi()
