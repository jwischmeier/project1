from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
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
        self.buttonWaterPlus.clicked.connect(lambda: self.water_tally(1))
        self.buttonWaterMinus.clicked.connect(lambda: self.water_tally(-1))
        self.buttonCookiePlus.clicked.connect(lambda: self.cookie_tally(1))
        self.buttonCookieMinus.clicked.connect(lambda: self.cookie_tally(-1))
        self.buttonSandwichPlus.clicked.connect(lambda: self.sandwich_tally(1))
        self.buttonSandwichMinus.clicked.connect(lambda: self.sandwich_tally(-1))

    def water_tally(self, tally):
        self.water += tally
        if self.water < 0:
            self.water = 0
        self.outputWater.setText(f'{self.water} waters')
        self.output_display()

    def cookie_tally(self, tally):
        self.cookie += tally
        if self.cookie < 0:
            self.cookie = 0
        self.outputCookie.setText(f'{self.cookie} cookies')
        self.output_display()

    def sandwich_tally(self, tally):
        self.sandwich += tally
        if self.sandwich < 0:
            self.sandwich = 0
        self.outputSandwich.setText(f'{self.sandwich} sandwiches')
        self.output_display()

    def clear(self):
        self.cookie = 0
        self.sandwich = 0
        self.water = 0
        self.output_display()
        self.outputCookie.setText(f'{self.cookie} cookies')
        self.outputWater.setText(f'{self.water} waters')
        self.outputSandwich.setText(f'{self.sandwich} sandwiches')

    def output_display(self):
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
