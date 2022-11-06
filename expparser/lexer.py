from decimal import Decimal
from typing import Tuple, List

from .abstract import AbstractLexer

from .constants import END, POINT
from .entities import Token, TokenType, TokenSign
from .exceptions import SyntaxError


class LexerUtilities:
    @staticmethod
    def read_token(experession: str, pos: int) -> Tuple[Token, int]:
        length = len(experession)

        if experession[pos].isalpha():
            variable = ''

            while pos < length and (experession[pos].isalpha() or experession[pos].isdigit()):
                variable += experession[pos]
                pos += 1

            if experession[pos:].strip().startswith('('):
                type_token = TokenType.FUNC
            else:
                type_token = TokenType.VAR

            pos -= 1

            return Token(type_token, variable), pos
        else:
            number = ''

            while pos < length and (experession[pos].isdigit() or experession[pos] == POINT):
                if experession[pos] == POINT and POINT in number:
                    raise SyntaxError(f'Wrong number in position {pos + 1}')

                number += experession[pos]
                pos += 1

            pos -= 1

            return Token(TokenType.NUM, Decimal(number)), pos


class Lexer(AbstractLexer):
    @staticmethod
    def tokenize(experession: str) -> List[TokenType]:
        tokens: List[TokenType] = []
        pos = 0

        experession = experession.strip()
        assert experession, 'Empty expression'
        length = len(experession)

        while pos < length:
            if experession[pos] in TokenSign.OPERATORS:
                # Проверка на унарный минус
                # Если нету токенов или последний токен оператор или открывающая скобка
                if experession[pos] == '-' and (
                    not tokens or tokens[END].type in {TokenType.OPERATOR, TokenType.OPEN_BKT}
                ):
                    tokens.append(Token(TokenType.UNARY, TokenSign.UNARY))
                else:
                    # Вызывает исключение, если два оператора подряд
                    if tokens and tokens[END].type in {TokenType.OPERATOR, TokenType.UNARY}:
                        raise SyntaxError(f'The operator comes after the operator in position {pos + 1}')

                    # Вызывает исключение, если оператор используется как унарный минус
                    if not tokens or tokens[END].type == TokenType.OPEN_BKT:
                        raise SyntaxError(f'No number or variable before operator at position {pos}')

                    tokens.append(Token(TokenType.OPERATOR, experession[pos]))
            elif experession[pos].isalpha() or experession[pos].isdigit() or experession[pos] == POINT:
                if tokens and tokens[END].type in {TokenType.VAR, TokenType.NUM}:
                    raise SyntaxError(f'No operator between operands at position {pos}')

                token, pos = LexerUtilities.read_token(experession, pos)
                tokens.append(token)
            elif experession[pos] == TokenSign.OPEN_BKT:
                tokens.append(Token(TokenType.OPEN_BKT, TokenSign.OPEN_BKT))
            elif experession[pos] == TokenSign.CLOSE_BKT:
                if tokens[END].type == TokenType.OPERATOR:
                    raise SyntaxError(f'No number or variable before operator at position {pos + 1}')

                tokens.append(Token(TokenType.CLOSE_BKT, TokenSign.CLOSE_BKT))
            elif not experession[pos].isspace():
                raise SyntaxError(f'At position {pos + 1} is an unknown character {experession[pos]}')

            pos += 1

        if tokens[END].type == TokenType.OPERATOR:
            raise SyntaxError(f'No number or variable before operator at position {pos + 1}')

        return tokens
