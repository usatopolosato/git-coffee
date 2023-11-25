import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QLabel, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui
from addCoffee import AddCoffee
from main_design import Ui_Form


class Coffee(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = 1

        self.changeButton.clicked.connect(self.change)

    def load_content(self, db):
        con = sqlite3.connect(db)
        cur = con.cursor()
        query = '''SELECT * FROM data'''
        result = cur.execute(query).fetchall()
        self.tableWidget.setRowCount(len(result))
        for i, elem in enumerate(result):
            for j, el in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(el)))
        self.tableWidget.resizeColumnsToContents()
        con.close()

    def change(self):
        self.second_form = AddCoffee(self)
        self.second_form.show()
        self.flag = 1
        self.hide()

    def paintEvent(self, event):
        if self.flag:
            self.load_content('../data/coffee.sqlite')
            self.flag = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
