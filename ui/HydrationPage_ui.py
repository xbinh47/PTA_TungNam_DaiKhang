# Form implementation generated from reading ui file 'c:\Users\binhn\Documents\MindX\PTA\PTA02\PTA_TungNam_DaiKhang\ui\HydrationPage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.UpperBar = QtWidgets.QWidget(parent=self.centralwidget)
        self.UpperBar.setGeometry(QtCore.QRect(70, 10, 921, 61))
        self.UpperBar.setStyleSheet("border-radius:20px;\n"
"background-color:rgb(232, 232, 232);")
        self.UpperBar.setObjectName("UpperBar")
        self.label_6 = QtWidgets.QLabel(parent=self.UpperBar)
        self.label_6.setGeometry(QtCore.QRect(880, 20, 31, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("c:\\Users\\binhn\\Documents\\MindX\\PTA\\PTA02\\PTA_TungNam_DaiKhang\\ui\\../img/house-solid.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.UpperBar)
        self.label_7.setGeometry(QtCore.QRect(830, 20, 31, 31))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("c:\\Users\\binhn\\Documents\\MindX\\PTA\\PTA02\\PTA_TungNam_DaiKhang\\ui\\../img/bell-regular.svg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.bellButton = QtWidgets.QPushButton(parent=self.UpperBar)
        self.bellButton.setGeometry(QtCore.QRect(840, 20, 31, 31))
        self.bellButton.setStyleSheet("background-color:rgba(0,0,0)")
        self.bellButton.setText("")
        self.bellButton.setObjectName("bellButton")
        self.houseButton = QtWidgets.QPushButton(parent=self.UpperBar)
        self.houseButton.setGeometry(QtCore.QRect(880, 20, 31, 29))
        self.houseButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.houseButton.setStyleSheet("background-color:rgba(0,0,0)")
        self.houseButton.setText("")
        self.houseButton.setObjectName("houseButton")
        self.helpButton = QtWidgets.QPushButton(parent=self.UpperBar)
        self.helpButton.setGeometry(QtCore.QRect(740, 20, 93, 29))
        self.helpButton.setStyleSheet("font: 700 11pt \"Segoe UI\";\n"
"color:rgb(0, 0, 0)")
        self.helpButton.setObjectName("helpButton")
        self.logo_2 = QtWidgets.QLabel(parent=self.UpperBar)
        self.logo_2.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.logo_2.setStyleSheet("font: 700 10pt \"Segoe UI\";")
        self.logo_2.setText("")
        self.logo_2.setPixmap(QtGui.QPixmap("c:\\Users\\binhn\\Documents\\MindX\\PTA\\PTA02\\PTA_TungNam_DaiKhang\\ui\\../img/logo.png"))
        self.logo_2.setScaledContents(True)
        self.logo_2.setObjectName("logo_2")
        self.SideBar = QtWidgets.QWidget(parent=self.centralwidget)
        self.SideBar.setGeometry(QtCore.QRect(10, 10, 51, 581))
        self.SideBar.setStyleSheet("border-radius:10px;\n"
"background-color:rgb(70, 70, 70)")
        self.SideBar.setObjectName("SideBar")
        self.settingButton = QtWidgets.QPushButton(parent=self.SideBar)
        self.settingButton.setGeometry(QtCore.QRect(0, 520, 51, 41))
        self.settingButton.setAutoFillBackground(False)
        self.settingButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.settingButton.setText("")
        self.settingButton.setObjectName("settingButton")
        self.settingIcon = QtWidgets.QLabel(parent=self.SideBar)
        self.settingIcon.setGeometry(QtCore.QRect(0, 520, 51, 41))
        self.settingIcon.setText("")
        self.settingIcon.setPixmap(QtGui.QPixmap("c:\\Users\\binhn\\Documents\\MindX\\PTA\\PTA02\\PTA_TungNam_DaiKhang\\ui\\../img/gear-solid.svg"))
        self.settingIcon.setScaledContents(True)
        self.settingIcon.setObjectName("settingIcon")
        self.barButton = QtWidgets.QPushButton(parent=self.SideBar)
        self.barButton.setGeometry(QtCore.QRect(0, 470, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.barButton.setFont(font)
        self.barButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.barButton.setText("")
        self.barButton.setObjectName("barButton")
        self.barIcon = QtWidgets.QLabel(parent=self.SideBar)
        self.barIcon.setGeometry(QtCore.QRect(10, 470, 31, 31))
        self.barIcon.setText("")
        self.barIcon.setPixmap(QtGui.QPixmap("c:\\Users\\binhn\\Documents\\MindX\\PTA\\PTA02\\PTA_TungNam_DaiKhang\\ui\\../img/bars-solid.svg"))
        self.barIcon.setScaledContents(True)
        self.barIcon.setObjectName("barIcon")
        self.label_2 = QtWidgets.QLabel(parent=self.SideBar)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 51, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\binhn\\Documents\\MindX\\PTA\\PTA02\\PTA_TungNam_DaiKhang\\ui\\../img/decor.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 80, 451, 511))
        self.widget.setObjectName("widget")
        self.listBlog = QtWidgets.QListWidget(parent=self.widget)
        self.listBlog.setGeometry(QtCore.QRect(0, 30, 451, 481))
        self.listBlog.setStyleSheet("border-radius:10px")
        self.listBlog.setObjectName("listBlog")
        self.searchBar = QtWidgets.QLineEdit(parent=self.widget)
        self.searchBar.setGeometry(QtCore.QRect(0, 0, 451, 26))
        self.searchBar.setStyleSheet("border-radius:10px")
        self.searchBar.setObjectName("searchBar")
        self.widget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(540, 80, 431, 511))
        self.widget_2.setObjectName("widget_2")
        self.TitleBar = QtWidgets.QLineEdit(parent=self.widget_2)
        self.TitleBar.setGeometry(QtCore.QRect(0, 0, 431, 26))
        self.TitleBar.setAccessibleName("")
        self.TitleBar.setStyleSheet("border-radius:10px")
        self.TitleBar.setObjectName("TitleBar")
        self.BlogEdit = QtWidgets.QTextEdit(parent=self.widget_2)
        self.BlogEdit.setGeometry(QtCore.QRect(0, 30, 431, 421))
        self.BlogEdit.setObjectName("BlogEdit")
        self.blogBtn = QtWidgets.QPushButton(parent=self.widget_2)
        self.blogBtn.setGeometry(QtCore.QRect(10, 460, 401, 51))
        self.blogBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.blogBtn.setStyleSheet("font: 700 12pt \"Segoe UI\";\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 83);\n"
"border-radius:15px")
        self.blogBtn.setObjectName("blogBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.helpButton.setText(_translate("MainWindow", "Help?"))
        self.searchBar.setPlaceholderText(_translate("MainWindow", "Search Blog..."))
        self.TitleBar.setPlaceholderText(_translate("MainWindow", "Edit Blog Title:"))
        self.blogBtn.setText(_translate("MainWindow", "Publish"))