from PyQt5 import QtCore
from  calendarWindow import CalendarWindow
import leaguesCollector
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QCalendarWidget

class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__()
        self.title = "Okno"
        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 250
        self.leagues_collection = leaguesCollector.LeaguesCollector()
        self.window_builder()

    @staticmethod
    def update(name):
        print(str(name))

    def signal_connect(self):
        self.obj = CalendarWindow()
        self.obj.signal.connect(self.update)

    def window_builder(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.add_date_labels()
        self.add_button()
        self.calendar_start_date = CalendarWindow()
        self.calendar_start_date.create_calendar(0)
        self.show()

    def add_button(self):
        self.button = QPushButton("Wczytaj", self)
        self.button.move(50,200)
        self.button.clicked.connect(self.leagues_collection.run_scraper)

    def add_date_labels(self):
        left = 70
        width = 60
        height = 21
        self.label_start_date = QLabel("2020-08-02", self)
        self.label_middle_date = QLabel("2020-08-09", self)
        self.label_end_date = QLabel("2020-08-16", self)
        self.label_start_date.setGeometry(left, 10, width, height)
        self.label_middle_date.setGeometry(left, 70, width, height)
        self.label_end_date.setGeometry(left, 130, width, height)

    @QtCore.pyqtSlot(str, int)
    def set_label_text(self, text, number):
        assert isinstance(text, str)
        assert isinstance(number, int)

        if number == 0:
            self.label_start_date.setText(text)
        if number == 1:
            self.label_middle_date.setText(text)
        if number == 2:
            self.label_end_date.setText(text)