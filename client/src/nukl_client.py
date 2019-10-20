from PyQt5.QtWidgets import QMainWindow
from src.ui.mainwindow import Ui_MainWindow
from src.model.firedb import firedb
from src.EnrollCheckPage import EnrollCheckPage
from src.MatchControlPage import MatchControlPage

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db=firedb()
        self.enrollCheck=EnrollCheckPage(self.ui, self.db)
        self.matchControl=MatchControlPage(self.ui, self.db)
        self.show()
