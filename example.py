from expparser.calculator import Calculator

calculator = Calculator()

while True:
    print('Result:', calculator.calc(input('Expression: ')))
