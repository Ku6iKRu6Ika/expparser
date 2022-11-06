from typing import List

from .abstract import AbstractParser

from .constants import OPERATORS_PRIORITY, END
from .entities import Token, TokenType
from .exceptions import LogicError

class ParserUtilities:
    @staticmethod
    def get_priority(token: TokenType):
        return OPERATORS_PRIORITY[token.value]

class Parser(AbstractParser):
    # Алгоритм преобразования выражения в ОПЗ
    @staticmethod
    def parse(tokens: List[TokenType]) -> List[TokenType]:
        assert tokens, 'Empty list of tokens'

        length = len(tokens)
        parse_tokens: List[TokenType] = []
        stack: List[TokenType] = []

        for pos, token in enumerate(tokens):
            if token.type in {TokenType.NUM, TokenType.VAR}:
                parse_tokens.append(token)

                # Ставить оператор умножения если его явно нету
                if (pos + 1 < length and
                    token.type == TokenType.NUM and
                    tokens[pos + 1].type in {TokenType.OPEN_BKT, TokenType.VAR, TokenType.FUNC}
                ):
                    tokens.insert(pos + 1, Token(TokenType.OPERATOR, '*'))

                if (pos > 0 and
                    token.type == TokenType.NUM and
                    tokens[pos - 1].type == TokenType.CLOSE_BKT
                ):
                    parse_tokens.append(Token(TokenType.OPERATOR, '*'))
            elif token.type == TokenType.FUNC:
                if length - pos < 3 or tokens[pos + 2].type == TokenType.CLOSE_BKT:
                    raise LogicError('Nothing is passed to the function')

                stack.append(token)
            elif token.type == TokenType.OPEN_BKT:
                stack.append(token)
            elif token.type == TokenType.CLOSE_BKT:
                while stack:
                    token_stack = stack.pop()

                    if token_stack.type == TokenType.OPEN_BKT:
                        break

                    parse_tokens.append(token_stack)
                else:
                    raise LogicError('Invalid brackets')
            elif token.type == TokenType.OPERATOR:
                while stack and (
                    stack[END].type == TokenType.FUNC or
                    ParserUtilities.get_priority(stack[END]) >= ParserUtilities.get_priority(token)
                ):
                    parse_tokens.append(stack.pop())

                stack.append(token)
            elif token.type == TokenType.UNARY:
                stack.append(token)

        while stack:
            token = stack.pop()

            if token.type == TokenType.OPEN_BKT:
                raise LogicError('Invalid brackets')

            parse_tokens.append(token)

        return parse_tokens
