# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/ArrangementDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_arrangement_dialog(object):
    def setupUi(self, arrangement_dialog):
        arrangement_dialog.setObjectName("arrangement_dialog")
        arrangement_dialog.resize(321, 341)
        arrangement_dialog.setMinimumSize(QtCore.QSize(260, 160))
        arrangement_dialog.setMaximumSize(QtCore.QSize(999999, 999999))
        self.cancel_btn = QtWidgets.QPushButton(arrangement_dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(60, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.ok_btn = QtWidgets.QPushButton(arrangement_dialog)
        self.ok_btn.setGeometry(QtCore.QRect(170, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")
        self.date = QtWidgets.QCalendarWidget(arrangement_dialog)
        self.date.setGeometry(QtCore.QRect(40, 10, 248, 183))
        self.date.setSelectedDate(QtCore.QDate(2019, 11, 11))
        self.date.setObjectName("date")
        self.time = QtWidgets.QTimeEdit(arrangement_dialog)
        self.time.setGeometry(QtCore.QRect(90, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.time.setFont(font)
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.time.setTime(QtCore.QTime(18, 0, 0))
        self.time.setObjectName("time")

        self.retranslateUi(arrangement_dialog)
        QtCore.QMetaObject.connectSlotsByName(arrangement_dialog)

    def retranslateUi(self, arrangement_dialog):
        _translate = QtCore.QCoreApplication.translate
        arrangement_dialog.setWindowTitle(_translate("arrangement_dialog", "約戰時間"))
        self.cancel_btn.setText(_translate("arrangement_dialog", "取消"))
        self.ok_btn.setText(_translate("arrangement_dialog", "確認"))
        self.time.setDisplayFormat(_translate("arrangement_dialog", "HH:mm"))


