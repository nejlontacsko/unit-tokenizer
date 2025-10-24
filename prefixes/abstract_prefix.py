from abc import ABC, abstractmethod

from prefixes.prefix_enum import SiPrefixEnum


class AbstractPrefix(ABC):
    @property
    @abstractmethod
    def symbol(self) -> str: ...

    @property
    @abstractmethod
    def exponent(self) -> int: ...


class SiPrefixWrapper(AbstractPrefix):
    """Wrapper for the enum of known prefixes."""
    def __init__(self, enum: SiPrefixEnum):
        self._enum = enum

    @property
    def symbol(self) -> str:
        return self._enum.value.symbol

    @property
    def exponent(self) -> int:
        return self._enum.value.exponent


class GenericPrefix(AbstractPrefix):
    """Used for Non-standard exponent values."""
    def __init__(self, exponent: int):
        self._exponent = exponent

    @property
    def symbol(self) -> str:
        return f"10^{self._exponent}"

    @property
    def exponent(self) -> int:
        return self._exponent