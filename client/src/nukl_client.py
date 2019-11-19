from PyQt5.QtWidgets import QMainWindow
from src.ui.mainwindow import Ui_MainWindow
from src.model.firedb import firedb
from src.EnrollCheckPage import EnrollCheckPage
from src.MatchControlPage import MatchControlPage
from src.CalenderControlPage import CalenderControlPage
from src.TrackRecordPage import TrackRecordPage
from src.model.MatchInfo import MatchInfo
from src.model.EnrollInfo import EnrollInfo
from src.model.TrackRecord import TrackRecord

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db=firedb()
        self.matchInfo=MatchInfo(self.db)
        self.enrollInfo=EnrollInfo(self.db)
        self.trackRecord=TrackRecord(self.db)
        self.enrollCheck=EnrollCheckPage(self.ui, self.enrollInfo)
        self.matchControl=MatchControlPage(self.ui, self.matchInfo, self.enrollInfo, self)
        self.calenderControl=CalenderControlPage(self.ui, self.matchInfo, self.enrollInfo)
        self.trackRecordPage=TrackRecordPage(self.ui, self.trackRecord, self)
        self.show()
