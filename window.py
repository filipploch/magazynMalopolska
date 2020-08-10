from functools import partial

from PyQt5 import QtCore
from  calendarWindow import CalendarWindow
import leaguesCollector
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QObject

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

        # self.calendar_middle_date = CalendarWindow()
        # self.calendar_middle_date.create_calendar(1)
        # self.calendar_end_date = CalendarWindow()
        # self.calendar_end_date.create_calendar(2)
        self.add_buttons()
        self.show()

    def add_buttons(self):
        left = 50
        self.button_run = QPushButton("Wczytaj", self)
        self.button_run.move(left, 200)
        self.button_run.clicked.connect(self.leagues_collection.run_scraper)

        self.button_set_start_date = QPushButton("Data 1", self)
        self.button_set_start_date.move(left, 35)
        self.button_set_start_date.clicked.connect(partial(self.open_calendar, 0))

        self.button_set_middle_date = QPushButton("Data 2", self)
        self.button_set_middle_date.move(left, 95)
        self.button_set_middle_date.clicked.connect(partial(self.open_calendar, 1))

        self.button_end_start_date = QPushButton("Data 3", self)
        self.button_end_start_date.move(left, 155)
        self.button_end_start_date.clicked.connect(partial(self.open_calendar, 2))

    def open_calendar(self, number):
        calendar_start_date = CalendarWindow()
        calendar_start_date.create_calendar(number)

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