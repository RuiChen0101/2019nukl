# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/JudgeAssignDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_judge_assign_dialog(object):
    def setupUi(self, judge_assign_dialog):
        judge_assign_dialog.setObjectName("judge_assign_dialog")
        judge_assign_dialog.resize(500, 230)
        judge_assign_dialog.setMinimumSize(QtCore.QSize(500, 230))
        judge_assign_dialog.setMaximumSize(QtCore.QSize(500, 230))
        self.judge = QtWidgets.QLineEdit(judge_assign_dialog)
        self.judge.setGeometry(QtCore.QRect(100, 60, 351, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.judge.setFont(font)
        self.judge.setInputMask("")
        self.judge.setText("")
        self.judge.setObjectName("judge")
        self.judge_label = QtWidgets.QLabel(judge_assign_dialog)
        self.judge_label.setGeometry(QtCore.QRect(30, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.judge_label.setFont(font)
        self.judge_label.setObjectName("judge_label")
        self.cancel_btn = QtWidgets.QPushButton(judge_assign_dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(110, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.ok_btn = QtWidgets.QPushButton(judge_assign_dialog)
        self.ok_btn.setGeometry(QtCore.QRect(280, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")

        self.retranslateUi(judge_assign_dialog)
        QtCore.QMetaObject.connectSlotsByName(judge_assign_dialog)

    def retranslateUi(self, judge_assign_dialog):
        _translate = QtCore.QCoreApplication.translate
        judge_assign_dialog.setWindowTitle(_translate("judge_assign_dialog", "Dialog"))
        self.judge_label.setText(_translate("judge_assign_dialog", "裁判:"))
        self.cancel_btn.setText(_translate("judge_assign_dialog", "取消"))
        self.ok_btn.setText(_translate("judge_assign_dialog", "確認"))

