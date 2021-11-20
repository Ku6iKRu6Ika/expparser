## Парсер математических выражений
#### Что умеет:
- Работать с операциями +, -, *, /, ^
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
- fact (факториал)
- exp

#### Пример кода:
```python
from expparser.calculator import Calculator

calculator = Calculator()

while True:
    print('Result:', calculator.calc(input('Expression: ')))
```

## API
##### *class expparser.calculator.Calculator(variables: Dict[str, Union[float, int]] = {}, functions: Dict[str, Callable[[Union[float, int]], Union[float, int]]] = {})*
  - **Аргументы:**
    - **variables(Dict[str, Union[float, int]], {})** - переменные
    - **functions(Dict[str, Callable[[Union[float, int]], Union[float, int]]], {})** - функции
  - **calc(expression: str) -> Union[float, int]**
    Вычисляет значение выражения.
    - **Аргументы:**
      - **expression(str)** - выражение