from .lexems import TokenType, Token
from .constants import OPERATORS_PRIORITY
from .exceptions import FormulaLogicError

class ParserLexems:
    @staticmethod
    def parse(tokens: list[TokenType]) -> list[TokenType]:
        assert tokens, 'Empty list of tokens'
        parse_tokens: list[TokenType] = []
        stack: list[TokenType] = []

        for j, i in enumerate(tokens):
            if i.type == TokenType.NUMBER or i.type == TokenType.VARIABLE:
                parse_tokens.append(i)

                if i.type == TokenType.NUMBER and j + 1 < len(tokens) and (
                    tokens[j + 1].type == TokenType.OPENING_BRACKET or
                    tokens[j + 1].type == TokenType.VARIABLE or tokens[j + 1].type == TokenType.FUNCTION
                ):
                    tokens.insert(j + 1, Token(TokenType.OPERATOR, '*'))

                if i.type == TokenType.NUMBER and j > 0 and tokens[j - 1].type == TokenType.CLOSED_BRACKET:
                    parse_tokens.append(Token(TokenType.OPERATOR, '*'))
            elif i.type == TokenType.FUNCTION:
                if len(tokens) - j < 3 or tokens[j + 2].type == TokenType.CLOSED_BRACKET:
                    raise FormulaLogicError('Nothing passed to the function')

                stack.append(i)
            elif i.type == TokenType.OPENING_BRACKET:
                stack.append(i)
            elif i.type == TokenType.CLOSED_BRACKET:
                while stack:
                    token = stack.pop()

                    if token.type == TokenType.OPENING_BRACKET:
                        break

                    parse_tokens.append(token)
                else:
                    raise FormulaLogicError('Invalid parentheses')
            elif i.type == TokenType.OPERATOR:
                while (stack and (
                        stack[-1].type == TokenType.FUNCTION or
                        OPERATORS_PRIORITY[stack[-1].value] >= OPERATORS_PRIORITY[i.value]
                    )):
                    parse_tokens.append(stack.pop())

                stack.append(i)
            elif i.type == TokenType.UNAR_MINUS:
                while (stack and (
                    stack[-1].type == TokenType.FUNCTION or
                    OPERATORS_PRIORITY[stack[-1].value] > OPERATORS_PRIORITY[i.value]
                )):
                    parse_tokens.append(stack.pop())

                stack.append(i)

        while stack:
            token = stack.pop()

            if token.type == TokenType.OPENING_BRACKET:
                raise FormulaLogicError('Invalid parentheses')

            parse_tokens.append(token)

        return parse_tokens
