from PyQt5 import uic
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class Main(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("kebab.ui", self)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        
        self.load_data()

    def load_data(self):
        kebsy = [
            {"Nazwa":"OstryWChuj", "Sos":"Ostry", "Mieso":"baranina", "Cena":"John"}
        ]

        row = 0
        self.tableWidget.setRowCount(len(kebsy))
        for kebs in kebsy:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(kebs["Nazwa"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(kebs["Sos"]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(kebs["Mieso"]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(kebs["Cena"]))
            row += 1

if __name__=="__main__":
    app = QApplication([])
    main=Main()
    main.show()

    sys.exit(app.exec_())

