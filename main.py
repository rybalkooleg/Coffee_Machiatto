from PyQt5 import QtWidgets, QtCore, QtGui, uic
import sqlite3


db = sqlite3.connect("coffee.sqlite")
cur = db.cursor()


class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        uic.loadUi("main.ui", self)

        res = list(cur.execute("SELECT * FROM coffee ORDER BY id DESC"))
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(7)

        for i in range(len(res)):
            for j in range(len(res[i])):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(res[i][j])))
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([""])
    m = Main()
    m.show()
    app.exec()