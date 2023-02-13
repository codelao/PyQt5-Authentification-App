from join_window import *
from login_window import *
from profile_window import *
from delete_window import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5 import QtGui


class first_win(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.UI()
        self.connections()

    def appear(self):
        self.setWindowTitle('Welcome')
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
        '''
        )
        self.resize(500, 250)
        self.move(400, 300)
        #self.setWindowIcon(QtGui.QIcon('logo.png')) - optional

    def UI(self):
        self.text = QLabel('Welcome')
        self.join_button = QPushButton('Join')
        self.login_button = QPushButton('Log in')
        self.profile_button = QPushButton('My profile')
        self.delete_button = QPushButton('Delete account')

        self.line = QVBoxLayout()
        self.line.addWidget(self.text, alignment=Qt.AlignCenter)
        
        self.line2 = QHBoxLayout()
        self.line2.addWidget(self.join_button, alignment=Qt.AlignCenter)
        self.line2.addWidget(self.login_button, alignment=Qt.AlignCenter)

        self.line3 = QHBoxLayout()
        self.line3.addWidget(self.profile_button, alignment=Qt.AlignCenter)
        self.line3.addWidget(self.delete_button, alignment=Qt.AlignCenter)
        self.line.addLayout(self.line2)
        self.line.addLayout(self.line3)
        self.setLayout(self.line)

    def connections(self):
        self.join_button.clicked.connect(self.join_click)
        self.login_button.clicked.connect(self.login_click)
        self.profile_button.clicked.connect(self.profile_click)
        self.delete_button.clicked.connect(self.delete_click)

    def join_click(self):
        self.close()
        self.jw = join_win()
        self.jw.show()

    def login_click(self):
        self.close()
        self.lw = login_win()
        self.lw.show()

    def profile_click(self):
        self.close()
        self.pw = profile_win()
        self.pw.show()

    def delete_click(self):
        self.close()
        self.dw = delete_win()
        self.dw.show()


if __name__ == '__main__':
    app = QApplication([])
    mw = first_win()
    mw.show()
    app.exec_()