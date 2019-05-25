# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\黄翰林\Desktop\数据库大作业\前端制作\GaoKao\ChildrenForm3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChildrenFrom3(object):
    def setupUi(self, ChildrenFrom3):
        ChildrenFrom3.setObjectName("ChildrenFrom3")
        ChildrenFrom3.resize(400, 300)
        self.tableWidget = QtWidgets.QTableWidget(ChildrenFrom3)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 271, 91))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(ChildrenFrom3)
        QtCore.QMetaObject.connectSlotsByName(ChildrenFrom3)

    def retranslateUi(self, ChildrenFrom3):
        _translate = QtCore.QCoreApplication.translate
        ChildrenFrom3.setWindowTitle(_translate("ChildrenFrom3", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ChildrenFrom3", "Name"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ChildrenFrom3", "Height"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ChildrenFrom3", "Weight"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ChildrenFrom3", "HHL"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ChildrenFrom3", "HZL"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ChildrenFrom3", "LHZ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChildrenFrom3 = QtWidgets.QWidget()
    ui = Ui_ChildrenFrom3()
    ui.setupUi(ChildrenFrom3)
    ChildrenFrom3.show()
    sys.exit(app.exec_())

