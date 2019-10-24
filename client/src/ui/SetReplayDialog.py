# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/SetReplayDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_set_replay_dialog(object):
    def setupUi(self, set_replay_dialog):
        set_replay_dialog.setObjectName("set_replay_dialog")
        set_replay_dialog.resize(500, 230)
        set_replay_dialog.setMinimumSize(QtCore.QSize(500, 230))
        set_replay_dialog.setMaximumSize(QtCore.QSize(500, 230))
        self.url = QtWidgets.QLineEdit(set_replay_dialog)
        self.url.setGeometry(QtCore.QRect(100, 60, 351, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.url.setFont(font)
        self.url.setInputMask("")
        self.url.setText("")
        self.url.setObjectName("url")
        self.url_label = QtWidgets.QLabel(set_replay_dialog)
        self.url_label.setGeometry(QtCore.QRect(30, 60, 61, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(16)
        self.url_label.setFont(font)
        self.url_label.setObjectName("url_label")
        self.cancel_btn = QtWidgets.QPushButton(set_replay_dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(110, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.ok_btn = QtWidgets.QPushButton(set_replay_dialog)
        self.ok_btn.setGeometry(QtCore.QRect(280, 140, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")

        self.retranslateUi(set_replay_dialog)
        QtCore.QMetaObject.connectSlotsByName(set_replay_dialog)

    def retranslateUi(self, set_replay_dialog):
        _translate = QtCore.QCoreApplication.translate
        set_replay_dialog.setWindowTitle(_translate("set_replay_dialog", "Dialog"))
        self.url_label.setText(_translate("set_replay_dialog", "URL:"))
        self.cancel_btn.setText(_translate("set_replay_dialog", "取消"))
        self.ok_btn.setText(_translate("set_replay_dialog", "確認"))


