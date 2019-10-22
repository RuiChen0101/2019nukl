from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.MatchFinishDialog import Ui_match_finish_dialog
from src.model.EnrollInfo import EnrollInfo
from src.model.firedb import firedb

class MatchFinish(QDialog):
    def __init__(self, enrollInfo, playerList, cat):
        super().__init__()
        self.ui = Ui_match_finish_dialog()
        self.ui.setupUi(self)
        self._playerList=playerList
        self._enrollInfo=enrollInfo
        self._advanceList=[]
        self._scoreList={}
        self._advanceListLimit= 1 if cat=="團體競速" else 4
        self.ui.ok_btn.clicked.connect(self.onOkClick)
        self.ui.cancel_btn.clicked.connect(self.onCancelClick)
        self.ui.add_btn.clicked.connect(self.onAddClick)
        self.ui.remove_btn.clicked.connect(self.onRemoveClick)
        self.setUpUi()

    def getResult(self):
        return self._scoreList, self._advanceList

    def setUpUi(self):
        table=self.ui.player_list
        table.setRowCount(0)
        for id in self._playerList:
            self._scoreList[id]=0
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self._enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem("0"))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(id))
        self.ui.player_list.cellChanged.connect(self.onCellChange)

    def updatePlayerList(self):
        self.ui.player_list.cellChanged.disconnect(self.onCellChange)
        table=self.ui.advance_player_list
        table.setRowCount(0)
        for id in self._advanceList:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self._enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(str(self._scoreList[id])))
        table=self.ui.player_list
        table.setRowCount(0)
        for id in self._playerList:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self._enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(str(self._scoreList[id])))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(id))
        self.ui.player_list.cellChanged.connect(self.onCellChange)

    def onCellChange(self):
        for i in range(self.ui.player_list.rowCount()):
            self._scoreList[self.ui.player_list.item(i,2).text()]=int(self.ui.player_list.item(i,1).text())
        self.updatePlayerList()

    def onOkClick(self):
        self.accept()

    def onCancelClick(self):
        self.reject()

    def onAddClick(self):
        playerId=self.ui.player_list.item(self.ui.player_list.currentRow(), 2).text()
        if playerId not in self._advanceList and len(self._advanceList)<self._advanceListLimit:
            self._advanceList.append(playerId)
            self.updatePlayerList()

    def onRemoveClick(self):
        self._advanceList.pop(self.ui.advance_player_list.currentRow())
        self.updatePlayerList()
