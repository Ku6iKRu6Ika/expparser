import math
from typing import Dict, Union, Callable

OPERATORS: str = '+-*/^'

OPERATORS_ACTIONS: Dict[str, Callable[[Union[float, int]], Union[float, int]]] = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y,
    '^' : lambda x, y: x ** y,
}

OPERATORS_PRIORITY: Dict[str, int] = {
    '(' : 0, ')' : 1,
    '+' : 2, '-' : 2,
    '*' : 3, '/' : 3,
    '^' : 4,
    '~' : 5,
}

CONSTANTS: Dict[str, Union[float, int]] = {
    'PI' : math.pi,
    'E' : math.e,
}

FUNCTIONS: Dict[str, Callable[[Union[float, int]], Union[float, int]]] = {
    'abs' : lambda x: abs(x),
    'sqrt' : lambda x: math.sqrt(x),
    'sin' : lambda x: math.sin(x),
    'cos' : lambda x: math.cos(x),
    'tan' : lambda x: math.tan(x),
    'log2' : lambda x: math.log2(x),
    'log10' : lambda x: math.log10(x),
    'fact' : lambda x: math.factorial(x),
    'exp' : lambda x: math.exp(x),
}
