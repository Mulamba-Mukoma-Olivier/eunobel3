from PySide6.QtWidgets import QMainWindow
from eunobel import Ui_MainWindow 

class Logique(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_ecran = Ui_MainWindow()
        self.ui_ecran.setupUi(self)