# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui
from app.browser import PersonaForm
from app.scanFile import DocTable
from selenium.webdriver.common.by import By

class Head(QtWidgets.QWidget):
    def __init__(self, stranica, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.d = None
        self.stranica = stranica

        self.lebel_path = QtWidgets.QLabel('Путь к файлу:', self)
        self.lebel_path.setFixedSize(180, 20)
        self.lebel_path.move(10, 10)

        self.line_path = QtWidgets.QLineEdit(self)
        self.line_path.setFixedSize(155, 20)
        self.line_path.move(10, 30)
        self.line_path.setReadOnly(True)

        self.button_path = QtWidgets.QPushButton("...", self)
        self.button_path.setFixedSize(20, 20)
        self.button_path.move(170, 30)
        self.button_path.clicked.connect(self.open_file)

        self.lebel_seriya = QtWidgets.QLabel('Серия:', self)
        self.lebel_seriya.setFixedSize(50, 20)
        self.lebel_seriya.move(33, 60)
        self.line_seriya = QtWidgets.QLineEdit(self)
        self.line_seriya.setValidator(QtGui.QIntValidator(0,9999))
        self.line_seriya.setFixedSize(50, 20)
        self.line_seriya.move(33, 80)

        self.lebel_nomer = QtWidgets.QLabel('Номер:', self)
        self.lebel_nomer.setFixedSize(50, 20)
        self.lebel_nomer.move(117, 60)
        self.line_nomer = QtWidgets.QLineEdit(self)
        self.line_nomer.setValidator(QtGui.QIntValidator(0,999999))
        self.line_nomer.setFixedSize(50, 20)
        self.line_nomer.move(117, 80)

        self.searh_button = QtWidgets.QPushButton('Найти', self)
        self.searh_button.setFixedSize(80, 30)
        self.searh_button.move(60, 120)
        self.searh_button.clicked.connect(self.searh_person)

        self.send_button = QtWidgets.QPushButton('Очистить', self)
        self.send_button.setFixedSize(80, 30)
        self.send_button.move(60, 155)
        self.send_button.clicked.connect(self.send_data)


    def open_file(self):
        try:
            dialog = QtWidgets.QFileDialog(filter='Word (*.docx)')
            dialog.exec()
            self.line_path.setText(dialog.selectedFiles()[0])
            self.d = DocTable(self.line_path.text())
        except:
            critical = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Ошибка открытия файла", "Не удалось открыть файл, проверьте формат файла", buttons = QtWidgets.QMessageBox.Ok)
            critical.exec()

    def searh_person(self):
        if self.d is not None:
            p = self.d.search_person(self.line_seriya.text(), self.line_nomer.text())
            if p is None:
                criticalp = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "Ошибка персоны", "Не удалось найти персону, проверьте правильность введённых данных", buttons = QtWidgets.QMessageBox.Ok)
                criticalp.exec()
            else:
                p.toSimForm(self.stranica)

    def send_data(self):
        self.line_seriya.setText('')
        self.line_nomer.setText('')

    def closeEvent(self, e):
        self.stranica.close()
        return QtWidgets.QWidget.closeEvent(self, e)
