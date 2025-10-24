from prefixes.prefix_enum import SiPrefixEnum, SYMBOL_TO_ENUM, EXPONENT_TO_ENUM


class SiPrefixUtils:
    """Helper class to handle SI prefixes."""

    @staticmethod
    def from_symbol(symbol: str) -> SiPrefixEnum | None:
        """Symbol → Enum"""
        return SYMBOL_TO_ENUM.get(symbol)

    @staticmethod
    def from_exponent(exponent: int) -> SiPrefixEnum | None:
        """Exponent → Enum"""
        return EXPONENT_TO_ENUM.get(exponent)

    @staticmethod
    def from_name(name: str) -> SiPrefixEnum | None:
        """Enum name (pl. 'KILO') → Enum"""
        try:
            return SiPrefixEnum[name.upper()]
        except KeyError:
            return None

    @staticmethod
    def to_symbol(item: SiPrefixEnum | str | int) -> str | None:
        """Enum / name / exponent → symbol"""
        if isinstance(item, SiPrefixEnum):
            return item.value.symbol
        elif isinstance(item, str):
            if item in SYMBOL_TO_ENUM:
                return item
            prefix = SiPrefixUtils.from_name(item)
            return prefix.value.symbol if prefix else None
        elif isinstance(item, int):
            prefix = SiPrefixUtils.from_exponent(item)
            return prefix.value.symbol if prefix else None

    @staticmethod
    def to_exponent(item: SiPrefixEnum | str) -> int | None:
        """Enum / symbol / name → exponent"""
        if isinstance(item, SiPrefixEnum):
            return item.value.exponent
        elif isinstance(item, str):
            prefix = (
                SYMBOL_TO_ENUM.get(item)
                or SiPrefixUtils.from_name(item)
            )
            return prefix.value.exponent if prefix else None

    @staticmethod
    def all_symbols() -> list[str]:
        """All the prefix symbols (unordered)."""
        return list(SYMBOL_TO_ENUM.keys())

    @staticmethod
    def sorted_by_exponent(descending: bool = True) -> list[SiPrefixEnum]:
        """All the prefix enums ordered by the exponent."""
        return sorted(SiPrefixEnum, key=lambda p: p.value.exponent, reverse=descending)