# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/ArrangementDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_arrangement_dialog(object):
    def setupUi(self, arrangement_dialog):
        arrangement_dialog.setObjectName("arrangement_dialog")
        arrangement_dialog.resize(321, 341)
        arrangement_dialog.setMinimumSize(QtCore.QSize(260, 160))
        arrangement_dialog.setMaximumSize(QtCore.QSize(999999, 999999))
        self.cancel = QtWidgets.QPushButton(arrangement_dialog)
        self.cancel.setGeometry(QtCore.QRect(60, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.ok = QtWidgets.QPushButton(arrangement_dialog)
        self.ok.setGeometry(QtCore.QRect(170, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.calendarWidget = QtWidgets.QCalendarWidget(arrangement_dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 10, 248, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.timeEdit = QtWidgets.QTimeEdit(arrangement_dialog)
        self.timeEdit.setGeometry(QtCore.QRect(100, 220, 118, 22))
        self.timeEdit.setObjectName("timeEdit")

        self.retranslateUi(arrangement_dialog)
        QtCore.QMetaObject.connectSlotsByName(arrangement_dialog)

    def retranslateUi(self, arrangement_dialog):
        _translate = QtCore.QCoreApplication.translate
        arrangement_dialog.setWindowTitle(_translate("arrangement_dialog", "約戰時間"))
        self.cancel.setText(_translate("arrangement_dialog", "取消"))
        self.ok.setText(_translate("arrangement_dialog", "確認"))

