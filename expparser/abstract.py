from abc import ABC, abstractstaticmethod, abstractmethod
from typing import (
    Dict,
    Callable,
    List,
    Any
)
from decimal import Decimal


class AbstractCalculator(ABC):
    def __init__(self,
        variables: Dict[str, Decimal] = {},
        functions: Dict[str, Callable[[Decimal], Decimal]] = {}
    ) -> None:
        self.variables = variables
        self.functions = functions

    @abstractmethod
    def calc(self, expression: str) -> Decimal:
        pass


class AbstractParser(ABC):
    @abstractstaticmethod
    def parse(tokens: List[Any]) -> List[Any]:
        pass


class AbstractLexer(ABC):
    @abstractstaticmethod
    def tokenize(experession: str) -> List[Any]:
        pass


class AbstractException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message