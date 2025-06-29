from PySide6.QtWidgets import QApplication 
from Logique import Logique
import sys 

if __name__=='__main__':
    app = QApplication(sys.argv)
    ecran = Logique()
    ecran.show()
    sys.exit(app.exec())