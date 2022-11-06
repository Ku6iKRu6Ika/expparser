import math
from decimal import Decimal
from typing import Dict, Callable, Set

END = -1
POINT = '.'

OPERATORS: Set[str] = {'+', '-', '*', '/', '^', '%'}

OPERATORS_ACTIONS: Dict[str, Callable[[Decimal], Decimal]] = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y,
    '^' : lambda x, y: x ** y,
    '%' : lambda x, y: x % y
}

OPERATORS_PRIORITY: Dict[str, int] = {
    '(' : 0, ')' : 1,
    '+' : 2, '-' : 2,
    '*' : 3, '/' : 3, '%' : 3,
    '^' : 4,
    '~' : 5,
}

CONSTANTS: Dict[str, Decimal] = {
    'PI' : Decimal(math.pi),
    'E' : Decimal(math.e),
}

FUNCTIONS: Dict[str, Callable[[Decimal], Decimal]] = {
    'abs' : lambda x: Decimal(abs(float(x))),
    'sqrt' : lambda x: Decimal(math.sqrt(float(x))),
    'sin' : lambda x: Decimal(math.sin(float(x))),
    'cos' : lambda x: Decimal(math.cos(float(x))),
    'tan' : lambda x: Decimal(math.tan(float(x))),
    'log2' : lambda x: Decimal(math.log2(float(x))),
    'log10' : lambda x: Decimal(math.log10(float(x))),
    'exp' : lambda x: Decimal(math.exp(float(x))),
    'ln' : lambda x: Decimal(math.log(float(x), math.e)),
    'factorial' : lambda x: Decimal(math.factorial(float(x))),
    'floor' : lambda x: Decimal(math.floor(float(x))),
    'fraction' : lambda x: x - Decimal(math.floor(float(x)))
}
