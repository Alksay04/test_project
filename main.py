from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap
file_path = ''

app = QApplication([])
layout = QVBoxLayout()
window = QWidget()

buttons_layout = QHBoxLayout()
open_button = QPushButton('Открыть')
close_button = QPushButton('Закрыть')
buttons_layout.addWidget(open_button)
buttons_layout.addWidget(close_button)

layout.addLayout(buttons_layout)

window = QWidget()
window.setLayout(layout)
window.show()

picture = QLabel()
pixmap = QPixmap(file_path)
picture.setPixmap(pixmap)

layout.addWidget(picture)


def update_pixmap(file_path):
    global pixmap
    pixmap = QPixmap(file_path)
    picture.setPixmap(pixmap)


def openButtonHandler():
    global file_path
    filename = QFileDialog.getOpenFileName()[0]
    if filename:
        picture.setPixmap(QPixmap(filename))
        file_path = filename


open_button.clicked.connect(openButtonHandler)

app.exec()