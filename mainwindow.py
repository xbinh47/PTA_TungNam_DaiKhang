from PyQt6 import QtWidgets 
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import uic
import sys
import sqlite3

class Register(QtWidgets.QMainWindow):
    def __init__ (self):
        super().__init__()
        uic.loadUi("ui/register.ui", self)
        self.name = ""
        self.btnSignUp.clicked.connect(self.register)
        self.btnLogin.clicked.connect(self.showLoginPage)

    def register(self):
        self.name = self.txtname.text()
        email = self.txtEmail.text()
        password = self.txtPass.text()
        confirm_pass = self.txtConfirmPass.text()

        if not self.name:
            err_box.setText("Please enter your name!")
            err_box.exec()
            return 

        if not email:
            err_box.setText("Please enter your email!")
            err_box.exec() 
            return 

        if not password:
            err_box.setText("Please enter your password!")
            err_box.exec()
            return 
        
        if not confirm_pass:
            err_box.setText("Please enter your confirmed password!")
            err_box.exec() 
            return 

        if password != confirm_pass:
            err_box.setText("Password and Confirm Password not match!")
            err_box.exec()
            return 
        
        query = f"INSERT INTO USER (username, password, email) VALUES ('{self.name}', '{password}', '{email}')"
        print(query)
        insert_db(query)
        success_box.setText("Register Successfully!")
        loginPage.show()
        self.close()

    def showLoginPage(self):
        loginPage.show()
        self.close()

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() #call out the characters of ParentClass
        uic.loadUi("ui/login.ui", self) #Create and load the file ui
        self.name = ""
        self.btn_login.clicked.connect(self.checkLogin)
        self.btn_register.clicked.connect(self.showRegisterPage)
    
    def checkLogin():
        email
        password

    def showRegisterPage(self):
        registerPage.show()
        self.close()
    
if __name__ == '__main__':
    sqliteConnection = sqlite3.connect('data/data.db')
    def insert_db(query):
        cusor = sqliteConnection.cursor()
        cusor.execute(query)
        sqliteConnection.commit()
        cusor.close()

    def query_db(query):
        return
    
    app = QtWidgets.QApplication(sys.argv)

    loginPage = Login()
    loginPage.show()
    registerPage = Register()

    err_box = QMessageBox()
    err_box.setWindowTitle("Error.")
    err_box.setIcon(QMessageBox.Icon.Warning)
    # msg_box.setStyleSheet()
    
    success_box = QMessageBox()
    success_box.setWindowTitle("Success!")
    success_box.setIcon(QMessageBox.Icon.Information)
    # success_box.setStyleSheet
    app.exec()
    
