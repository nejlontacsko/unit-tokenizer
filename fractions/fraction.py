from __future__ import annotations

from tokens.token_list import TokenList
from tokens.tokens import UnitToken


class Fraction:
    def __init__(self,
            numerator = UnitToken.one(),
            denominator = UnitToken.one()):
        self.numerators = [numerator]
        self.denominators = [denominator]

    @staticmethod
    def from_lists(num: TokenList, den: TokenList) -> Fraction:
        f = Fraction()
        if len(num.tokens) > 0:
            f.numerators = num.tokens
        if len(den.tokens) > 0:
            f.denominators = den.tokens
        return f

    # TODO: Need to reconsider. Use Mul or have tuples of dim+exp?
    """
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
    """

    def __str__(self):
        numerator_str = " ".join(repr(n) for n in self.numerators)
        denominator_str = " ".join(repr(d) for d in self.denominators)
        line_len = max(len(numerator_str), len(denominator_str))
        return (
            f"\t/ {numerator_str.center(line_len)} \\\n"
            f"\t| {'-' * line_len} |\n"
            f"\t\\ {denominator_str.center(line_len)} /"
        )