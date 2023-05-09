from PyQt5.QtWidgets import *
from view import *


"""
This application rus PyQt5 for GUI.
It includes main.py, view.py, and controller.py.
Program output is contained in the GUI.
"""

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        """
        water: variable for item count of waters
        cookie: variable for item count of cookies
        sandwich: variable for item count of sandwiches
        waterCost: variable for the price per water
        cookieCost: variable for the price per cookie
        sandwichCost: variable for the price per sandwich
        cookieTotal: variable for the number of cookies * price per cookie
        sandwichTotal: variable for the number of sandwiches * price per sandwich
        waterTotal: variable for the number of waters * price per water
        totalItems: count of the total number of waters + cookies + sandwiches
        subTotal: amount of cookieTotal + sandwichTotal + waterTotal
        tax: subTotal * tax rate of 7%
        total: subTotal + tax
        Initial setup for the application by clearing the output box and
        setting all the quantity entry boxes to 1 the establishing commands
        that run as each button is pressed.
        """
        self.water = 0
        self.cookie = 0
        self.sandwich = 0
        self.waterCost = 1.00
        self.cookieCost = 2.00
        self.sandwichCost = 4.50
        self.cookieTotal = 0
        self.sandwichTotal = 0
        self.waterTotal = 0
        self.totalItems = 0
        self.subTotal = 0
        self.tax = 0
        self.total = 0
        self.clear()
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonExit.clicked.connect(lambda: exit(code=0))
        self.buttonWaterPlus.clicked.connect(lambda: self.water_tally())
        self.buttonWaterMinus.clicked.connect(lambda: self.water_tally_minus())
        self.buttonCookiePlus.clicked.connect(lambda: self.cookie_tally())
        self.buttonCookieMinus.clicked.connect(lambda: self.cookie_tally_minus())
        self.buttonSandwichPlus.clicked.connect(lambda: self.sandwich_tally())
        self.buttonSandwichMinus.clicked.connect(lambda: self.sandwich_tally_minus())

    def water_tally(self):
        #adds items based on addWater box to water count
        try:
            self.water += int(self.addWater.text())
            if self.water < 0:
                self.water = 0
            self.outputWater.setText(f'{self.water} waters')
            self.output_display()
        except:
            self.outputTotal.setText(f'Integer must be used in\nwater plus calculation')
            self.addWater.setText('1')

    def water_tally_minus(self):
        #subtracts items based on addWater box from water count
        try:
            self.water -= int(self.addWater.text())
            if self.water < 0:
                self.water = 0
            self.outputWater.setText(f'{self.water} waters')
            self.output_display()
        except:
            self.outputTotal.setText(f'Integer must be used in\nwater minus calculation')
            self.addWater.setText('1')

    def cookie_tally(self):
        #adds items based on addCookie box to cookie count
        try:
            self.cookie += int(self.addCookie.text())
            if self.cookie < 0:
                self.cookie = 0
            self.outputCookie.setText(f'{self.cookie} cookies')
            self.output_display()
        except:
            self.outputTotal.setText(f'Integer must be used in\ncookie plus calculation')
            self.addCookie.setText('1')

    def cookie_tally_minus(self):
        #subtracts items based on addCookie box from cookie count
        try:
            self.cookie -= int(self.addCookie.text())
            if self.cookie < 0:
                self.cookie = 0
            self.outputCookie.setText(f'{self.cookie} cookies')
            self.output_display()
        except:
            self.outputTotal.setText(f'Integer must be used in\ncookie minus calculation')
            self.addCookie.setText('1')

    def sandwich_tally(self):
        #adds items based on addSandwich box to sandwich count
        try:
            self.sandwich += int(self.addSandwich.text())
            if self.sandwich < 0:
                self.sandwich = 0
            self.outputSandwich.setText(f'{self.sandwich} sandwiches')
            self.output_display()
        except:
            self.outputTotal.setText(f'Integer must be used in\nsandwich plus calculation')
            self.addSandwich.setText('1')

    def sandwich_tally_minus(self):
        #subtracts items based on addSandwich from sandwich count
        try:
            self.sandwich -= int(self.addSandwich.text())
            if self.sandwich < 0:
                self.sandwich = 0
            self.outputSandwich.setText(f'{self.sandwich} sandwiches')
            self.output_display()
        except:
            self.outputTotal.setText(f'Integer must be used in\nsandwich minus calculation')
            self.addSandwich.setText('1')

    def clear(self):
        #clears all output boxes and sets default addition of each item to 1
        try:
            self.cookie = 0
            self.sandwich = 0
            self.water = 0
            self.output_display()
            self.addWater.setText('1')
            self.addCookie.setText('1')
            self.addSandwich.setText('1')
            self.outputCookie.setText(f'{self.cookie} cookies')
            self.outputWater.setText(f'{self.water} waters')
            self.outputSandwich.setText(f'{self.sandwich} sandwiches')
        except:
            self.outputTotal.setText('Error clearing screen')

    def output_display(self):
        #sets output based on user entry in a receipt format
        try:
            self.cookieTotal = self.cookie * self.cookieCost
            self.sandwichTotal = self.sandwich * self.sandwichCost
            self.waterTotal = self.water * self.waterCost
            self.totalItems = self.cookie + self.sandwich + self.water
            self.subTotal = self.cookieTotal + self.sandwichTotal + self.waterTotal
            self.tax = self.subTotal * .07
            self.total = self.subTotal + self.tax
            self.outputTotal.setText(f'Cookies x{self.cookie}\t\t${self.cookieTotal:.2f}'
                                     f'\nSandwiches x{self.sandwich}\t\t${self.sandwichTotal:.2f}'
                                     f'\nWater x{self.water}\t\t${self.waterTotal:.2f}'
                                     f'\nTotal Items\t\t\t\t\t{self.totalItems}'
                                     f'\n'
                                     f'\nSubtotal\t\t${self.subTotal:.2f}'
                                     f'\nTax (7%)\t\t${self.tax:.2f}'
                                     f'\n--------------------------------'
                                     f'\nTotal\t\t${self.total:.2f}')
        except:
            self.outputTotal.setText('Error when producing output')
