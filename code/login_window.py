from last_window import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from PyQt5 import QtGui
from db import Database


class login_win(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.UI()
        self.connections()

    def appear(self):
        self.setWindowTitle('Log in')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''
        QWidget{
            background-color: #04202C
        }
        QLabel{
            color: #C9D1C8;
            font: bold 20px
        }
        QPushButton{
            color: #C9D1C8;
            font: bold 14px;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: #5B7065;
            font: bold 14px;
            min-width: 10em;
            padding: 6px
        }
        QPushButton:pressed{
            background-color: #5B7065
        }
        QLineEdit{
            border: 5px solid #5B7065;
            font: bold 20px;
            color: #C9D1C8
        }
        '''
        )
        self.resize(700, 450)
        self.move(400, 300)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

    def UI(self):
        self.username_text = QLabel('Username:')
        self.username = QLineEdit()
        self.password_text = QLabel('Password:')
        self.password = QLineEdit()
        self.login_button = QPushButton('Log in')

        self.password.setEchoMode(QLineEdit.Password)

        self.line = QVBoxLayout()
        self.line.addWidget(self.username_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.username, alignment=Qt.AlignCenter)
        self.line.addWidget(self.password_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.password, alignment=Qt.AlignCenter)
        self.line.addWidget(self.login_button, alignment=Qt.AlignCenter)
        self.setLayout(self.line)

    def connections(self):
        self.login_button.clicked.connect(self.click)

    def click(self):
        self.stylesheet = '''
        QMessageBox{
            background-color: #04202C
        }
        QLabel{
            color: #C9D1C8;
            font: bold 20px
        }
        QPushButton{
            color: #C9D1C8;
            font: bold 14px;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: #5B7065;
            font: bold 14px;
            min-width: 10em;
            padding: 6px
        }
        QPushButton:pressed{
            background-color: #5B7065
        }
        '''
        self.db = Database('usersdata.db')
        self.save_username = self.username.text()
        self.save_password = self.password.text()
        if self.save_username != '' and self.save_password != '':
            if not self.db.check_user(username=self.save_username):
                self.user_error = QMessageBox()
                self.user_error.setWindowTitle('Alert')
                self.user_error.setStyleSheet(self.stylesheet)
                self.user_error.move(1200, 300)
                self.user_error.setIcon(QMessageBox.Information)
                self.user_error.setText('User not found\nTry again?')
                self.user_error.setWindowFlags(Qt.WindowStaysOnTopHint)
                self.user_error.setDefaultButton(QMessageBox.Ok)
                self.user_error.buttonClicked.connect(self.again_click)
                self.user_error.exec_()
            else:
                self.check_pass = self.db.get_user_password(username=self.save_username)
                if self.save_password == self.check_pass:
                    self.success = QMessageBox()
                    self.success.setWindowTitle('Alert')
                    self.success.setStyleSheet(self.stylesheet)
                    self.success.move(1200, 300)
                    self.success.setIcon(QMessageBox.Information)
                    self.success.setText('Successfully loged in!\nGo to the next window?')
                    self.success.setWindowFlags(Qt.WindowStaysOnTopHint)
                    self.success.setDefaultButton(QMessageBox.Ok)
                    self.success.buttonClicked.connect(self.continue_click)
                    self.success.exec_()
                else:
                    self.pass_error = QMessageBox()
                    self.pass_error.setWindowTitle('Alert')
                    self.pass_error.setStyleSheet(self.stylesheet)
                    self.pass_error.move(1200, 300)
                    self.pass_error.setIcon(QMessageBox.Information)
                    self.pass_error.setText('Incorrect password\nTry again?')
                    self.pass_error.setWindowFlags(Qt.WindowStaysOnTopHint)
                    self.pass_error.setDefaultButton(QMessageBox.Ok)
                    self.pass_error.buttonClicked.connect(self.again_click)
                    self.pass_error.exec_()
        else:
            self.lines_error = QMessageBox()
            self.lines_error.setWindowTitle('Alert')
            self.lines_error.setStyleSheet(self.stylesheet)
            self.lines_error.move(1200, 300)
            self.lines_error.setIcon(QMessageBox.Information)
            self.lines_error.setText('Not all lines are filled in\nTry again?')
            self.lines_error.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.lines_error.setDefaultButton(QMessageBox.Ok)
            self.lines_error.buttonClicked.connect(self.again_click)
            self.lines_error.exec_()

    def continue_click(self):
        self.hide()
        self.lw = last_win()
        self.lw.show()

    def again_click(self):
        self.hide()
        self.show()