import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
from old_design import Ui_MainWindow


class OldCoffee(QMainWindow, Ui_MainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('../data/coffee.sqlite')
        self.loadButton.clicked.connect(self.load_data)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.modified = {}
        self.titles = None
        self.main_window = main_window
        self.saveButton.clicked.connect(self.save)

        cur = self.con.cursor()
        query = '''SELECT ID FROM data'''
        result = cur.execute(query).fetchall()
        self.idBox.addItems(map(lambda x: str(x[0]), result))

    def load_data(self):
        cur = self.con.cursor()
        result = cur.execute('''SELECT * FROM data
         WHERE ID = ?''', (int(self.idBox.currentText() if self.idBox.currentText() != '' else 1),
                           )).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, el in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(el)))
        self.tableWidget.setHorizontalHeaderLabels(self.titles)

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save(self):
        if self.modified:
            try:
                cur = self.con.cursor()
                query = 'UPDATE data SET\n'
                error1 = int(self.modified['price'])
                error2 = int(self.modified['volume'])
                error3 = int(self.modified['ID'])
                query += ', '.join([f'{key} = "{self.modified[key]}"' for key in self.modified])
                query += ' WHERE ID=?'
                cur.execute(query, (int(self.idBox.currentText() if self.idBox.currentText() != ''
                                        else 1), ))
                self.con.commit()
                self.modified = {}
                cur = self.con.cursor()
                query = '''SELECT ID FROM data'''
                result = cur.execute(query).fetchall()
                self.idBox.addItems(map(lambda x: str(x[0]), result))
            except sqlite3.OperationalError:
                ...
            except Exception:
                ...

    def closeEvent(self, event):
        self.con.close()
        self.main_window.show()
