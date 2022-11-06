from typing import List
from decimal import Decimal

from .abstract import AbstractCalculator

from .constants import CONSTANTS, FUNCTIONS, OPERATORS_ACTIONS
from .entities import TokenType
from .lexer import Lexer
from .parser import Parser
from .exceptions import NotFoundError

class Calculator(AbstractCalculator):
    def calc(self, expression: str) -> Decimal:
        tokens = Parser.parse(Lexer.tokenize(expression))
        return self._calc(tokens)

    def _calc(self, tokens: List[TokenType]) -> Decimal:
        assert tokens, 'Empty list of tokens'
        stack: list[TokenType] = []

        for token in tokens:
            if token.type == TokenType.NUM:
                stack.append(token.value)
            elif token.type == TokenType.VAR:
                value = self.variables.get(token.value, CONSTANTS.get(token.value))

                if value is None:
                    raise NotFoundError(f'Variable \'{token.value}\' not found')

                stack.append(value)
            elif token.type == TokenType.OPERATOR:
                operand2 = stack.pop()
                operand1 = stack.pop()

                stack.append(OPERATORS_ACTIONS[token.value](operand1, operand2))
            elif token.type == TokenType.UNARY:
                operand = stack.pop()
                stack.append(-operand)
            elif token.type == TokenType.FUNC:
                value = stack.pop()
                func = self.functions.get(token.value, FUNCTIONS.get(token.value))

                if func is None:
                    raise NotFoundError(f'Function \'{token.value}\' not found')

                stack.append(func(value))

        value = stack[0]
    
        return value
