from enum import Enum
from collections import deque
from .constants import OPERATORS
from .exceptions import FormulaSyntaxError, FormulaUnknownSymbol

class TokenType(Enum):
    '''Enumeration with token types in expression'''

    NUMBER = 0
    OPERATOR = 1
    UNAR_MINUS = 2
    VARIABLE = 3
    FUNCTION = 4
    OPENING_BRACKET = 5
    CLOSED_BRACKET = 6

class TokenIdentifiers:
    '''Identifiers for tokens'''

    OPERATORS = OPERATORS
    UNAR_MINUS = '~'
    OPENING_BRACKET = '('
    CLOSED_BRACKET = ')'

class Token:
    '''Smallest unit of expression'''

    def __init__(self, token_type: TokenType, token_value) -> None:
        '''
            token_type: TokenType - token type from TokenType
            token_value: Any - token value
        '''
        self._token_type = token_type
        self._token_value = token_value

    @property
    def type(self) -> TokenType:
        return self._token_type

    @property
    def value(self):
        return self._token_value

    def __repr__(self) -> str:
        return f'<{self._token_type} value={self._token_value}>'

class Lexer:
    '''The main lexer class'''

    @staticmethod
    def tokenize(experession: str) -> deque[TokenType]:
        '''
            Translates an expression into a list of tokens.

            Example:
                Lexer.tokenize('2 + 2') => [<TokenType.NUMBER value=2.0>, <TokenType.OPERATOR value=+>, <TokenType.NUMBER value=2.0>]
        '''

        tokens: deque[TokenType] = deque()
        i = 0 # Character index in expression

        experssion = experession.strip()
        len_experssion = len(experssion)

        while i < len_experssion:
            if experssion[i] in TokenIdentifiers.OPERATORS:
                # Defines a unary minus
                if (experssion[i] == '-' and (not tokens or (
                        tokens[-1].type != TokenType.NUMBER and
                        tokens[-1].type != TokenType.VARIABLE and
                        tokens[-1].type != TokenType.CLOSED_BRACKET
                ))):
                    tokens.append(Token(TokenType.UNAR_MINUS, TokenIdentifiers.UNAR_MINUS))
                else:
                    # Throws an exception if two operators except + and - appear twice in a row
                    if (tokens and
                        tokens[-1].type == TokenType.OPERATOR and
                        experssion[i] != '+' and
                        experssion[i] != '-'
                    ):
                        raise FormulaSyntaxError('Invalid syntax')

                    # Adds an operator if it is not unary +
                    if (tokens and not ((
                            tokens[-1].type == TokenType.OPERATOR or
                            tokens[-1].type == TokenType.OPENING_BRACKET
                        ) and
                        experssion[i] == '+'
                    )):
                        tokens.append(Token(TokenType.OPERATOR, experssion[i]))
            elif experssion[i] == TokenIdentifiers.OPENING_BRACKET:
                tokens.append(Token(TokenType.OPENING_BRACKET, TokenIdentifiers.OPENING_BRACKET))
            elif experssion[i] == TokenIdentifiers.CLOSED_BRACKET:
                tokens.append(Token(TokenType.CLOSED_BRACKET, TokenIdentifiers.CLOSED_BRACKET))
            elif experssion[i].isalpha():
                # Checks that there is no number in front of a variable or a function
                variable = ''

                # Adds characters to variable until it encounters a space
                while i < len_experssion and (experssion[i].isalpha() or experssion[i].isdigit()):
                    variable += experssion[i]
                    i += 1

                j = i

                # searches '(' before a variable to check that it is not a function
                while j < len_experssion and experssion[j] not in TokenIdentifiers.OPERATORS and not experssion[j].isdigit():
                    if experssion[j] == TokenIdentifiers.OPENING_BRACKET:
                        tokens.append(Token(TokenType.FUNCTION, variable))
                        break

                    j += 1
                else:
                    tokens.append(Token(TokenType.VARIABLE, variable))

                i -= 1
            elif experssion[i].isdigit() or experssion[i] == '.':
                # Throw an exception if there is no operator between the operands
                if tokens and (tokens[-1].type == TokenType.VARIABLE or
                               tokens[-1].type == TokenType.NUMBER
                ):
                    raise FormulaSyntaxError('No operator between operands')

                number = ''

                # Getting a number
                while i < len_experssion and (experssion[i].isdigit() or experssion[i] == '.'):
                    if experssion[i] == '.' and '.' in number:
                        raise FormulaSyntaxError('Invalid number')

                    number += experssion[i]
                    i += 1

                i -= 1
                
                tokens.append(Token(TokenType.NUMBER, float(number)))
            elif not experssion[i].isspace():
                raise FormulaUnknownSymbol(f'Unknown symbol \'{experssion[i]}\'')

            i += 1

        return tokens
