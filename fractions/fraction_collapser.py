from fractions.fraction import Fraction
from prefixes.prefix_utils import SiPrefixUtils
from tokens.tokens import TokenTypeEnum


class FractionCollapser:
    def __init__(self, fraction: Fraction):
        self.fraction = fraction

        self.num_prefixes = []
        self.den_prefixes = []

    @staticmethod
    def collect_prefixes(source, target):
        for token in source:
            if token.type == TokenTypeEnum.Dimension:
                prefix = token.value.prefix
                if prefix != "1":
                    target.append(SiPrefixUtils.from_symbol(prefix))
                    token.value.prefix = "1" # removing the prefix from the dims

    def collapse_prefixes(self):
        self.collect_prefixes(self.fraction.numerators, self.num_prefixes)
        self.collect_prefixes(self.fraction.denominators, self.den_prefixes)

        exponent = 0.0
        exponent += sum(p.value.exponent for p in self.num_prefixes)
        exponent -= sum(p.value.exponent for p in self.den_prefixes)

        print("Exponent:", exponent)


    def collapse_dimensions(self):
        dimensions = []