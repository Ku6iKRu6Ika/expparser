from expparser.calculator import Calculator

calculator = Calculator()

while True:
    try:
        print('Result:', calculator.calc(input('Expression: ')))
    except Exception as ex:
        print(f'{ex.__class__.__name__}: {ex}')
