from PyQt6 import QtWidgets 
from PyQt6.QtWidgets import QMessageBox,QPushButton,QLineEdit
from PyQt6 import uic
import sys

import sqlite3

class Register(QtWidgets.QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("register.ui", self) #Create and load file ui
        self.name = ""
        self.btnSignUp.clicked.connect(self.Register)
        self.btnLogin.clicked.connect(self.showLoginPage)

    def Register(self):
        self.name = self.txtFullName.text()
        email = self.txtEmail.text()
        password = self.txtPassword.text()

        if not self.name:
            msg_box.setText("Please enter your name!")
            msg_box.exec()
            return
        if not email:
            msg_box.setText("Please enter your email!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter your password!")
            msg_box.exec()
            return
        
        #Success
        success_box.setText("Succesfully Signed Up!")
        success_box.exec()
        self.close()

    def showLoginPage(self):
        loginPage.show()
        self.close()

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() #call out the characters of ParentClass
        uic.loadUi("login.ui", self) #Create and load the file ui
        self.name = ""
        self.btnLogin.clicked.connect(self.check_login)
        self.btn_register.clicked.connect(self.show_register)

    def check_login(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()

        if not email:
            msg_box.setText("Please enter your email!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Please enter your password!")
            msg_box.exec()
            return

        if email == "trandaikhang9510@gmail.com" and password == "AdminKhang01": #check if infor are correct
            success_box.setText("Succesfully Logged in!")
            success_box.exec()
            self.close()
        else:
            success_box.setText("Wrong Email or Password.")
            success_box.exec()
            return
        
    def show_register(self):
        registerPage.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    loginPage = Login()
    loginPage.show()
    registerPage = Register()

    msg_box = QMessageBox()
    msg_box.setWindowTitle("Error.")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    # msg_box.setStyleSheet()
    
    success_box = QMessageBox()
    success_box.setWindowTitle("Success!")
    success_box.setIcon(QMessageBox.Icon.Information)
    # success_box.setStyleSheet
    app.exec()