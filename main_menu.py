from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from code_editor import EditorWindow


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"gridline-color: rgb(71, 71, 71);\n"
"selection-background-color: rgb(252, 186, 3);\n"
"border-color: rgb(118, 118, 118);\n"
"color: rgb(220, 220, 220);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 411, 91))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.plus_paste_btn = QtWidgets.QPushButton(self.groupBox)
        self.plus_paste_btn.setGeometry(QtCore.QRect(20, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plus_paste_btn.setFont(font)
        self.plus_paste_btn.setObjectName("plus_paste_btn")
        self.search_btn = QtWidgets.QPushButton(self.groupBox)
        self.search_btn.setGeometry(QtCore.QRect(220, 30, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.plus_paste_btn.clicked.connect(lambda: self.open_new())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ppaste"))
        self.plus_paste_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Create new paste.</p></body></html>"))
        self.plus_paste_btn.setText(_translate("MainWindow", "+ paste"))
        self.search_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Search paste by entering the code.</p></body></html>"))
        self.search_btn.setText(_translate("MainWindow", "search paste"))

    def open_new(self):
        self.editor_win = EditorWindow()
        self.editor_win.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())

