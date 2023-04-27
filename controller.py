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
        self.clear()
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonExit.clicked.connect(lambda: exit(code=0))
        self.buttonWaterPlus.clicked.connect(lambda: self.waterTally(1))
        self.buttonWaterMinus.clicked.connect(lambda: self.waterTally(-1))
        self.buttonCookiePlus.clicked.connect(lambda: self.cookieTally(1))
        self.buttonCookieMinus.clicked.connect(lambda: self.cookieTally(-1))
        self.buttonSandwichPlus.clicked.connect(lambda: self.sandwichTally(1))
        self.buttonSandwichMinus.clicked.connect(lambda: self.sandwichTally(-1))

    def waterTally(self, tally):
        self.water += tally
        if self.water < 0:
            self.water = 0
        self.outputWater.setText(f'{self.water} waters')
        self.outputDisplay()

    def cookieTally(self, tally):
        self.cookie += tally
        if self.cookie < 0:
            self.cookie = 0
        self.outputCookie.setText(f'{self.cookie} cookies')
        self.outputDisplay()

    def sandwichTally(self, tally):
        self.sandwich += tally
        if self.sandwich < 0:
            self.sandwich = 0
        self.outputSandwich.setText(f'{self.sandwich} sandwiches')
        self.outputDisplay()

    def clear(self):
        self.cookie = 0
        self.sandwich = 0
        self.water = 0
        self.outputDisplay()
        self.outputCookie.setText(f'{self.cookie} cookies')
        self.outputWater.setText(f'{self.water} waters')
        self.outputSandwich.setText(f'{self.sandwich} sandwiches')

    def outputDisplay(self):
        self.cookieTotal = self.cookie * self.cookieCost
        self.sandwichTotal = self.sandwich * self.sandwichCost
        self.waterTotal = self.water * self.waterCost
        self.totalItems = self.cookie + self.sandwich + self.water
        self.subTotal = self.cookieTotal + self.sandwichTotal + self.waterTotal
        self.tax = self.subTotal * .07
        self.total = self.subTotal + self.tax
        self.outputTotal.setText(f'Cookies x{self.cookie}\t\t{self.cookieTotal:.2f}'
                                 f'\nSandwiches x{self.sandwich}\t\t{self.sandwichTotal:.2f}'
                                 f'\nWater x{self.water}\t\t{self.waterTotal:.2f}'
                                 f'\nTotal Items\t\t\t\t\t{self.totalItems}'
                                 f'\n'
                                 f'\nSubtotal\t\t{self.subTotal:.2f}'
                                 f'\nTax (7%)\t\t{self.tax:.2f}'
                                 f'\n--------------------------------'
                                 f'\nTotal\t\t{self.total:.2f}')

"""      
old code to incorporate into new gui version
def main_menu():
    print('----MAIN MENU----')
    print('s: Shop')
    print('x: Exit')
    selection = input('Option: ')
    selection = selection.lower().strip()
    while selection != 's' and selection != 'x':
        selection = input('Invalid (s/x): ')
        selection = selection.lower().strip()
    return selection


def cart_menu():
    print('----CART MENU----')
    print('1: Cookie - $1.50')
    print('2: Sandwich - $4.00')
    print('3: Water - $1.00')
    item = input('Item: ')
    item = item.strip()
    while item != '1' and item != '2' and item != '3':
        item = input('Invalid (1-3): ')
        item = item.strip()
    return item


def main():
    cookie = 0
    sandwich = 0
    water = 0
    selection = ''
    while selection != 'x':
        selection = main_menu()
        if selection == 's':
            item = cart_menu()
            if item == '1':
                print('Added cookie')
                cookie += 1
            elif item == '2':
                print('Added sandwich')
                sandwich += 1
            elif item == '3':
                print('Added water')
                water += 1
            continue
        else:
            break
    print('----------------------------------')
    print(f'({cookie}) - Cookie = ${cookie * 1.50:.2f}')
    print(f'({sandwich}) - Sandwich = ${sandwich * 4.00:.2f}')
    print(f'({water}) - Water = ${water * 1.00:.2f}')
    print('----------------------------------')
    print(f'GRAND TOTAL = ${((cookie * 1.50) + (sandwich * 4.00) + (water * 1.00)):.2f}')
    print('----------------------------------')
"""