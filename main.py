import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QLabel, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui


class Coffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.load_content('coffee.sqlite')

    def load_content(self, db):
        con = sqlite3.connect(db)
        cur = con.cursor()
        query = '''SELECT * FROM data'''
        result = cur.execute(query).fetchall()
        for i, elem in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, el in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(el)))
        self.tableWidget.resizeColumnsToContents()
        con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
