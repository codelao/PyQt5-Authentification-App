from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QMessageBox
from PyQt5 import QtGui
from db import Database


class profile_win(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.UI()
        self.connections()

    def appear(self):
        self.setWindowTitle('Profile')
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
        self.resize(500, 250)
        self.move(400, 300)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

    def UI(self):
        self.username_text = QLabel('Enter your username to view profile info:')
        self.username = QLineEdit()
        self.view_button = QPushButton('View')

        self.line = QVBoxLayout()
        self.line.addWidget(self.username_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.username, alignment=Qt.AlignCenter)
        self.line.addWidget(self.view_button, alignment=Qt.AlignCenter)
        self.setLayout(self.line)

    def connections(self):
        self.view_button.clicked.connect(self.click)

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
        if self.save_username != '':
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
                self.success = QMessageBox()
                self.success.setWindowTitle('Alert')
                self.success.setStyleSheet(self.stylesheet)
                self.success.move(1200, 300)
                self.success.setIcon(QMessageBox.Information)
                self.success.setText('Profile information:'
                '\nUsername: ' + self.save_username +
                '\nJoin date: ' + self.db.get_user_join_date(username=self.save_username)
                )
                self.success.setWindowFlags(Qt.WindowStaysOnTopHint)
                self.success.setDefaultButton(QMessageBox.Ok)
                self.success.buttonClicked.connect(self.again_click)
                self.success.exec_()
        else:
            self.username_error = QMessageBox()
            self.username_error.setWindowTitle('Alert')
            self.username_error.setStyleSheet(self.stylesheet)
            self.username_error.move(1200, 300)
            self.username_error.setIcon(QMessageBox.Information)
            self.username_error.setText('Username wasn\'t entered\nTry again?')
            self.username_error.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.username_error.setDefaultButton(QMessageBox.Ok)
            self.username_error.buttonClicked.connect(self.again_click)
            self.username_error.exec_()

    def again_click(self):
        self.hide()
        self.show()