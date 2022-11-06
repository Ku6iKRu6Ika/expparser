## Парсер математических выражений
#### Что умеет:
- Работать с операциями +, -, *, /, ^, %
- Работать с переменными
- Работать с функциями

#### Встороенные перменные:
- PI
- E

#### Встороенные функции:
- abs
- sqrt
- sin
- cos
- tan
- log2
- log10
- exp
- ln
- factorial
- floor
- fraction

#### Пример кода:
```python
from expparser.calculator import Calculator

calculator = Calculator()

while True:
    try:
        print('Result:', calculator.calc(input('Expression: ')))
    except Exception as ex:
        print(f'{ex.__class__.__name__}: {ex}')
```

## DOC
##### *class expparser.calculator.Calculator(variables: Dict[str, Decimal] = {}, functions: Dict[str, Callable[[Decimal], Decimal]] = {})*
  - **Аргументы:**
    - **variables(Dict[str, Decimal], {})** - переменные
    - **functions(Dict[str, Callable[[Decimal], Decimal]], {})** - функции
  - **calc(expression: str) -> Decimal**
    - Вычисляет значение выражения.
    - **Аргументы:**
      - **expression(str)** - выражение
