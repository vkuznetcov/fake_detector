import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt, QProcess
from PyQt5.QtWidgets import QApplication, QMainWindow, QFormLayout, QSpinBox, QVBoxLayout, QWidget, QHBoxLayout, \
    QSizePolicy, QDoubleSpinBox, QLabel, QCheckBox,QPushButton,QTextEdit
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFileDialog

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Fake Image Detector")
        self.setGeometry(50, 50, 600, 800)  # Первые двве координаты смешение окна, последние две-размеры окна.
        self.widget = QWidget()

        self.main_lay = QVBoxLayout(self)

        self.panel = ControlPanel()
        self.main_lay.addWidget(self.panel)


        self.widget.setLayout(self.main_lay)
        self.setCentralWidget(self.widget)
        self.show()

class ControlPanel(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QVBoxLayout(self)
        self.label_methods = QLabel('Choose methods to detect',self)
        self.layout.addWidget(self.label_methods)
        self.method_layout = QHBoxLayout(self)
        self.method_1 = QCheckBox("Method1",self)
        self.method_2 = QCheckBox("Method2", self)
        self.method_3 = QCheckBox("Method3", self)
        self.method_layout.addWidget(self.method_1)
        self.method_layout.addWidget(self.method_2)
        self.method_layout.addWidget(self.method_3)
        self.layout.addLayout(self.method_layout)
        self.layout.setAlignment(Qt.AlignTop)

        self.path_layout=QHBoxLayout(self)
        self.label_path = QLabel('Choose image path',self)
        self.layout.addWidget(self.label_path)

        self.search_button = QPushButton('Browse', self)
        self.path_field = QTextEdit('Enter PATH to image')
        self.path_layout.addWidget(self.path_field)
        self.path_layout.addWidget(self.search_button)



        self.layout.addLayout(self.path_layout)
        self.browser = WinBrowser()
        self.search_button.clicked.connect(self.browser.searchFiles)
        self.search_button.clicked.connect(self.PrintPath)

        self.start_button=QPushButton('Start',self)
        self.layout.addWidget(self.start_button)
        #self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        #self.layout.addItem(self.spacerItem)
        self.layout.addStretch(5)
        self.layout.addSpacing(40)

        self.setLayout(self.layout)
    def PrintPath(self):
        self.path_field.setText(self.browser.filename)
class WinBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.filename=''

    def searchFiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\',
                                            'Images (*.png, *.xmp *.jpg)')
        self.filename=fname[0]

def start_app():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_app()