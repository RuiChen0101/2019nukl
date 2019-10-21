from PyQt5 import QtWidgets, QtCore
from src.model.firedb import firedb
from src.ui.mainwindow import Ui_MainWindow
from src.model.EnrollInfo import EnrollInfo


class EnrollCheckPage():
    def __init__(self, uiRef, enrollInfoRef):
        self.ui=uiRef
        self.enrollInfo=enrollInfoRef
        self.ui.check_btn.clicked.connect(self.onCheckClick)
        self.ui.cancel_btn.clicked.connect(self.onCancelClick)
        self.ui.delete_btn.clicked.connect(self.onDeleteClick)
        self.ui.refresh_btn.clicked.connect(self.onRefreshClick)
        self.ui.relife_btn.clicked.connect(self.onRelifeClick)
        self.idList=self.enrollInfo.getIdList()
        self.tableViews={'false':self.ui.uncheck_list,'true':self.ui.checked_list,'delete':self.ui.deleted_list}
        self.setUpUi()

    def setUpUi(self):
        self.ui.uncheck_list.setRowCount(0)
        self.ui.checked_list.setRowCount(0)
        self.ui.deleted_list.setRowCount(0)
        for id in self.idList:
            table=self.tableViews[self.enrollInfo.getStstus(id)]
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.enrollInfo.getTimeInterval(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.enrollInfo.getName(id)))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(self.enrollInfo.getCatogoryName(id)))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(self.enrollInfo.getSchool(id)))
            table.setItem(count, 4, QtWidgets.QTableWidgetItem(id))
        self.ui.uncheck_list.sortItems(2, QtCore.Qt.AscendingOrder)
        self.ui.checked_list.sortItems(2, QtCore.Qt.AscendingOrder)
        self.ui.deleted_list.sortItems(2, QtCore.Qt.AscendingOrder)

    def onCheckClick(self):
        pos=self.ui.uncheck_list.currentRow()
        self.enrollInfo.setStstus(self.ui.uncheck_list.item(pos,4).text(),"true")
        self.setUpUi()

    def onCancelClick(self):
        pos=self.ui.checked_list.currentRow()
        self.enrollInfo.setStstus(self.ui.checked_list.item(pos,4).text(),"false")
        self.setUpUi()

    def onDeleteClick(self):
        pos=self.ui.uncheck_list.currentRow()
        self.enrollInfo.setStstus(self.ui.uncheck_list.item(pos,4).text(),"delete")
        self.setUpUi()

    def onRelifeClick(self):
        pos=self.ui.deleted_list.currentRow()
        self.enrollInfo.setStstus(self.ui.deleted_list.item(pos,4).text(),"false")
        self.setUpUi()

    def onRefreshClick(self):
        self.enrollInfo.refresh()
        self.setUpUi()
