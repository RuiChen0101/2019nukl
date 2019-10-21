from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.NewMatchDialog import Ui_new_match_dialog
from src.model.MatchInfo import MatchInfo
from src.model.EnrollInfo import EnrollInfo

class NewMatch(QDialog):
    def __init__(self, enrollInfo, cat, round):
        super().__init__()
        self.ui = Ui_new_match_dialog()
        self.ui.setupUi(self)
        self._playerList=[]
        self._group=""
        self.enrollInfo=enrollInfo
        self.cat=cat
        self.round=round
        self.plyerListLimit= 2 if cat=="團體競速" else 8
        self.ui.ok_btn.clicked.connect(self.onOkClick)
        self.ui.cancel_btn.clicked.connect(self.onCancelClick)
        self.ui.add_btn.clicked.connect(self.onAddClick)
        self.ui.remove_btn.clicked.connect(self.onRemoveClick)
        self.setUpUi()

    def setUpUi(self):
        self.ui.catgory.setText(self.cat)
        self.ui.round.setText(self.round)
        idList=self.enrollInfo.getIdListByCatRound(self.cat, self.round)
        table=self.ui.total_player_list
        table.setRowCount(0)
        for id in idList:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.enrollInfo.getCatogoryName(id)))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(self.enrollInfo.getRound(id)))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(id))

    def updatePlayerList(self):
        table=self.ui.player_list
        table.setRowCount(0)
        for id in self._playerList:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.enrollInfo.getCatogoryName(id)))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(self.enrollInfo.getRound(id)))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(id))

    def getResult(self):
        return self._group, self._playerList

    def onOkClick(self):
        self._group=self.ui.group.text()
        if self._group!="":
            self.accept()

    def onCancelClick(self):
        self.reject()

    def onAddClick(self):
        playerId=self.ui.total_player_list.item(self.ui.total_player_list.currentRow(),3).text()
        if playerId not in self._playerList and len(self._playerList)<self.plyerListLimit:
            self._playerList.append(playerId)
            self.updatePlayerList()

    def onRemoveClick(self):
        self._playerList.pop(self.ui.player_list.currentRow())
        self.updatePlayerList()
