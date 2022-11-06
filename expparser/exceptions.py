from .abstract import AbstractException

class SyntaxError(AbstractException):
    pass

class LogicError(AbstractException):
    pass

class NotFoundError(AbstractException):
    pass
