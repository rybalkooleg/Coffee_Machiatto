# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditAndAddCoffee(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.type_name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.type_name_line.setObjectName("type_name_line")
        self.horizontalLayout.addWidget(self.type_name_line)
        self.roast_degree_line = QtWidgets.QLineEdit(self.centralwidget)
        self.roast_degree_line.setObjectName("roast_degree_line")
        self.horizontalLayout.addWidget(self.roast_degree_line)
        self.character_line = QtWidgets.QLineEdit(self.centralwidget)
        self.character_line.setObjectName("character_line")
        self.horizontalLayout.addWidget(self.character_line)
        self.taste_line = QtWidgets.QLineEdit(self.centralwidget)
        self.taste_line.setText("")
        self.taste_line.setObjectName("taste_line")
        self.horizontalLayout.addWidget(self.taste_line)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.price_line = QtWidgets.QLineEdit(self.centralwidget)
        self.price_line.setObjectName("price_line")
        self.horizontalLayout_2.addWidget(self.price_line)
        self.val_line = QtWidgets.QLineEdit(self.centralwidget)
        self.val_line.setObjectName("val_line")
        self.horizontalLayout_2.addWidget(self.val_line)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 1, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.type_name_line.setPlaceholderText(_translate("MainWindow", "Сорт"))
        self.roast_degree_line.setPlaceholderText(_translate("MainWindow", "Прожарка"))
        self.character_line.setPlaceholderText(_translate("MainWindow", "Молотый/в зернах"))
        self.taste_line.setPlaceholderText(_translate("MainWindow", "Описание вкуса"))
        self.price_line.setPlaceholderText(_translate("MainWindow", "Цена"))
        self.val_line.setPlaceholderText(_translate("MainWindow", "Объем упаковки"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))

