from enum import Enum

from .constants import OPERATORS


TokenType = Enum('TokenType', [
    'NUM',
    'OPERATOR',
    'UNARY',
    'VAR',
    'FUNC',
    'OPEN_BKT',
    'CLOSE_BKT'
])


class Token:
    def __init__(self, token_type: TokenType, token_value) -> None:
        self.type = token_type
        self.value = token_value

    def __repr__(self) -> str:
        return f'<{self.type} value={self.value}>'


class TokenSign:
    OPERATORS = OPERATORS
    UNARY = '~'
    OPEN_BKT = '('
    CLOSE_BKT = ')'
