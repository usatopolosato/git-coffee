import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5 import uic
from oldAddCoffee import OldCoffee
from newAddCoffee import NewCoffee
from addEditCoffeeForm import Ui_Form


class AddCoffee(QWidget, Ui_Form):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)

        self.main_window = main_window

        self.oldButton.clicked.connect(self.old)
        self.newButton.clicked.connect(self.new)

    def old(self):
        self.second_form = OldCoffee(self)
        self.second_form.show()
        self.hide()

    def new(self):
        self.second_form = NewCoffee(self)
        self.second_form.show()
        self.hide()

    def closeEvent(self, event):
        self.main_window.show()
