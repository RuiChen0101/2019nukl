# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/NewMatchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_match_dialog(object):
    def setupUi(self, new_match_dialog):
        new_match_dialog.setObjectName("new_match_dialog")
        new_match_dialog.resize(770, 540)
        new_match_dialog.setMinimumSize(QtCore.QSize(770, 540))
        new_match_dialog.setMaximumSize(QtCore.QSize(770, 540))
        self.total_player_list_label = QtWidgets.QLabel(new_match_dialog)
        self.total_player_list_label.setGeometry(QtCore.QRect(100, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.total_player_list_label.setFont(font)
        self.total_player_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.total_player_list_label.setObjectName("total_player_list_label")
        self.total_player_list = QtWidgets.QTableWidget(new_match_dialog)
        self.total_player_list.setGeometry(QtCore.QRect(10, 50, 341, 351))
        self.total_player_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.total_player_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.total_player_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.total_player_list.setObjectName("total_player_list")
        self.total_player_list.setColumnCount(4)
        self.total_player_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.total_player_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_player_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_player_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.total_player_list.setHorizontalHeaderItem(3, item)
        self.total_player_list.horizontalHeader().setDefaultSectionSize(84)
        self.player_list_label = QtWidgets.QLabel(new_match_dialog)
        self.player_list_label.setGeometry(QtCore.QRect(540, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.player_list_label.setFont(font)
        self.player_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_list_label.setObjectName("player_list_label")
        self.player_list = QtWidgets.QTableWidget(new_match_dialog)
        self.player_list.setGeometry(QtCore.QRect(480, 50, 261, 351))
        self.player_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.player_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.player_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.player_list.setObjectName("player_list")
        self.player_list.setColumnCount(4)
        self.player_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.player_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.player_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.player_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.player_list.setHorizontalHeaderItem(3, item)
        self.player_list.horizontalHeader().setDefaultSectionSize(84)
        self.add_btn = QtWidgets.QPushButton(new_match_dialog)
        self.add_btn.setGeometry(QtCore.QRect(370, 150, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.remove_btn = QtWidgets.QPushButton(new_match_dialog)
        self.remove_btn.setGeometry(QtCore.QRect(370, 210, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.remove_btn.setFont(font)
        self.remove_btn.setObjectName("remove_btn")
        self.catgory = QtWidgets.QLabel(new_match_dialog)
        self.catgory.setGeometry(QtCore.QRect(130, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.catgory.setFont(font)
        self.catgory.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.catgory.setObjectName("catgory")
        self.round = QtWidgets.QLabel(new_match_dialog)
        self.round.setGeometry(QtCore.QRect(130, 490, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.round.setFont(font)
        self.round.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.round.setObjectName("round")
        self.catgory_label = QtWidgets.QLabel(new_match_dialog)
        self.catgory_label.setGeometry(QtCore.QRect(20, 450, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.catgory_label.setFont(font)
        self.catgory_label.setAlignment(QtCore.Qt.AlignCenter)
        self.catgory_label.setObjectName("catgory_label")
        self.round_label = QtWidgets.QLabel(new_match_dialog)
        self.round_label.setGeometry(QtCore.QRect(20, 490, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.round_label.setFont(font)
        self.round_label.setAlignment(QtCore.Qt.AlignCenter)
        self.round_label.setObjectName("round_label")
        self.group_label = QtWidgets.QLabel(new_match_dialog)
        self.group_label.setGeometry(QtCore.QRect(20, 410, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.group_label.setFont(font)
        self.group_label.setAlignment(QtCore.Qt.AlignCenter)
        self.group_label.setObjectName("group_label")
        self.group = QtWidgets.QLineEdit(new_match_dialog)
        self.group.setGeometry(QtCore.QRect(132, 409, 121, 31))
        self.group.setObjectName("group")
        self.ok_btn = QtWidgets.QPushButton(new_match_dialog)
        self.ok_btn.setGeometry(QtCore.QRect(650, 470, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(new_match_dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(550, 470, 91, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")

        self.retranslateUi(new_match_dialog)
        QtCore.QMetaObject.connectSlotsByName(new_match_dialog)

    def retranslateUi(self, new_match_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_match_dialog.setWindowTitle(_translate("new_match_dialog", "新比賽"))
        self.total_player_list_label.setText(_translate("new_match_dialog", "選手總名單"))
        item = self.total_player_list.horizontalHeaderItem(0)
        item.setText(_translate("new_match_dialog", "ID"))
        item = self.total_player_list.horizontalHeaderItem(1)
        item.setText(_translate("new_match_dialog", "項目"))
        item = self.total_player_list.horizontalHeaderItem(2)
        item.setText(_translate("new_match_dialog", "輪數"))
        item = self.total_player_list.horizontalHeaderItem(3)
        item.setText(_translate("new_match_dialog", "docID"))
        self.player_list_label.setText(_translate("new_match_dialog", "選手名單"))
        item = self.player_list.horizontalHeaderItem(0)
        item.setText(_translate("new_match_dialog", "ID"))
        item = self.player_list.horizontalHeaderItem(1)
        item.setText(_translate("new_match_dialog", "項目"))
        item = self.player_list.horizontalHeaderItem(2)
        item.setText(_translate("new_match_dialog", "輪數"))
        item = self.player_list.horizontalHeaderItem(3)
        item.setText(_translate("new_match_dialog", "docID"))
        self.add_btn.setText(_translate("new_match_dialog", "加入>>"))
        self.remove_btn.setText(_translate("new_match_dialog", "<<取消"))
        self.catgory.setText(_translate("new_match_dialog", "個人競速"))
        self.round.setText(_translate("new_match_dialog", "128強"))
        self.catgory_label.setText(_translate("new_match_dialog", "項目:"))
        self.round_label.setText(_translate("new_match_dialog", "輪數:"))
        self.group_label.setText(_translate("new_match_dialog", "組別:"))
        self.ok_btn.setText(_translate("new_match_dialog", "確認"))
        self.cancel_btn.setText(_translate("new_match_dialog", "取消"))

