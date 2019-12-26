from PyQt5 import QtWidgets, QtCore, QtGui, uic
from design import *
from addEditCoffeeForm import *
import sqlite3


db = sqlite3.connect("data/coffee.sqlite")
cur = db.cursor()


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        res = list(cur.execute("SELECT * FROM coffee ORDER BY id DESC"))
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(7)
        edit_action = QtWidgets.QAction(QtGui.QIcon(), "Изменить/добавить", self)
        edit_action.triggered.connect(self.open_editing_window)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(edit_action)

        for i in range(len(res)):
            for j in range(len(res[i])):
                self.tableWidget.setItem(i, j, 
                                         QtWidgets.QTableWidgetItem(str(res[i][j])))
    
    def open_editing_window(self):
        w = EditAndAddCoffee(self)
        w.show()

class EditAndAddCoffee(QtWidgets.QMainWindow, Ui_EditAndAddCoffee):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.add_button.clicked.connect(self.add_coffee)
        res = list(cur.execute("SELECT * FROM coffee ORDER BY id DESC"))
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(7)
        self.attributes = dict(enumerate("type_name,roast_degree,character,taste,price,vol".split(","), 1))

        for i in range(len(res)):
            for j in range(len(res[i])):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(res[i][j])))
        self.tableWidget.cellChanged.connect(self.update_data)
    
    def add_coffee(self):
        if self.type_name_line.text() != "" and\
            self.roast_degree_line.text() != "" and\
            self.character_line.text() != "" and\
            self.taste_line.text() != "" and\
            self.price_line.text() != "" and\
            self.val_line.text() != "":
            cur.execute("""INSERT INTO coffee (type_name, roast_degree, character, taste, price, vol)
                        VALUES (?, ?, ?, ?, ?, ?)""", (self.type_name_line.text(),
                                                        self.roast_degree_line.text(),
                                                        self.character_line.text(),
                                                        self.taste_line.text(),
                                                        self.price_line.text(),
                                                        self.val_line.text()))
            db.commit()
    
    def update_data(self, row, col):
        id_ = self.tableWidget.item(row, 0).text()
        changed_attr = self.attributes[col]
        new_text = self.tableWidget.item(row, col).text()
        if new_text != "":
            cur.execute(f"UPDATE coffee SET {changed_attr} = ? WHERE id = ?", (new_text, id_))
            db.commit()

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([""])
    m = Main()
    m.show()
    app.exec()