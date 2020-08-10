from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCalendarWidget
from functools import partial
from datetime import datetime

class CalendarWindow(QWidget):
    signal = pyqtSignal(str, int)

    def __init__(self):
        super(CalendarWindow, self).__init__()
        self.setWindowTitle("Pyside2 Calendar")
        self.setGeometry(300, 200, 250, 200)

    def create_calendar(self, var):
        self.vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        self.vbox.addWidget(self.calendar)
        self.setLayout(self.vbox)
        self.calendar.clicked.connect(partial(self.set_date, var))
        self.show()
        # self.calendar.clicked[QDate].connect(partial(self.setDate, var))



    def set_date(self, number):
        self.date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        # self.signal.emit('2020-02-02', 0)
        self.signal.emit(self.date, number)
        self.close()



    @pyqtSlot(str, int)
    def print_it(self, text, number):
        assert isinstance(text, str)
        assert isinstance(number, int)
        print("print_it")
