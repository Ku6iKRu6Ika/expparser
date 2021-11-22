from .lexems import Lexer, TokenType
from .parser import ParserLexems
from .constants import CONSTANTS, FUNCTIONS, OPERATORS_ACTIONS
from .exceptions import FormulaUnknownVariable, FormulaUnknownFunction, FormulaLogicError

from typing import Dict, Union, Callable
from collections import deque
from math import modf

class Calculator:
    '''Reads result from RPN'''

    def __init__(self,
        variables: Dict[str, Union[float, int]] = {},
        functions: Dict[str, Callable[[Union[float, int]], Union[float, int]]] = {}
    ) -> None:
        self.variables = variables
        self.functions = functions

    def calc(self, expression: str) -> Union[float, int]:
        tokens = ParserLexems.parse(Lexer.tokenize(expression))

        return self._calc(tokens)

    def _calc(self, tokens: deque[TokenType]) -> Union[float, int]:
        assert tokens, 'Empty list of tokens'
        stack: deque[TokenType] = deque()

        for token in tokens:
            if token.type == TokenType.NUMBER:
                stack.append(token.value)
            elif token.type == TokenType.VARIABLE:
                value = self.variables.get(token.value, CONSTANTS.get(token.value))

                if value is None:
                    raise FormulaUnknownVariable(f'Unknown variable \'{token.value}\'')

                stack.append(value)
            elif token.type == TokenType.OPERATOR:
                if len(stack) < 2:
                    raise FormulaLogicError('There are not enough operands for the operation')

                operand2 = stack.pop()
                operand1 = stack.pop()

                stack.append(OPERATORS_ACTIONS[token.value](operand1, operand2))
            elif token.type == TokenType.UNAR_MINUS:
                if not stack:
                    raise FormulaLogicError('There are not enough operands for the operation')

                operand = stack.pop()
                stack.append(-operand)
            elif token.type == TokenType.FUNCTION:
                value = stack.pop()
                func = self.functions.get(token.value, FUNCTIONS.get(token.value))

                if func is None:
                    raise FormulaUnknownFunction(f'Unknown function \'{token.value}\'')

                stack.append(func(value))

        value = stack[0]

        if modf(value)[0] == 0:
            return int(value)

        return value
