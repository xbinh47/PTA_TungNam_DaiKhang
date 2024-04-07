from PyQt6 import QtWidgets 
from PyQt6.QtCore import QTimer,QTime
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QListWidget, QListWidgetItem, QDialog, QPushButton, QTextEdit, QVBoxLayout
from PyQt6 import uic
import sys
import sqlite3
import plyer
from plyer import notification #used for getting notify in the corner of the laptop, not QMessageBox
from custom_widget.CustomListItem import CustomListItemWidget
#CLASS THOSE PAGES
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
        
        query = f"SELECT * FROM USER WHERE email = ('{email}')"
        result = query_db(query)

        if len(result) > 0:
            err_box.setText("This email had been used for an another account!")
            err_box.exec()
            return
        
        query = f"INSERT INTO USER (username, password, email) VALUES ('{self.name}', '{password}', '{email}')"
        print(query)
        execute_db(query)

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
    
    def checkLogin(self):
        email = self.txtEmail.text()
        password = self.txtPass.text()

        if not email:
            err_box.setText("Please enter your email!")
            err_box.exec()
            return

        if not password:
            err_box.setText("Please enter your password!")
            err_box.exec()
            return

        query = f"SELECT * FROM USER WHERE email ='{email}' and password='{password}'" #query select
        result = query_db(query)
        self.name = result[0][1]

        if len(result) == 0:
            err_box.setText("Invalid Username or Password!")
            err_box.exec()
            return
        
        success_box.setText("Succesfully Login!")
        success_box.exec()
        self.showMainPage()

    def showRegisterPage(self):
        registerPage.show()
        self.close()

    def showMainPage(self):
        mainPage.setUsername(self.name)
        mainPage.show()
        self.close()

class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        uic.loadUi("ui/main.ui", self)
        self.name = ""
        self.hydrationButton.clicked.connect(self.showHydration)
        self.activityButton.clicked.connect(self.showActivity)
        self.drinksButton.clicked.connect(self.showDrinks)
        self.btn_reminder.clicked.connect(self.showReminder)
        self.timer = QTimer(self)
        self.startAutoReminder() #start the timer 
        self.timer.timeout.connect(self.autoReminder)

    def autoReminder(self):
        notification.notify(
        title='Hydration Reminder',
        message='Remember to drink water!',
        app_name='Summery',
        # app_icon='C:\\Users\\ADMIN\\Documents\\GitHub\\PTA_TungNam_DaiKhang\\img\\logo.png'
        )

    def startAutoReminder(self):
        hour = 60 * 1000 # milliseconds ==> currently sets for 1 minute
        self.timer.start(hour)
    
    def setUsername(self, name):
        self.name = name
        self.txtUsername.setText(name)

    def showHydration(self):
        hydrationPage.show()
        hydrationPage.loadBlog()
        self.close()

    def showActivity(self):
        activityPage.show()
        self.close()    

    def showDrinks(self):
        drinksPage.show()
        self.close()

    def showReminder(self):
        reminderPage.show()
        self.close()

