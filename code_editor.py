import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from pyperclip import copy
from string import ascii_letters, digits
from random import sample

from stylesheet import *


class EditorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.sql_connect = sqlite3.connect('database/pcode_data.db')
        self.sql_create_table_query = "CREATE TABLE IF NOT EXISTS pcode_data(pcode TEXT, paste TEXT, page TEXT);"
        self.sql_cursor = self.sql_connect.cursor()
        self.sql_cursor.execute(self.sql_create_table_query)
        self.sql_connect.commit()
        self.sql_cursor.close()

        self.pcode = ''

        self.setObjectName("MainWindow")
        self.resize(870, 759)
        self.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"gridline-color: rgb(71, 71, 71);\n"
"border-color: rgb(118, 118, 118);\n"
"color: rgb(220, 220, 220);\n"
"selection-background-color: rgb(252, 165, 3);\n"
"selection-color: rgb(43, 43, 43);\n"
"")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 158, 781, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("font: 14pt \"Courier New\";")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.copy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_btn.setGeometry(QtCore.QRect(10, 57, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.copy_btn.setFont(font)
        set_button_stylesheet(self.copy_btn)
        self.copy_btn.setObjectName("copy_btn")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(10, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(font)
        set_button_stylesheet(self.save_btn)
        self.save_btn.setObjectName("save_btn")
        self.pcode_gb = QtWidgets.QGroupBox(self.centralwidget)
        self.pcode_gb.setGeometry(QtCore.QRect(420, 10, 371, 131))
        self.pcode_gb.setObjectName("pcode_gb")
        self.pcode_label = QtWidgets.QLabel(self.pcode_gb)
        self.pcode_label.setGeometry(QtCore.QRect(10, 30, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.pcode_label.setFont(font)
        self.pcode_label.setFrameShape(QtWidgets.QFrame.Box)
        self.pcode_label.setObjectName("label")
        self.generate_pc_btn = QtWidgets.QPushButton(self.pcode_gb)
        self.generate_pc_btn.setGeometry(QtCore.QRect(10, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.generate_pc_btn.setFont(font)
        self.generate_pc_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate_pc_btn.setObjectName("generate_pc_btn")
        set_button_stylesheet(self.generate_pc_btn)
        self.hide_pcode = QtWidgets.QRadioButton(self.pcode_gb)
        self.hide_pcode.setGeometry(QtCore.QRect(220, 30, 131, 31))
        self.hide_pcode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hide_pcode.setObjectName("search_pcode_btn")
        self.copy_pc_btn = QtWidgets.QPushButton(self.pcode_gb)
        self.copy_pc_btn.setGeometry(QtCore.QRect(230, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.copy_pc_btn.setFont(font)
        self.copy_pc_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        set_button_stylesheet(self.copy_pc_btn)
        self.copy_pc_btn.setObjectName("copy_pc_btn")
        self.filename = QtWidgets.QLineEdit(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(10, 20, 401, 31))
        self.filename.setObjectName("filename")
        self.file_view = QtWidgets.QComboBox(self.centralwidget)
        self.file_view.setGeometry(QtCore.QRect(200, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.file_view.setFont(font)
        self.file_view.setObjectName("file_view")
        self.file_view.addItem("")
        self.file_view.addItem("")
        self.file_view.addItem("")
        self.file_view.addItem("")
        self.file_view.addItem("")
        self.file_view.addItem("")
        self.file_view.addItem("")
        self.file_view.addItem("")
        self.delete_paste_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_paste_btn.setGeometry(QtCore.QRect(800, 20, 61, 51))
        self.delete_paste_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        set_button_delete_stylesheet(self.delete_paste_btn)
        self.delete_paste_btn.setObjectName("create_paste_btn")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.to_this_btn = QtWidgets.QPushButton(self)
        self.to_this_btn.setText('')
        self.to_this_btn.setGeometry(QtCore.QRect(290, 97, 51, 41))
        set_button_stylesheet(self.to_this_btn)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.set_functions()
        self.generate_pcode()

    def set_functions(self):
        self.copy_btn.clicked.connect(lambda: copy(self.textEdit.toPlainText()))
        self.generate_pc_btn.clicked.connect(lambda: self.generate_pcode())
        self.hide_pcode.clicked.connect(lambda: self.hide_pcode_f())
        self.copy_pc_btn.clicked.connect(lambda: copy(self.pcode))
        self.save_btn.clicked.connect(lambda: self.save_paste())
        self.to_this_btn.clicked.connect(lambda: self.change_file())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Script Edit"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.copy_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Copy all the code.</span></p></body></html>"))
        self.copy_btn.setText(_translate("MainWindow", "Copy"))
        self.save_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Save this paste.</span></p></body></html>"))
        self.save_btn.setText(_translate("MainWindow", "Save at..."))
        self.pcode_gb.setTitle(_translate("MainWindow", "Pcode"))
        self.pcode_label.setText(_translate("MainWindow", "****************"))
        self.generate_pc_btn.setText(_translate("MainWindow", "Generate new"))
        self.hide_pcode.setText(_translate("MainWindow", "Show pcode"))
        self.copy_pc_btn.setText(_translate("MainWindow", "Copy"))
        self.file_view.setItemText(0, _translate("MainWindow", "1"))
        self.file_view.setItemText(1, _translate("MainWindow", "2"))
        self.file_view.setItemText(2, _translate("MainWindow", "3"))
        self.file_view.setItemText(3, _translate("MainWindow", "4"))
        self.file_view.setItemText(4, _translate("MainWindow", "5"))
        self.file_view.setItemText(5, _translate("MainWindow", "6"))
        self.file_view.setItemText(6, _translate("MainWindow", "7"))
        self.file_view.setItemText(7, _translate("MainWindow", "8"))
        self.delete_paste_btn.setText(_translate("MainWindow", "Z"))
        self.to_this_btn.setText(_translate("MainWindow", "set"))

    def generate_pcode(self):
        CHARS = ascii_letters + digits
        self.pcode = ''.join(sample(CHARS, k=16))
        if not self.hide_pcode.isChecked():
            self.pcode_label.setText(self.pcode)

    def hide_pcode_f(self):
        if self.hide_pcode.isChecked():
            self.pcode_label.setText('****************')
        else:
            self.pcode_label.setText(self.pcode)

    def save_paste(self):
        try:
            sql_connect = sqlite3.connect('database/pcode_data.db')
            sql_cursor = sql_connect.cursor()
            sql_cursor.execute("SELECT * FROM pcode_data")
            all_values = sql_cursor.fetchall()
            all_pcodes = list(map(lambda n: n[0], all_values))
            all_pages = list(map(lambda n: n[2], all_values))
            if self.pcode in all_pcodes and self.file_view.currentText() == all_pages[all_pcodes.index(self.pcode)]:
                sql_insert_request = "UPDATE pcode_data SET paste = ?, page = ? WHERE pcode = ?"
                sql_insert_values = (self.textEdit.toPlainText(), self.file_view.currentText(), self.pcode)
            else:
                sql_insert_request = "INSERT INTO pcode_data VALUES(?, ?, ?);"
                sql_insert_values = (self.pcode, self.textEdit.toPlainText(), self.file_view.currentText())
            sql_cursor.execute(sql_insert_request, sql_insert_values)
            sql_connect.commit()
            sql_cursor.close()
        except sqlite3.Error as error:
            print('[!] sqlite3 error in save_paste():', error)

    def change_file(self):
        try:
            sql_connect = sqlite3.connect('database/pcode_data.db')
            sql_cursor = sql_connect.cursor()

            sql_cursor.execute("SELECT * FROM pcode_data")
            all_values = sql_cursor.fetchall()
            all_pcodes_pages = list(map(lambda n: (n[0], n[2]), all_values))
            pages_in_pcodes = {}    # {pcode: [page1, page2, ...], ...}
            for row in all_pcodes_pages:
                pages_in_pcodes[row[0]] = []

            for row in all_pcodes_pages:
                pages_in_pcodes[row[0]].append(row[1])

            if self.file_view.currentText() in pages_in_pcodes[self.pcode]:
                sql_request = "SELECT * FROM pcode_data WHERE pcode = ? AND page = ?"
                sql_values = (self.pcode, self.file_view.currentText())
                sql_cursor.execute(sql_request, sql_values)
                text_in_db = sql_cursor.fetchall()[-1]
                print(text_in_db)
                self.textEdit.setText(text_in_db[1])
            else:
                self.textEdit.setText('[!] This page does not exists')

        except sqlite3.Error as error:
            print('[!] sqlite3 error:', error)
