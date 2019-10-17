import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, QtCore
from ui.mainwindow import Ui_MainWindow
from src.firedb import firedb

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.check_btn.clicked.connect(self.onCheckClick)
        self.ui.cancel_btn.clicked.connect(self.onCancelClick)
        self.ui.delete_btn.clicked.connect(self.onDeleteClick)
        self.ui.refresh_btn.clicked.connect(self.onRefreshClick)
        self.ui.relife_btn.clicked.connect(self.onRelifeClick)
        self.db=firedb()
        self.idList=self.db.getIdList()
        self.tableViews={'false':self.ui.uncheck_list,'true':self.ui.checked_list,'delete':self.ui.deleted_list}
        self.show()
        self.setUpUi()

    def setUpUi(self):
        self.ui.uncheck_list.setRowCount(0)
        self.ui.checked_list.setRowCount(0)
        self.ui.deleted_list.setRowCount(0)
        for id in self.idList:
            table=self.tableViews[self.db.getStstus(id)]
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(self.db.getTimeInterval(id)))
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(self.db.getName(id)))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(self.db.getCatogory(id)))
            table.setItem(count, 3, QtWidgets.QTableWidgetItem(self.db.getSchool(id)))
            table.setItem(count, 4, QtWidgets.QTableWidgetItem(id))
        self.ui.uncheck_list.sortItems(2, QtCore.Qt.AscendingOrder)
        self.ui.checked_list.sortItems(2, QtCore.Qt.AscendingOrder)
        self.ui.deleted_list.sortItems(2, QtCore.Qt.AscendingOrder)

    def onCheckClick(self):
        pos=self.ui.uncheck_list.currentRow()
        self.db.handelCheck(self.ui.uncheck_list.item(pos,4).text())
        self.setUpUi()

    def onCancelClick(self):
        pos=self.ui.checked_list.currentRow()
        self.db.handelCancel(self.ui.checked_list.item(pos,4).text())
        self.setUpUi()

    def onDeleteClick(self):
        pos=self.ui.uncheck_list.currentRow()
        self.db.handelDelete(self.ui.uncheck_list.item(pos,4).text())
        self.setUpUi()

    def onRelifeClick(self):
        pos=self.ui.deleted_list.currentRow()
        self.db.handelCancel(self.ui.deleted_list.item(pos,4).text())
        self.setUpUi()

    def onRefreshClick(self):
        self.db.handelRefresh()
        self.setUpUi()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
