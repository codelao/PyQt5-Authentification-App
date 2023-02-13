import datetime
from login_window import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from PyQt5 import QtGui
from db import Database


class join_win(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.UI()
        self.connections()

    def appear(self):
        self.setWindowTitle('Registration')
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
        self.repeat_password_text = QLabel('Repeat password:')
        self.repeat_password = QLineEdit()
        self.join_button = QPushButton('Join')

        self.password.setEchoMode(QLineEdit.Password)
        self.repeat_password.setEchoMode(QLineEdit.Password)

        self.line = QVBoxLayout()
        self.line.addWidget(self.username_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.username, alignment=Qt.AlignCenter)
        self.line.addWidget(self.password_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.password, alignment=Qt.AlignCenter)
        self.line.addWidget(self.repeat_password_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.repeat_password, alignment=Qt.AlignCenter)
        self.line.addWidget(self.join_button, alignment=Qt.AlignCenter)
        self.setLayout(self.line)

    def connections(self):
        self.join_button.clicked.connect(self.click)

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
        self.save_repeat_password = self.repeat_password.text()
        if self.save_username != '' and self.save_password != '' and self.save_repeat_password != '':
            if len(self.save_username) <= 12 and len(self.save_username) >= 2 and len(self.save_password) <= 20 and len(self.save_password) >= 5:
                if self.save_username != self.save_password:
                    if self.save_password == self.save_repeat_password:
                        if not self.db.check_user(username=self.save_username):
                            self.today = datetime.datetime.today()
                            self.date = self.today.strftime("%m/%d/%Y")
                            self.db.add_userdata(username=self.save_username, password=self.save_password, join_date=self.date)
                            self.success = QMessageBox()
                            self.success.setWindowTitle('Alert')
                            self.success.setStyleSheet(self.stylesheet)
                            self.success.move(1200, 300)
                            self.success.setIcon(QMessageBox.Information)
                            self.success.setText('Successfully registered!\nGo to the log in window?')
                            self.success.setWindowFlags(Qt.WindowStaysOnTopHint)
                            self.success.setDefaultButton(QMessageBox.Ok)
                            self.success.buttonClicked.connect(self.login_click)
                            self.success.exec_()
                        else:
                            self.reg_error = QMessageBox()
                            self.reg_error.setWindowTitle('Alert')
                            self.reg_error.setStyleSheet(self.stylesheet)
                            self.reg_error.move(1200, 300)
                            self.reg_error.setIcon(QMessageBox.Information)
                            self.reg_error.setText('You\'re already registered\nGo to the log in window?')
                            self.reg_error.setWindowFlags(Qt.WindowStaysOnTopHint)
                            self.reg_error.setDefaultButton(QMessageBox.Ok)
                            self.reg_error.buttonClicked.connect(self.login_click)
                            self.reg_error.exec_()
                    else:
                        self.pass_error = QMessageBox()
                        self.pass_error.setWindowTitle('Alert')
                        self.pass_error.setStyleSheet(self.stylesheet)
                        self.pass_error.move(1200, 300)
                        self.pass_error.setIcon(QMessageBox.Information)
                        self.pass_error.setText('Passwords don\'t match\nTry again?')
                        self.pass_error.setWindowFlags(Qt.WindowStaysOnTopHint)
                        self.pass_error.setDefaultButton(QMessageBox.Ok)
                        self.pass_error.buttonClicked.connect(self.again_click)
                        self.pass_error.exec_()
                else:
                    self.data_error = QMessageBox()
                    self.data_error.setWindowTitle('Alert')
                    self.data_error.setStyleSheet(self.stylesheet)
                    self.data_error.move(1200, 300)
                    self.data_error.setIcon(QMessageBox.Information)
                    self.data_error.setText('Password can\'t be same with the username\nTry again?')
                    self.data_error.setWindowFlags(Qt.WindowStaysOnTopHint)
                    self.data_error.setDefaultButton(QMessageBox.Ok)
                    self.data_error.buttonClicked.connect(self.again_click)
                    self.data_error.exec_()
            else:
                self.characters_error = QMessageBox()
                self.characters_error.setWindowTitle('Alert')
                self.characters_error.setStyleSheet(self.stylesheet)
                self.characters_error.move(1200, 300)
                self.characters_error.setIcon(QMessageBox.Information)
                self.characters_error.setText('Invalid username or password given\nTry again?')
                self.characters_error.setWindowFlags(Qt.WindowStaysOnTopHint)
                self.characters_error.setDefaultButton(QMessageBox.Ok)
                self.characters_error.setDetailedText('Username must contain at least 2 characters and no more than '
                '12 characters\nPassword must contain at least 5 characters and no more than 20 characters'
                )
                self.characters_error.buttonClicked.connect(self.again_click)
                self.characters_error.exec_()
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

    def again_click(self):
        self.hide()
        self.show()

    def login_click(self):
        self.hide()
        self.lw = login_win()
        self.lw.show()