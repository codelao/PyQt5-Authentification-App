from profile_window import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5 import QtGui


class last_win(QWidget):
    def __init__(self):
        super().__init__()
        self.appear()
        self.UI()
        self.connections()

    def appear(self):
        self.setWindowTitle('Last')
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
        self.setWindowIcon(QtGui.QIcon('logo.png'))

    def UI(self):
        self.welcome_text = QLabel('Last window')
        self.profile_button = QPushButton('My profile')

        self.line = QVBoxLayout()
        self.line.addWidget(self.welcome_text, alignment=Qt.AlignCenter)
        self.line.addWidget(self.profile_button, alignment=Qt.AlignCenter)
        self.setLayout(self.line)

    def connections(self):
        self.profile_button.clicked.connect(self.profile_click)

    def profile_click(self):
        self.hide()
        self.pw = profile_win()
        self.pw.show()