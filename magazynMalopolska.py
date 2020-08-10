import sys
import window
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

gui = window.Window()
# gui.show()

app.exec_()