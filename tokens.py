from __future__ import annotations

from enum import Enum


class TokenTypeEnum(Enum):
    Unknown = 0
    Number = 1
    Operator = 2
    Dimension = 3

    def __str__(self):
        return f"{self.name[:3]}"

class DimToken:
    def __init__(self, prefix, unit):
        self.prefix = prefix
        self.unit = unit

    def __repr__(self):
        return f"({self.prefix}*{self.unit})"

class UnitToken:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"

    def __eq__(self, other):
        if isinstance(other, UnitToken):
            return self.type == other.type and self.value == other.value
        return False

    @staticmethod
    def one() -> UnitToken:
        return UnitToken(TokenTypeEnum.Number, "1")

    @staticmethod
    def pow() -> UnitToken:
        return UnitToken(TokenTypeEnum.Operator, "^")

    @staticmethod
    def mul() -> UnitToken:
        return UnitToken(TokenTypeEnum.Operator, "*")

    @staticmethod
    def div() -> UnitToken:
        return UnitToken(TokenTypeEnum.Operator, "/")

    @staticmethod
    def sqrt() -> UnitToken:
        return UnitToken(TokenTypeEnum.Operator, "√")
