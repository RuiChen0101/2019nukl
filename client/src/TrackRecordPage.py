from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from src.ui.mainwindow import Ui_MainWindow
from src.model.TrackRecord import TrackRecord

class TrackRecordPage():
    def __init__(self, uiRef, trackRecordRef, main):
        self.ui=uiRef
        self.trackRecord=trackRecordRef
        self.main=main
        self.ui.track_record_update.clicked.connect(self.onUpdateRecord)
        self.ui.catgory_track_list.currentIndexChanged.connect(self.onCatgoryChange)
        self.ui.track_record_list.cellChanged.connect(self.onCellChange)
        self.ui.track_record_update.setEnabled(False)
        self.setUpUi()

    def setUpUi(self):
        self.ui.track_record_list.cellChanged.disconnect(self.onCellChange)
        self.ui.track_record_update.setEnabled(False)
        category=self.ui.catgory_track_list.currentText()
        table=self.ui.track_record_list
        table.setRowCount(0)
        trackList, recordItemList=self.trackRecord.getAllTrackRecord(category)
        for track in trackList:
            count=table.rowCount()
            table.insertRow(count)
            table.setItem(count, 0, QtWidgets.QTableWidgetItem(track))
            table.item(count,0).setFlags(QtCore.Qt.ItemIsEditable) #actual make item not editable
            table.setItem(count, 1, QtWidgets.QTableWidgetItem(recordItemList[track]['holder']))
            table.setItem(count, 2, QtWidgets.QTableWidgetItem(recordItemList[track]['record']))
        self.ui.track_record_list.cellChanged.connect(self.onCellChange)

    def onUpdateRecord(self):
        record={}
        category=self.ui.catgory_track_list.currentText()
        table=self.ui.track_record_list
        for i in range(table.rowCount()):
            template={"holder":table.item(i,1).text(),"record":table.item(i,2).text()}
            record[table.item(i,0).text()]=template
        self.trackRecord.updateTrackRecord(category, record)
        QMessageBox.information(self.main,' ','更新完成', QMessageBox.Ok, QMessageBox.Ok)
        self.ui.track_record_update.setEnabled(False)

    def onCatgoryChange(self):
        self.setUpUi()

    def onCellChange(self):
        self.ui.track_record_update.setEnabled(True)
