import math


class Calculate:
    def __init__(self, firstNo, operator, secondNo):
        self.firstNo = firstNo
        self.operator = operator
        self.secondNo = secondNo

    def checkSecondNumber(self):
        return self.secondNo != 0

    def doCalculation(self):
        if self.operator == '+':
            return self.firstNo + self.secondNo

        elif self.operator == '-':
            return self.firstNo - self.secondNo

        elif self.operator == '*':
            return self.firstNo * self.secondNo

        elif self.operator == '/':
            if self.checkSecondNumber():
                return self.firstNo / self.secondNo
            else:
                print('Division by zero not allowed')
        else:
            print('Enter a valid operator')

    def getCalculation(self):
        print(self.doCalculation())


class ScientificCalculator(Calculate):
    def __init__(self, operator, number):
        self.operator = operator
        self.number = number

    def doCalculation(self):
        if self.operator == 'sin':
            return math.sin(self.number)

        elif self.operator == 'cos':
            return math.cos(self.number)

        elif self.operator == 'tan':
            return math.tan(self.number)

        elif self.operator == 'log':
            return math.log(self.number)

        else:
            print('Invalid Operator')


while True:
    choice = input('Enter your choice 1) Basic 2) Scientific  \'n\' to quit ')

    if choice == '1':
        again = 'y'

        while again != 'n':
            firstNo, operator, secondNo = input(
                'Enter the operation statement(eg: 5+4)')
            Calculate(int(firstNo), operator, int(secondNo)).getCalculation()
            again = input('Another operation? (y or n)')

    elif choice == '2':
        again = 'y'

        while again != 'n':
            operator, number = input(
                'Enter the operation statement(eg: sin 4)').split()
            ScientificCalculator(operator, int(number)).getCalculation()
            again = input('Another operation? (y or n)')

    else:
        break
