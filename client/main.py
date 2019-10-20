import sys
from PyQt5.QtWidgets import QApplication
from src.nukl_client import AppWindow

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
