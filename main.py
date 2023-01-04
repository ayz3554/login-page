import sys
import os
import hashlib

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class WelcomeScreen(QDialog):

    def __init__(self):
        super(WelcomeScreen, self).__init__()

        logMenuPath = os.path.dirname(os.path.abspath(__file__))
        logMenu_ui_file = os.path.join(logMenuPath, 'loginMenu.ui')

        if not os.path.exists(logMenu_ui_file):
            print("File error: {}".format(logMenu_ui_file))
        else:
            loadUi(logMenu_ui_file, self)

        self.login.clicked.connect(self.gotologin)
        self.signup.clicked.connect(self.gotosignup)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotosignup(self):
        signup = SingupScreen()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class LoginScreen(QDialog):

    def __init__(self):
        super(LoginScreen, self).__init__()

        logScreenPath = os.path.dirname(os.path.abspath(__file__))
        log_ui_file = os.path.join(logScreenPath, 'loginGraphics.ui')

        loadUi(log_ui_file, self)

        self.LEPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login.clicked.connect(self.login_function)

    def login_function(self):
        username = self.LELoginInput.text()
        password = self.LEPasswordInput.text()

        if len(username) == 0 or len(password) == 0:
            self.error.setText('Wpisz poprawne dane!')

        logHashedPassword = hashlib.md5(password.encode()).hexdigest()

        originalData = username + ';' + logHashedPassword

        dataFilePath = r'Data/'
        fullDataFilePath = os.path.join(dataFilePath, 'passData.txt')

        realData = open(fullDataFilePath, 'r')

        with realData as file:
            allData = username + ';' + logHashedPassword

            if allData == originalData:
                self.success.setText('Zalogowałeś się.')
            else:
                self.error.setText('Wpisz poprawne dane!')


class SingupScreen(QDialog):

    def __init__(self):
        super(SingupScreen, self).__init__()

        signScreenPath = os.path.dirname(os.path.abspath(__file__))
        sign_ui_file = os.path.join(signScreenPath, 'signupGraphics.ui')

        loadUi(sign_ui_file, self)

        self.LESetPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LEConfirmPasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)

        self.signup.clicked.connect(self.signup_function)

    def signup_function(self):
        username = self.LESetLoginInput.text()
        password = self.LESetPasswordInput.text()
        confirmPassword = self.LEConfirmPasswordInput.text()

        allData = username + password + confirmPassword

        if confirmPassword != password:
            self.error.setText('Podane hasła są różne')
        elif len(allData) != 0:
            self.succes.setText('Pomyślnie stworzono konto')


        signHashedPassword = hashlib.md5(password.encode()).hexdigest()

        dataFilePath = r'Data/'
        fullDataFilePath = os.path.join(dataFilePath, 'passData.txt')
        signupData = open(fullDataFilePath, "w")

        with signupData as file:
            signupData.write(username + ';' + signHashedPassword)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    welcome = WelcomeScreen()

    widget = QStackedWidget()
    widget.addWidget(welcome)

    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)

    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print('Exiting...')
