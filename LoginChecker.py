# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserPassWord.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 339)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.UsernameLabel.setGeometry(QtCore.QRect(70, 0, 81, 31))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.UsernameLabel.setFont(font)
        self.UsernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UsernameLabel.setObjectName("UsernameLabel")
        self.PassWordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PassWordLabel.setGeometry(QtCore.QRect(70, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.PassWordLabel.setFont(font)
        self.PassWordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PassWordLabel.setObjectName("PassWordLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 201, 41))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.Correct = QtWidgets.QLabel(self.centralwidget)
        self.Correct.setGeometry(QtCore.QRect(300, 20, 201, 111))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(72)
        self.Correct.setFont(font)
        self.Correct.setAlignment(QtCore.Qt.AlignCenter)
        self.Correct.setProperty("Color", QtGui.QColor(0, 255, 0))
        self.Correct.setObjectName("Correct")
        self.Wrong = QtWidgets.QLabel(self.centralwidget)
        self.Wrong.setGeometry(QtCore.QRect(300, 140, 211, 121))
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(72)
        self.Wrong.setFont(font)
        self.Wrong.setAlignment(QtCore.Qt.AlignCenter)
        self.Wrong.setProperty("Color", QtGui.QColor(0, 255, 0))
        self.Wrong.setObjectName("Wrong")
        self.Uesrname = QtWidgets.QLineEdit(self.centralwidget)
        self.Uesrname.setGeometry(QtCore.QRect(20, 29, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Uesrname.setFont(font)
        self.Uesrname.setObjectName("Uesrname")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(20, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Correct.hide()
        self.Wrong.hide()

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.Check)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Check(self):

        if self.Uesrname.text() == "test" and self.Password.text() == "test":
            app.processEvents()
            self.ShowMessage("اطلاع","نام کاربري و رمز عبور شما درست است",QMessageBox.Information)
        else:
            app.processEvents()
            self.ShowMessage("هشدار","رمز و يا نام کاربري شما نادرست است",QMessageBox.Critical)

    def ShowMessage(self,title,message,icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LoginCheker"))
        self.UsernameLabel.setText(_translate("MainWindow", "نام کاربری"))
        self.PassWordLabel.setText(_translate("MainWindow", "رمز عبور"))
        self.pushButton.setText(_translate("MainWindow", "انجام"))
        self.Correct.setText(_translate("MainWindow", "درست"))
        self.Wrong.setText(_translate("MainWindow", "نادرست"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
