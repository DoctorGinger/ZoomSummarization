
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QWidget,QHBoxLayout
from tkinter import Tk, filedialog

class Widget(QtWidgets.QMainWindow):

    def open_folder(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        self.path = filedialog.askopenfilename()

    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.widget = QWidget()
        self.widget.setStyleSheet("background-image: url(zoom.png); border: 2 px solid blue ; object-fit: cover; ")
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.path = ""

        self.btn_open = QPushButton("select video")
        self.btn_open.setStyleSheet( "border :3px solid white;background-color: white;  color: blue")
        self.btn_open.clicked.connect( self.open_folder)
        self.btn_open.setFixedSize(100, 80)
        self.layout.addWidget(self.btn_open)

def create_app():
        app = QtWidgets.QApplication([])
        mw = Widget()
        mw.show()
        app.exec()
        return mw.path

