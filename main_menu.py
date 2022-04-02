from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sqlite3

from code_editor import EditorWindow


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(391, 600)
        self.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"gridline-color: rgb(71, 71, 71);\n"
"selection-background-color: rgb(252, 186, 3);\n"
"border-color: rgb(118, 118, 118);\n"
"color: rgb(220, 220, 220);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 221, 91))
        self.groupBox.setObjectName("groupBox")
        self.plus_paste_btn = QtWidgets.QPushButton(self.groupBox)
        self.plus_paste_btn.setGeometry(QtCore.QRect(20, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plus_paste_btn.setFont(font)
        self.plus_paste_btn.setObjectName("plus_paste_btn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 120, 351, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.search_paste_lbl = QtWidgets.QLineEdit(self.groupBox_2)
        self.search_paste_lbl.setGeometry(QtCore.QRect(10, 40, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.search_paste_lbl.setFont(font)
        self.search_paste_lbl.setObjectName("search_paste_lbl")
        self.search_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.search_btn.setGeometry(QtCore.QRect(270, 40, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.plus_paste_btn.clicked.connect(lambda: self.open_new())
        self.search_btn.clicked.connect(lambda: self.search_paste())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ppaste"))
        self.groupBox.setTitle(_translate("MainWindow", "create paste"))
        self.plus_paste_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create new paste.</p></body></html>"))
        self.plus_paste_btn.setText(_translate("MainWindow", "+ paste"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Search box"))
        self.search_paste_lbl.setText(_translate("MainWindow", ""))
        self.search_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Search paste by entering the code.</p></body></html>"))
        self.search_btn.setText(_translate("MainWindow", "go to"))

    def open_new(self):
        self.editor_win = EditorWindow()
        self.editor_win.show()

    def search_paste(self):
        try:
            sql_connect = sqlite3.connect('database\pcode_data.db')
            sql_cursor = sql_connect.cursor()
            sql_request = "SELECT * FROM pcode_data WHERE pcode = ?"
            sql_value = self.search_paste_lbl.text(),
            sql_cursor.execute(sql_request, sql_value)

            if not sql_cursor.fetchone():
                print('No')
            else:
                self.editor_win = EditorWindow()
                self.editor_win.pcode_label.setText(self.search_paste_lbl.text())
                self.editor_win.pcode = self.search_paste_lbl.text()
                self.editor_win.change_file()
                self.editor_win.show()
            sql_cursor.close()
        except sqlite3.Error as error:
            print('[!] sqlite3 error:', error)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainMenu()
    ui.show()
    sys.exit(app.exec_())