class Hydration(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        uic.loadUi("ui/HydrationPage.ui", self)
        self.name = ""
        self.listBlog = self.findChild(QListWidget, 'listBlog')
        self.houseButton.clicked.connect(self.showMainPage)
        self.blogBtn.clicked.connect(self.addBlog)
        self.listBlog.itemClicked.connect(self.onItemClicked)
        self.searchBar.textChanged.connect(self.search)
        self.loadBlog()

    def search(self):
        search_title = self.searchBar.text()
        query = f"SELECT * FROM BLOG_Hydration WHERE title like '%{search_title}%'" # %% check all txt in title / otherwise only checking 1st txt
        result = query_db(query)
        self.listBlog.clear()
        for blog in result:
            item = QListWidgetItem(self.listBlog)
            self.listBlog.addItem(item)
            custom_widget = CustomListItemWidget(blog[0], blog[1], blog[2])
            custom_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 10px; padding: 10px;")
            self.listBlog.setItemWidget(item, custom_widget)
            item.setSizeHint(custom_widget.sizeHint()) 

    def onItemClicked(self, item):
        widget = self.listBlog.itemWidget(item)
        title = widget.title
        content = widget.content
        dialog = Dialog(title, content)
        dialog.exec()

    def loadBlog(self):
        query = "SELECT * FROM BLOG_Hydration"
        result = query_db(query)
        self.listBlog.clear()
        for blog in result:
            item = QListWidgetItem(self.listBlog)
            self.listBlog.addItem(item)
            custom_widget = CustomListItemWidget(blog[0], blog[1], blog[2])
            custom_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 10px; padding: 10px;")
            self.listBlog.setItemWidget(item, custom_widget)
            item.setSizeHint(custom_widget.sizeHint())

    def addBlog(self):
        title = self.TitleBar.text()
        content = self.BlogEdit.toPlainText()
        if title == "":
            err_box.setText("Please enter the title!")
            err_box.exec()
            return
        if content == "":
            err_box.setText("Please enter the content!")
            err_box.exec()
            return
        
        query = f"INSERT INTO BLOG_Hydration (title, content) VALUES ('{title}', '{content}')"
        execute_db(query)
        success_box.setText("Blog added successfully!")
        success_box.exec()
        self.resetBlog()
        self.loadBlog()

    def resetBlog(self):
        self.TitleBar.setText("")
        self.BlogEdit.setText("")

    def showMainPage(self):
        mainPage.show()
        self.close()

class Activity(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        uic.loadUi("ui/ActivityPage.ui", self)
        self.name = ""
        self.listBlog = self.findChild(QListWidget, 'listBlog')
        self.houseButton.clicked.connect(self.showMainPage)
        self.blogBtn.clicked.connect(self.addBlog)
        self.listBlog.itemClicked.connect(self.onItemClicked)
        self.searchBar.textChanged.connect(self.search)
        self.loadBlog()

    def search(self):
        search_title = self.searchBar.text()
        query = f"SELECT * FROM BLOG_Activity WHERE title like '%{search_title}%'" 
        result = query_db(query)
        self.listBlog.clear()
        for blog in result:
            item = QListWidgetItem(self.listBlog)
            self.listBlog.addItem(item)
            custom_widget = CustomListItemWidget(blog[0], blog[1], blog[2])
            custom_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 10px; padding: 10px;")
            self.listBlog.setItemWidget(item, custom_widget)
            item.setSizeHint(custom_widget.sizeHint()) 

    def onItemClicked(self, item):
        widget = self.listBlog.itemWidget(item)
        title = widget.title
        content = widget.content
        dialog = Dialog(title, content)
        dialog.exec()

    def loadBlog(self):
        query = "SELECT * FROM BLOG_Activity"
        result = query_db(query)
        self.listBlog.clear()
        for blog in result:
            item = QListWidgetItem(self.listBlog)
            self.listBlog.addItem(item)
            custom_widget = CustomListItemWidget(blog[0], blog[1], blog[2])
            custom_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 10px; padding: 10px;")
            self.listBlog.setItemWidget(item, custom_widget)
            item.setSizeHint(custom_widget.sizeHint())

    def addBlog(self):
        title = self.TitleBar.text()
        content = self.BlogEdit.toPlainText()
        if title == "":
            err_box.setText("Please enter the title!")
            err_box.exec()
            return
        if content == "":
            err_box.setText("Please enter the content!")
            err_box.exec()
            return
        query = f"INSERT INTO BLOG_Activity (title, content) VALUES ('{title}', '{content}')"
        execute_db(query)
        success_box.setText("Blog added successfully!")
        success_box.exec()
        self.resetBlog()
        self.loadBlog()

    def resetBlog(self):
        self.TitleBar.setText("")
        self.BlogEdit.setText("")

    def showMainPage(self):
        mainPage.show()
        self.close()

class Drinks(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        uic.loadUi("ui/DrinksPage.ui", self)
        self.name = ""
        self.listBlog = self.findChild(QListWidget, 'listBlog')
        self.houseButton.clicked.connect(self.showMainPage)
        self.blogBtn.clicked.connect(self.addBlog)
        self.listBlog.itemClicked.connect(self.onItemClicked)
        self.searchBar.textChanged.connect(self.search)
        self.loadBlog()

    def search(self):
        search_title = self.searchBar.text()
        query = f"SELECT * FROM BLOG_Activity WHERE title like '%{search_title}%'" 
        result = query_db(query)
        self.listBlog.clear()
        for blog in result:
            item = QListWidgetItem(self.listBlog)
            self.listBlog.addItem(item)
            custom_widget = CustomListItemWidget(blog[0], blog[1], blog[2])
            custom_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 10px; padding: 10px;")
            self.listBlog.setItemWidget(item, custom_widget)
            item.setSizeHint(custom_widget.sizeHint())         

    def onItemClicked(self, item):
        widget = self.listBlog.itemWidget(item)
        title = widget.title
        content = widget.content
        dialog = Dialog(title, content)
        dialog.exec()

    def loadBlog(self):
        query = "SELECT * FROM BLOG_Drinks"
        result = query_db(query)
        self.listBlog.clear()
        for blog in result:
            item = QListWidgetItem(self.listBlog)
            self.listBlog.addItem(item)
            custom_widget = CustomListItemWidget(blog[0], blog[1], blog[2])
            custom_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 10px; padding: 10px;")
            self.listBlog.setItemWidget(item, custom_widget)
            item.setSizeHint(custom_widget.sizeHint())

    def addBlog(self):
        title = self.TitleBar.text()
        content = self.BlogEdit.toPlainText()
        if title == "":
            err_box.setText("Please enter the title!")
            err_box.exec()
            return
        if content == "":
            err_box.setText("Please enter the content!")
            err_box.exec()
            return
        query = f"INSERT INTO BLOG_Drinks (title, content) VALUES ('{title}', '{content}')"
        execute_db(query)
        success_box.setText("Blog added successfully!")
        success_box.exec()
        self.resetBlog()
        self.loadBlog()

    def resetBlog(self):
        self.TitleBar.setText("")
        self.BlogEdit.setText("")

    def showMainPage(self):
        mainPage.show()
        self.close()

class Reminder(QMainWindow):
    def __init__(self):
        super().__init__() 
        uic.loadUi("ui/ReminderPage.ui", self)
        self.name = ""
        self.houseBtn.clicked.connect(self.showMainPage)
        self.reminderBtn.clicked.connect(self.setReminder)
        self.reminder_time = None  # Initialize reminder_time attribute
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.checkTime)  # Connect the timer timeout to checkTime method
        self.timer.start(1000)  # Start the timer to check every second

    def showMainPage(self):
        mainPage.show()
        self.close()
    
    def setReminder(self):
        self.reminder_time = self.timeReminder.time().toString("hh:mm")  # Get the reminder time in string format
        self.reminder_message = self.txtReminder.text()  # Get the reminder message
        success_box.setText("Reminder set successfully!")
        success_box.exec()
        self.timer.start()

    def checkTime(self):
        if self.reminder_time is not None:
            current_time = QTime.currentTime().toString("hh:mm")  # Get the current time in string format
            if current_time == self.reminder_time:
                notification.notify(
                    title='Reminder',
                    message=self.reminder_message,
                    app_name = 'Summery',
                    timeout=10,  # Timeout for the notification in seconds ==> 10 secs
                )
                self.timer.stop()
                self.reminder_time = None
                self.reminder_message = None

class Dialog(QDialog):
    def __init__(self, title, text):
        super().__init__()

        self.setWindowTitle(title)
        self.setLayout(QVBoxLayout())

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)  # Make the text read-only
        self.textEdit.setText(text)
        self.layout().addWidget(self.textEdit)

        closeButton = QPushButton("Close")
        closeButton.clicked.connect(self.close)
        self.layout().addWidget(closeButton)

#IMPORTANT STUFF
if __name__ == '__main__':
    sqliteConnection = sqlite3.connect('data/data.db')
    def execute_db(query):
        cusor = sqliteConnection.cursor()
        cusor.execute(query)
        sqliteConnection.commit()
        cusor.close()

    def query_db(query):
        cursor = sqliteConnection.cursor()
        cursor.execute(query)
        result = cursor.fetchall() #check if the result was in db(in list)
        cursor.close()
        return result
    
    app = QtWidgets.QApplication(sys.argv)

    loginPage = Login() #set page
    loginPage.show()
    registerPage = Register()
    mainPage = MainPage()
    hydrationPage = Hydration()
    activityPage = Activity()
    drinksPage = Drinks()
    reminderPage = Reminder()

    err_box = QMessageBox()
    err_box.setWindowTitle("Error.")
    err_box.setIcon(QMessageBox.Icon.Warning)
    # err_box.setStyleSheet()
    
    success_box = QMessageBox()
    success_box.setWindowTitle("Success!")
    success_box.setIcon(QMessageBox.Icon.Information)
    # success_box.setStyleSheet()
    app.exec()
