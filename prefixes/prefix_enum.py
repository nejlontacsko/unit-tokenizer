from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class PrefixInfo:
    symbol: str
    exponent: int


class SiPrefixEnum(Enum):
    QUECTO = PrefixInfo('q', -30)
    RONTO = PrefixInfo('r', -27)
    YOCTO = PrefixInfo('y', -24)
    ZEPTO = PrefixInfo('z', -21)
    ATTO  = PrefixInfo('a', -18)
    FEMTO = PrefixInfo('f', -15)
    PICO  = PrefixInfo('p', -12)
    NANO  = PrefixInfo('n', -9)
    MICRO = PrefixInfo('µ', -6)
    MILLI = PrefixInfo('m', -3)
    CENTI = PrefixInfo('c', -2)
    DECI  = PrefixInfo('d', -1)
    NONE  = PrefixInfo('', 0)
    DECA  = PrefixInfo('da', 1)
    HECTO = PrefixInfo('h', 2)
    KILO  = PrefixInfo('k', 3)
    MEGA  = PrefixInfo('M', 6)
    GIGA  = PrefixInfo('G', 9)
    TERA  = PrefixInfo('T', 12)
    PETA  = PrefixInfo('P', 15)
    EXA   = PrefixInfo('E', 18)
    ZETTA = PrefixInfo('Z', 21)
    YOTTA = PrefixInfo('Y', 24)
    RONNA = PrefixInfo('R', 27)
    QUETTA = PrefixInfo('Q', 30)

SYMBOL_TO_ENUM = {p.value.symbol: p for p in SiPrefixEnum}
EXPONENT_TO_ENUM = {p.value.exponent: p for p in SiPrefixEnum}
