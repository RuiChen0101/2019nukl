from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, QtCore
from src.ui.NewMatchDialog import Ui_new_match_dialog
from src.model.MatchInfo import MatchInfo
from src.model.EnrollInfo import EnrollInfo

class NewMatch(QDialog):
    def __init__(self, matchInfo, enrollInfo, cat, round):
        super().__init__()
        self.ui = Ui_new_match_dialog()
        self.ui.setupUi(self)
        self.playerList=[]
        self.matchInfo=matchInfo
        self.enrollInfo=enrollInfo
        self.cat=cat
        self.round=round
        self.setUpUi()

    def setUpUi(self):
        self.ui.catgory.setText(self.cat)
        self.ui.round.setText(self.round)
        idList=self.enrollInfo.getIdListByCatRound(self.cat, self.round)
        table=self.ui.total_player_list
        for id in idList:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.enrollInfo.getName(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.enrollInfo.getCatogoryName(id)))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(self.enrollInfo.getRound(id)))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(id))
