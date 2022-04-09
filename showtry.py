from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from tax_cal import cal
from UI.ui import Ui_MainWindow
from qt_material import apply_stylesheet
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.validator = QtGui.QIntValidator()
        self.ui.lineEdit.setValidator(self.validator)
        self.ui.lineEdit.textChanged.connect(self.text_changed)
        self.ui.lineEdit_2.setValidator(self.validator)
        self.ui.pushButton.setText('Calculate')
        self.ui.lineEdit_2.setEnabled(0)
        self.ui.pushButton.setEnabled(0)
        self.ui.pushButton.clicked.connect(self.buttonClicked)
        self.ui.pushButton_2.clicked.connect(self.clear)
        self.ui.radioButton_2.toggled.connect(self.onclicksingle)
        self.ui.radioButton.toggled.connect(self.onclickmarry)

    def text_changed(self,s):
        if not s:
            self.ui.pushButton.setEnabled(0)
        if s:
            self.ui.pushButton.setEnabled(1)

    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

    def buttonClicked(self):
        _translate = QtCore.QCoreApplication.translate
        text = self.ui.lineEdit.text()
        text2 = self.ui.lineEdit_2.text()
        Male = int(text)
        if self.ui.radioButton_2.isChecked():
            calculation = cal()
            data= calculation.single(Male)
            for i in range(5):
                item = self.ui.tableWidget.item(i, 0)
                item.setText(_translate("MainWindow", str(int(data[i]))))
            for i in range(5):
                item = self.ui.tableWidget.item(i, 1)
                item.setText(_translate("MainWindow", "N/A"))
            for i in range(5):
                item = self.ui.tableWidget.item(i, 2)
                item.setText(_translate("MainWindow", "N/A"))
            self.ui.label_5.setText(data[5])
        if self.ui.radioButton.isChecked():
            Female = int(text2)
            calculation = cal()
            data1 = calculation.single(Male)
            data2 = calculation.single(Female)
            data3 = calculation.joint(Male, Female)
            for i in range(5):
                item = self.ui.tableWidget.item(i, 0)
                item.setText(_translate("MainWindow", str(int(data1[i]))))
            for i in range(5):
                item = self.ui.tableWidget.item(i, 1)
                item.setText(_translate("MainWindow", str(int(data2[i]))))
            for i in range(5):
                item = self.ui.tableWidget.item(i, 2)
                item.setText(_translate("MainWindow", str(int(data3[i]))))
            noticestring = calculation.better(data3[4],data1[4],data2[4])
            self.ui.label_5.setText(data1[5])
            self.ui.label_6.setText(data2[5])
            self.ui.label_7.setText(data3[5])
            self.ui.label_4.setText(noticestring)

    def onclicksingle(self):
        self.ui.radioButton_2 = self.sender()
        if self.ui.radioButton_2.isChecked():
            self.ui.lineEdit_2.setEnabled(0)
    def onclickmarry(self):
        self.ui.radioButton = self.sender()
        if self.ui.radioButton.isChecked():
            self.ui.lineEdit_2.setEnabled(1)
            self.ui.pushButton.setEnabled(0)
            self.ui.lineEdit_2.textChanged.connect(self.text_changed)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    apply_stylesheet(app, theme='dark_teal.xml')
    window.show()
    sys.exit(app.exec_())