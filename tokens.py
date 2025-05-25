from enum import Enum

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


class TokenTypeEnum(Enum):
    Unknown = 0
    Number = 1
    Operator = 2
    Dimension = 3

    def __str__(self):
        return f"{self.name[:3]}"
