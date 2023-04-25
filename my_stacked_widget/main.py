from PyQt5.QtWidgets import *
import sys
from my_stacked_widget import  Ui_MainWindow

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.stackedWidget.setCurrentWidget(self.green)

        self.pushButton.clicked.connect(self.change_green)
        self.pushButton_2.clicked.connect(self.change_blue)
        self.pushButton_3.clicked.connect(self.change_yellow)
        self.pushButton_4.clicked.connect(self.change_red)
    def change_green(self):
        self.stackedWidget.setCurrentWidget(self.green)
    def change_blue(self):
        self.stackedWidget.setCurrentWidget(self.blue)
    def change_yellow(self):
        self.stackedWidget.setCurrentWidget(self.yellow)
    def change_red(self):
        self.stackedWidget.setCurrentWidget(self.red)

if __name__ == "__main__":
    app = QApplication([])
    main = Main()
    main.show()
    sys.exit(app.exec_())