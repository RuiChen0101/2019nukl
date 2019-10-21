from PyQt5.QtWidgets import QMainWindow
from src.ui.mainwindow import Ui_MainWindow
from src.model.firedb import firedb
from src.EnrollCheckPage import EnrollCheckPage
from src.MatchControlPage import MatchControlPage
from src.model.MatchInfo import MatchInfo
from src.model.EnrollInfo import EnrollInfo

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db=firedb()
        self.matchInfo=MatchInfo(self.db)
        self.enrollInfo=EnrollInfo(self.db)
        self.enrollCheck=EnrollCheckPage(self.ui, self.enrollInfo)
        self.matchControl=MatchControlPage(self.ui, self.matchInfo, self.enrollInfo, self)
        self.show()
