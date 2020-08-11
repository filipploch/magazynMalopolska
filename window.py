from functools import partial

from PyQt5 import QtCore
from  calendarWindow import CalendarWindow
import leaguesCollector
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel
import datetime

class Window(QMainWindow):
    signal = pyqtSignal(str, int)
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__()
        self.title = "Okno"
        self.top = 100
        self.left = 100
        self.width = 200
        self.height = 250
        self.leagues_collection = leaguesCollector.LeaguesCollector()
        self.window_builder()

    def window_builder(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('img\\icon.png'))
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
        self.calendar = CalendarWindow()
        self.calendar.signal.connect(self.set_label_text)
        self.button_run.disconnect()
        self.calendar.create_calendar(number)

    def add_date_labels(self):
        left = 70
        width = 60
        height = 21
        start_date = datetime.datetime.strftime(self.leagues_collection.d0, '%Y-%m-%d')
        middle_date = datetime.datetime.strftime(self.leagues_collection.d1, '%Y-%m-%d')
        end_date = datetime.datetime.strftime(self.leagues_collection.d2, '%Y-%m-%d')
        self.label_start_date = QLabel(start_date, self)
        self.label_middle_date = QLabel(middle_date, self)
        self.label_end_date = QLabel(end_date, self)
        self.label_start_date.setGeometry(left, 10, width, height)
        self.label_middle_date.setGeometry(left, 70, width, height)
        self.label_end_date.setGeometry(left, 130, width, height)

    @QtCore.pyqtSlot(str, int)
    def set_label_text(self, text, number):
        assert isinstance(text, str)
        assert isinstance(number, int)

        if number == 0:
            self.label_start_date.setText(text)
            x = datetime.datetime.strptime(text, '%Y-%m-%d')
            self.leagues_collection.d0 = x
        if number == 1:
            self.label_middle_date.setText(text)
            x = datetime.datetime.strptime(text, '%Y-%m-%d')
            self.leagues_collection.d1 = x
        if number == 2:
            self.label_end_date.setText(text)
            x = datetime.datetime.strptime(text, '%Y-%m-%d')
            self.leagues_collection.d2 = x
        self.button_run.clicked.connect(self.leagues_collection.run_scraper)