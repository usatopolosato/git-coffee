import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class NewCoffee(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi('new_design.ui', self)

        self.saveButton.clicked.connect(self.save)
        self.main_window = main_window

        self.tableWidget.itemChanged.connect(self.item_changed)
        self.message.setText('')

        self.con = sqlite3.connect('coffee.sqlite')

    def paintEvent(self, event):
        self.tableWidget.resizeColumnsToContents()

    def save(self):
        try:
            ID = int(self.tableWidget.item(0, 0).text())
            NAME = self.tableWidget.item(0, 1).text()
            ROASTING = self.tableWidget.item(0, 2).text()
            MILLED = self.tableWidget.item(0, 3).text()
            DESCRIPTION = self.tableWidget.item(0, 4).text()
            PRICE = int(self.tableWidget.item(0, 5).text())
            VOLUME = int(self.tableWidget.item(0, 6).text())
            cur = self.con.cursor()
            query = '''INSERT INTO data(ID, NAME, ROASTING, MILLED,
                                         DESCRIPTION, PRICE, VOLUME) VALUES(?, ?, ?, ?, ?, ?, ?)'''
            result = cur.execute(query, (ID, NAME, ROASTING, MILLED,
                                         DESCRIPTION, PRICE, VOLUME)).fetchall()
            self.message.setText('Успешно')
            self.con.commit()
        except Exception:
            ...

    def closeEvent(self, event):
        self.con.close()
        self.main_window.show()

    def item_changed(self, item):
        self.message.setText('')
