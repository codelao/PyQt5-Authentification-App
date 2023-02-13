from join_window import *
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QLineEdit
from PyQt5 import QtGui
from db import Database


class delete_win(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.UI()
        self.connections()

    def appear(self):
        self.setWindowTitle('Delete')
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
        self.time = QTime(0, 0, 30)
        self.time_count = QLabel(self.time.toString("hh:mm:ss"))
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_start)
        self.timer.start(1000)
        self.timer_text = QLabel('You have 30 seconds to delete your account')
        self.username_text = QLabel('Username:')
        self.username = QLineEdit()
        self.password_text = QLabel('Password:')
        self.password = QLineEdit()
        self.repeat_password_text = QLabel('Repeat password:')
        self.repeat_password = QLineEdit()
        self.delete_button = QPushButton('Delete')

        self.password.setEchoMode(QLineEdit.Password)
        self.repeat_password.setEchoMode(QLineEdit.Password)

        self.line = QVBoxLayout()
        self.line.addWidget(self.timer_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.time_count, alignment=Qt.AlignCenter)
        self.line.addWidget(self.username_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.username, alignment=Qt.AlignCenter)
        self.line.addWidget(self.password_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.password, alignment=Qt.AlignCenter)
        self.line.addWidget(self.repeat_password_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.repeat_password, alignment=Qt.AlignCenter)
        self.line.addWidget(self.delete_button, alignment=Qt.AlignCenter)
        self.setLayout(self.line)

    def connections(self):
        self.delete_button.clicked.connect(self.click)

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
            if self.save_password == self.save_repeat_password:
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
                        self.success.setText('Are you sure you want to delete your account?')
                        self.success.setWindowFlags(Qt.WindowStaysOnTopHint)
                        self.success.setDefaultButton(QMessageBox.Ok)
                        self.success.buttonClicked.connect(self.delete_click)
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
                self.match_error = QMessageBox()
                self.match_error.setWindowTitle('Alert')
                self.match_error.setStyleSheet(self.stylesheet)
                self.match_error.move(1200, 300)
                self.match_error.setIcon(QMessageBox.Information)
                self.match_error.setText('Passwords don\'t match\nTry again?')
                self.match_error.setWindowFlags(Qt.WindowStaysOnTopHint)
                self.match_error.setDefaultButton(QMessageBox.Ok)
                self.match_error.buttonClicked.connect(self.again_click)
                self.match_error.exec_()
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

    def timer_start(self):
        global time
        self.time = self.time.addSecs(-1)
        self.time_count.setText(self.time.toString('hh:mm:ss'))
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
            self.close()

    def again_click(self):
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.close()
        else:
            self.hide()
            self.show()

    def delete_click(self):
        if self.time.toString('hh:mm:ss') == '00:00:00':
            self.close()
        else:
            self.db.delete_user(username=self.save_username)
            self.success.close()
            self.delete_success = QMessageBox()
            self.delete_success.setWindowTitle('Alert')
            self.delete_success.setStyleSheet(self.stylesheet)
            self.delete_success.move(1200, 300)
            self.delete_success.setIcon(QMessageBox.Information)
            self.delete_success.setText('User deleted successfully')
            self.delete_success.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.delete_success.setDefaultButton(QMessageBox.Ok)
            self.delete_success.buttonClicked.connect(self.delete_success_click)
            self.delete_success.exec_()

    def delete_success_click(self):
        self.close()