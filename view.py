# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 212)
        MainWindow.setMinimumSize(QtCore.QSize(617, 212))
        MainWindow.setMaximumSize(QtCore.QSize(617, 212))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonExit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonExit.setGeometry(QtCore.QRect(170, 130, 93, 28))
        self.buttonExit.setObjectName("buttonExit")
        self.buttonCookieMinus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCookieMinus.setGeometry(QtCore.QRect(170, 10, 93, 28))
        self.buttonCookieMinus.setObjectName("buttonCookieMinus")
        self.buttonSandwichPlus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSandwichPlus.setGeometry(QtCore.QRect(20, 50, 93, 28))
        self.buttonSandwichPlus.setObjectName("buttonSandwichPlus")
        self.buttonCookiePlus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCookiePlus.setGeometry(QtCore.QRect(20, 10, 93, 28))
        self.buttonCookiePlus.setObjectName("buttonCookiePlus")
        self.buttonSandwichMinus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSandwichMinus.setGeometry(QtCore.QRect(170, 50, 93, 28))
        self.buttonSandwichMinus.setObjectName("buttonSandwichMinus")
        self.buttonWaterPlus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonWaterPlus.setGeometry(QtCore.QRect(20, 90, 93, 28))
        self.buttonWaterPlus.setObjectName("buttonWaterPlus")
        self.buttonWaterMinus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonWaterMinus.setGeometry(QtCore.QRect(170, 90, 93, 28))
        self.buttonWaterMinus.setObjectName("buttonWaterMinus")
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setGeometry(QtCore.QRect(20, 130, 93, 28))
        self.buttonClear.setObjectName("buttonClear")
        self.outputCookie = QtWidgets.QLabel(self.centralwidget)
        self.outputCookie.setGeometry(QtCore.QRect(280, 10, 91, 21))
        self.outputCookie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputCookie.setObjectName("outputCookie")
        self.outputSandwich = QtWidgets.QLabel(self.centralwidget)
        self.outputSandwich.setGeometry(QtCore.QRect(280, 50, 91, 21))
        self.outputSandwich.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputSandwich.setObjectName("outputSandwich")
        self.outputWater = QtWidgets.QLabel(self.centralwidget)
        self.outputWater.setGeometry(QtCore.QRect(280, 90, 91, 21))
        self.outputWater.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputWater.setObjectName("outputWater")
        self.outputTotal = QtWidgets.QLabel(self.centralwidget)
        self.outputTotal.setGeometry(QtCore.QRect(380, 0, 211, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputTotal.sizePolicy().hasHeightForWidth())
        self.outputTotal.setSizePolicy(sizePolicy)
        self.outputTotal.setMinimumSize(QtCore.QSize(211, 151))
        self.outputTotal.setMaximumSize(QtCore.QSize(211, 151))
        self.outputTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.outputTotal.setObjectName("outputTotal")
        self.addCookie = QtWidgets.QLineEdit(self.centralwidget)
        self.addCookie.setGeometry(QtCore.QRect(120, 10, 41, 28))
        self.addCookie.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.addCookie.setObjectName("addCookie")
        self.addSandwich = QtWidgets.QLineEdit(self.centralwidget)
        self.addSandwich.setGeometry(QtCore.QRect(120, 50, 41, 28))
        self.addSandwich.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.addSandwich.setObjectName("addSandwich")
        self.addWater = QtWidgets.QLineEdit(self.centralwidget)
        self.addWater.setGeometry(QtCore.QRect(120, 90, 41, 28))
        self.addWater.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.addWater.setObjectName("addWater")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Concessions"))
        self.buttonExit.setText(_translate("MainWindow", "Exit"))
        self.buttonCookieMinus.setText(_translate("MainWindow", "Cookie -"))
        self.buttonSandwichPlus.setText(_translate("MainWindow", "Sandwich +"))
        self.buttonCookiePlus.setText(_translate("MainWindow", "Cookie +"))
        self.buttonSandwichMinus.setText(_translate("MainWindow", "Sandwich -"))
        self.buttonWaterPlus.setText(_translate("MainWindow", "Water +"))
        self.buttonWaterMinus.setText(_translate("MainWindow", "Water -"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.outputCookie.setText(_translate("MainWindow", "Cookies"))
        self.outputSandwich.setText(_translate("MainWindow", "Sandwiches"))
        self.outputWater.setText(_translate("MainWindow", "Waters"))
        self.outputTotal.setText(_translate("MainWindow", "Total purchase"))
        self.addCookie.setText(_translate("MainWindow", "1"))
        self.addSandwich.setText(_translate("MainWindow", "1"))
        self.addWater.setText(_translate("MainWindow", "1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
