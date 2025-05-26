from __future__ import annotations

from tokens.tokens import UnitToken


class Fraction:
    def __init__(self,
            numerator = UnitToken.one(),
            denominator = UnitToken.one()):
        self.numerators = [numerator]
        self.denominators = [denominator]

    def inverse(self) -> Fraction:
        frac = Fraction()
        for numerator in self.numerators:
            frac.append_denominator(numerator)
        for denominator in self.denominators:
            frac.append_numerator(denominator)
        return frac

    # Multiplication with a single value
    def append_numerator(self, numerator: UnitToken):
        self.numerators.append(numerator)

    # Division with a single value
    def append_denominator(self, denominator: UnitToken):
        self.denominators.append(denominator)

    # Multiplication with another fraction
    def append_fraction(self, fraction: Fraction):
        self.numerators.extend(fraction.numerators)
        self.denominators.extend(fraction.denominators)

    # Division with another fraction
    def append_inverse_fraction(self, fraction: Fraction):
        self.append_fraction(fraction.inverse())

    def __str__(self):
        numerator_str = ""
        denominator_str = ""
        for numerator in self.numerators:
            numerator_str += f"{repr(numerator)} "
        for denominator in self.denominators:
            denominator_str += f"{repr(denominator)} "

        line_len = max(len(numerator_str), len(denominator_str))
        return f"/ {numerator_str} \\\n| {"-" * line_len} |\n\\ {denominator_str} /"