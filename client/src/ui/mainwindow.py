# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/mainui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 850)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 850))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 850))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.function_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.function_tab.setGeometry(QtCore.QRect(0, 10, 1001, 831))
        self.function_tab.setStyleSheet("background-color:#f0f0f0;")
        self.function_tab.setObjectName("function_tab")
        self.enroll_check_tab = QtWidgets.QWidget()
        self.enroll_check_tab.setObjectName("enroll_check_tab")
        self.cancel_btn = QtWidgets.QPushButton(self.enroll_check_tab)
        self.cancel_btn.setGeometry(QtCore.QRect(460, 180, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName("cancel_btn")
        self.checked_list = QtWidgets.QTableWidget(self.enroll_check_tab)
        self.checked_list.setGeometry(QtCore.QRect(560, 60, 431, 701))
        self.checked_list.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.checked_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.checked_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.checked_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.checked_list.setObjectName("checked_list")
        self.checked_list.setColumnCount(5)
        self.checked_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.checked_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.checked_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.checked_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.checked_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.checked_list.setHorizontalHeaderItem(4, item)
        self.checked_list.horizontalHeader().setDefaultSectionSize(84)
        self.check_btn = QtWidgets.QPushButton(self.enroll_check_tab)
        self.check_btn.setGeometry(QtCore.QRect(460, 130, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.check_btn.setFont(font)
        self.check_btn.setObjectName("check_btn")
        self.uncheck_list_label = QtWidgets.QLabel(self.enroll_check_tab)
        self.uncheck_list_label.setGeometry(QtCore.QRect(140, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.uncheck_list_label.setFont(font)
        self.uncheck_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.uncheck_list_label.setObjectName("uncheck_list_label")
        self.checked_list_label = QtWidgets.QLabel(self.enroll_check_tab)
        self.checked_list_label.setGeometry(QtCore.QRect(690, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.checked_list_label.setFont(font)
        self.checked_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.checked_list_label.setObjectName("checked_list_label")
        self.delete_btn = QtWidgets.QPushButton(self.enroll_check_tab)
        self.delete_btn.setGeometry(QtCore.QRect(460, 230, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.deleted_list = QtWidgets.QTableWidget(self.enroll_check_tab)
        self.deleted_list.setGeometry(QtCore.QRect(10, 500, 431, 261))
        self.deleted_list.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.deleted_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.deleted_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.deleted_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.deleted_list.setObjectName("deleted_list")
        self.deleted_list.setColumnCount(5)
        self.deleted_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.deleted_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleted_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleted_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleted_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.deleted_list.setHorizontalHeaderItem(4, item)
        self.deleted_list.horizontalHeader().setDefaultSectionSize(84)
        self.deleted_list_label = QtWidgets.QLabel(self.enroll_check_tab)
        self.deleted_list_label.setGeometry(QtCore.QRect(140, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.deleted_list_label.setFont(font)
        self.deleted_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.deleted_list_label.setObjectName("deleted_list_label")
        self.refresh_btn = QtWidgets.QPushButton(self.enroll_check_tab)
        self.refresh_btn.setGeometry(QtCore.QRect(460, 590, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.refresh_btn.setFont(font)
        self.refresh_btn.setObjectName("refresh_btn")
        self.uncheck_list = QtWidgets.QTableWidget(self.enroll_check_tab)
        self.uncheck_list.setGeometry(QtCore.QRect(10, 60, 431, 381))
        self.uncheck_list.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.uncheck_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.uncheck_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.uncheck_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.uncheck_list.setObjectName("uncheck_list")
        self.uncheck_list.setColumnCount(5)
        self.uncheck_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.uncheck_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uncheck_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uncheck_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.uncheck_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.uncheck_list.setHorizontalHeaderItem(4, item)
        self.uncheck_list.horizontalHeader().setDefaultSectionSize(84)
        self.relife_btn = QtWidgets.QPushButton(self.enroll_check_tab)
        self.relife_btn.setGeometry(QtCore.QRect(460, 660, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.relife_btn.setFont(font)
        self.relife_btn.setObjectName("relife_btn")
        self.function_tab.addTab(self.enroll_check_tab, "")
        self.match_tab = QtWidgets.QWidget()
        self.match_tab.setObjectName("match_tab")
        self.catgory_list = QtWidgets.QComboBox(self.match_tab)
        self.catgory_list.setGeometry(QtCore.QRect(30, 20, 101, 22))
        self.catgory_list.setMaxCount(3)
        self.catgory_list.setObjectName("catgory_list")
        self.catgory_list.addItem("")
        self.catgory_list.addItem("")
        self.catgory_list.addItem("")
        self.match_list_lable = QtWidgets.QLabel(self.match_tab)
        self.match_list_lable.setGeometry(QtCore.QRect(200, 60, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.match_list_lable.setFont(font)
        self.match_list_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.match_list_lable.setObjectName("match_list_lable")
        self.match_list = QtWidgets.QTableWidget(self.match_tab)
        self.match_list.setGeometry(QtCore.QRect(50, 100, 431, 241))
        self.match_list.setStyleSheet("background-color:#ffffff;")
        self.match_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.match_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.match_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.match_list.setObjectName("match_list")
        self.match_list.setColumnCount(6)
        self.match_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.match_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.match_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.match_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.match_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.match_list.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.match_list.setHorizontalHeaderItem(5, item)
        self.match_list.horizontalHeader().setDefaultSectionSize(84)
        self.round_list = QtWidgets.QComboBox(self.match_tab)
        self.round_list.setGeometry(QtCore.QRect(30, 50, 101, 22))
        self.round_list.setMaxCount(6)
        self.round_list.setObjectName("round_list")
        self.round_list.addItem("")
        self.round_list.addItem("")
        self.round_list.addItem("")
        self.round_list.addItem("")
        self.round_list.addItem("")
        self.round_list.addItem("")
        self.player_list = QtWidgets.QTableWidget(self.match_tab)
        self.player_list.setGeometry(QtCore.QRect(540, 100, 181, 241))
        self.player_list.setStyleSheet("background-color:#ffffff;")
        self.player_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.player_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.player_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.player_list.setObjectName("player_list")
        self.player_list.setColumnCount(2)
        self.player_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.player_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.player_list.setHorizontalHeaderItem(1, item)
        self.player_list.horizontalHeader().setDefaultSectionSize(84)
        self.player_list_label = QtWidgets.QLabel(self.match_tab)
        self.player_list_label.setGeometry(QtCore.QRect(540, 60, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.player_list_label.setFont(font)
        self.player_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_list_label.setObjectName("player_list_label")
        self.delete_match_btn = QtWidgets.QPushButton(self.match_tab)
        self.delete_match_btn.setGeometry(QtCore.QRect(320, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.delete_match_btn.setFont(font)
        self.delete_match_btn.setObjectName("delete_match_btn")
        self.new_match_btn = QtWidgets.QPushButton(self.match_tab)
        self.new_match_btn.setGeometry(QtCore.QRect(110, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.new_match_btn.setFont(font)
        self.new_match_btn.setObjectName("new_match_btn")
        self.advance_player_list = QtWidgets.QTableWidget(self.match_tab)
        self.advance_player_list.setGeometry(QtCore.QRect(780, 100, 181, 241))
        self.advance_player_list.setStyleSheet("background-color:#ffffff;")
        self.advance_player_list.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.advance_player_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.advance_player_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.advance_player_list.setObjectName("advance_player_list")
        self.advance_player_list.setColumnCount(2)
        self.advance_player_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.advance_player_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.advance_player_list.setHorizontalHeaderItem(1, item)
        self.advance_player_list.horizontalHeader().setDefaultSectionSize(84)
        self.advance_player_list_label = QtWidgets.QLabel(self.match_tab)
        self.advance_player_list_label.setGeometry(QtCore.QRect(780, 60, 191, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.advance_player_list_label.setFont(font)
        self.advance_player_list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.advance_player_list_label.setObjectName("advance_player_list_label")
        self.set_arrangement_btn = QtWidgets.QPushButton(self.match_tab)
        self.set_arrangement_btn.setGeometry(QtCore.QRect(480, 500, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.set_arrangement_btn.setFont(font)
        self.set_arrangement_btn.setObjectName("set_arrangement_btn")
        self.match_finish_btn = QtWidgets.QPushButton(self.match_tab)
        self.match_finish_btn.setGeometry(QtCore.QRect(480, 600, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.match_finish_btn.setFont(font)
        self.match_finish_btn.setObjectName("match_finish_btn")
        self.arranged_time_label = QtWidgets.QLabel(self.match_tab)
        self.arranged_time_label.setGeometry(QtCore.QRect(60, 650, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.arranged_time_label.setFont(font)
        self.arranged_time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.arranged_time_label.setObjectName("arranged_time_label")
        self.arranged_time = QtWidgets.QLabel(self.match_tab)
        self.arranged_time.setGeometry(QtCore.QRect(220, 650, 201, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.arranged_time.setFont(font)
        self.arranged_time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.arranged_time.setObjectName("arranged_time")
        self.group = QtWidgets.QLabel(self.match_tab)
        self.group.setGeometry(QtCore.QRect(220, 490, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.group.setFont(font)
        self.group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.group.setObjectName("group")
        self.group_label = QtWidgets.QLabel(self.match_tab)
        self.group_label.setGeometry(QtCore.QRect(100, 490, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.group_label.setFont(font)
        self.group_label.setAlignment(QtCore.Qt.AlignCenter)
        self.group_label.setObjectName("group_label")
        self.catgory_label = QtWidgets.QLabel(self.match_tab)
        self.catgory_label.setGeometry(QtCore.QRect(100, 530, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.catgory_label.setFont(font)
        self.catgory_label.setAlignment(QtCore.Qt.AlignCenter)
        self.catgory_label.setObjectName("catgory_label")
        self.catgory = QtWidgets.QLabel(self.match_tab)
        self.catgory.setGeometry(QtCore.QRect(220, 530, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.catgory.setFont(font)
        self.catgory.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.catgory.setObjectName("catgory")
        self.round_label = QtWidgets.QLabel(self.match_tab)
        self.round_label.setGeometry(QtCore.QRect(100, 570, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.round_label.setFont(font)
        self.round_label.setAlignment(QtCore.Qt.AlignCenter)
        self.round_label.setObjectName("round_label")
        self.round = QtWidgets.QLabel(self.match_tab)
        self.round.setGeometry(QtCore.QRect(220, 570, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.round.setFont(font)
        self.round.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.round.setObjectName("round")
        self.status_label = QtWidgets.QLabel(self.match_tab)
        self.status_label.setGeometry(QtCore.QRect(100, 610, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.status = QtWidgets.QLabel(self.match_tab)
        self.status.setGeometry(QtCore.QRect(220, 610, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        self.status.setFont(font)
        self.status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.status.setObjectName("status")
        self.set_replay_btn = QtWidgets.QPushButton(self.match_tab)
        self.set_replay_btn.setGeometry(QtCore.QRect(480, 650, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.set_replay_btn.setFont(font)
        self.set_replay_btn.setObjectName("set_replay_btn")
        self.judge_assign_btn = QtWidgets.QPushButton(self.match_tab)
        self.judge_assign_btn.setGeometry(QtCore.QRect(480, 550, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.judge_assign_btn.setFont(font)
        self.judge_assign_btn.setObjectName("judge_assign_btn")
        self.function_tab.addTab(self.match_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.function_tab.setCurrentIndex(1)
        self.catgory_list.setCurrentIndex(0)
        self.round_list.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2019北區跑跑聯賽管理系統"))
        self.cancel_btn.setText(_translate("MainWindow", "<<取消"))
        item = self.checked_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "報名時間"))
        item = self.checked_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.checked_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "項目"))
        item = self.checked_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "學校"))
        item = self.checked_list.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "docID"))
        self.check_btn.setText(_translate("MainWindow", "確認>>"))
        self.uncheck_list_label.setText(_translate("MainWindow", "未確認清單"))
        self.checked_list_label.setText(_translate("MainWindow", "已確認清單"))
        self.delete_btn.setText(_translate("MainWindow", "X刪除X"))
        item = self.deleted_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "報名時間"))
        item = self.deleted_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.deleted_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "項目"))
        item = self.deleted_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "學校"))
        item = self.deleted_list.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "docID"))
        self.deleted_list_label.setText(_translate("MainWindow", "已刪除清單"))
        self.refresh_btn.setText(_translate("MainWindow", "重整"))
        item = self.uncheck_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "報名時間"))
        item = self.uncheck_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.uncheck_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "項目"))
        item = self.uncheck_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "學校"))
        item = self.uncheck_list.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "docID"))
        self.relife_btn.setText(_translate("MainWindow", "回復"))
        self.function_tab.setTabText(self.function_tab.indexOf(self.enroll_check_tab), _translate("MainWindow", "報到確認"))
        self.catgory_list.setItemText(0, _translate("MainWindow", "個人競速"))
        self.catgory_list.setItemText(1, _translate("MainWindow", "個人道具"))
        self.catgory_list.setItemText(2, _translate("MainWindow", "團體競速"))
        self.match_list_lable.setText(_translate("MainWindow", "比賽清單"))
        item = self.match_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "組別"))
        item = self.match_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "項目"))
        item = self.match_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "狀態"))
        item = self.match_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "裁判"))
        item = self.match_list.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "約戰日期"))
        item = self.match_list.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "docID"))
        self.round_list.setItemText(0, _translate("MainWindow", "128強"))
        self.round_list.setItemText(1, _translate("MainWindow", "64強"))
        self.round_list.setItemText(2, _translate("MainWindow", "32強"))
        self.round_list.setItemText(3, _translate("MainWindow", "16強"))
        self.round_list.setItemText(4, _translate("MainWindow", "8強"))
        self.round_list.setItemText(5, _translate("MainWindow", "4強"))
        item = self.player_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.player_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "比賽分數"))
        self.player_list_label.setText(_translate("MainWindow", "比賽選手名單"))
        self.delete_match_btn.setText(_translate("MainWindow", "刪除比賽"))
        self.new_match_btn.setText(_translate("MainWindow", "新比賽"))
        item = self.advance_player_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.advance_player_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "比賽分數"))
        self.advance_player_list_label.setText(_translate("MainWindow", "晉級選手名單"))
        self.set_arrangement_btn.setText(_translate("MainWindow", "約戰"))
        self.match_finish_btn.setText(_translate("MainWindow", "比賽完成"))
        self.arranged_time_label.setText(_translate("MainWindow", "約戰時間:"))
        self.arranged_time.setText(_translate("MainWindow", "11/11, 18:00"))
        self.group.setText(_translate("MainWindow", "A"))
        self.group_label.setText(_translate("MainWindow", "組別:"))
        self.catgory_label.setText(_translate("MainWindow", "項目:"))
        self.catgory.setText(_translate("MainWindow", "個人競速"))
        self.round_label.setText(_translate("MainWindow", "輪數:"))
        self.round.setText(_translate("MainWindow", "128強"))
        self.status_label.setText(_translate("MainWindow", "狀態:"))
        self.status.setText(_translate("MainWindow", "已完成"))
        self.set_replay_btn.setText(_translate("MainWindow", "儲存直播紀錄"))
        self.judge_assign_btn.setText(_translate("MainWindow", "裁判指派"))
        self.function_tab.setTabText(self.function_tab.indexOf(self.match_tab), _translate("MainWindow", "場次用"))

