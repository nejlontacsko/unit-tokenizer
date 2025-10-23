from fractions.fraction import Fraction

from tokens.token_list import TokenList

from tokens.token_matcher import *
from tokens.tokens import *


def skip_if_no_tokens(func):
    def wrapper(self, *args, **kwargs):
        if not getattr(self.token_list, "tokens", None):
            printer = getattr(self, "print", print)
            printer(f"Skipping {func.__name__} — no tokens found.")
            return None
        return func(self, *args, **kwargs)
    return wrapper


class FractionBuilder:
    def __init__(self, token_list: TokenList, show_info = False):
        self.fraction = Fraction()
        self.token_list = token_list
        self.show_info = show_info

        self.nom = TokenList([])
        self.den = TokenList([])

    def print(self, txt):
        if self.show_info:
            print(txt)

    @skip_if_no_tokens
    def find_nominators(self):
        self.print("NOM Finding complete nominators...")
        pattern = [
            ExactMatch(UnitToken.pow()),
            PositiveMatch(),
            OptionalMatch(ExactMatch(UnitToken.mul()))
        ]
        self.find_part(pattern, self.nom)

    @skip_if_no_tokens
    def find_denominators(self):
        self.print("DEN Finding denominators...")
        pattern = [
            ExactMatch(UnitToken.pow()),
            NegativeMatch(),
            OptionalMatch(ExactMatch(UnitToken.mul()))
        ]
        self.find_part(pattern, self.den)

        # All the exponent need to be positive in den considering they were added by a negative filter.
        for d in self.den.tokens:
            if d.type == TokenTypeEnum.Number:
                d.value = d.value.lstrip('-')

    @skip_if_no_tokens
    def digest_remaining(self):
        self.print("REM Digesting remaining incomplete nominators...")
        pattern = [
            TypeMatch(UnitToken.dim()),
            OptionalMatch(ExactMatch(UnitToken.mul()))
        ]

        # Extend to complete nominators
        rem = TokenList([])
        self.find_part(pattern, rem)
        rem.do_replacements()
        self.nom.tokens.extend(rem.tokens)

    def find_part(self, pattern, target: TokenList):
        found = UnitToken(TokenTypeEnum.Dimension, DimToken("place", "holder"))
        while found and len(self.token_list.tokens) > 0:
            plen = len(pattern)
            result = match_pattern_prev_index(self.token_list.tokens, pattern)
            if result is not None:
                result += 1 if plen < 3 else 0
                found = self.token_list.tokens[result]
                exponent = abs(float(self.token_list.tokens[result + 2].value)) if plen > 2 else 0.0
                target.tokens.extend(self.token_list.tokens[result:(result + plen)] + [UnitToken.mul()])
                del self.token_list.tokens[result:(result + plen)]
                self.print(f">> Index: {result} > Found {found} with exponent {exponent}")
            else:
                found = None
                exponent = 0.0

            self.token_list.remove_duplicates()
            self.token_list.trim_operators()
            self.print(f">>\t\tremain: {self.token_list.tokens}")

        target.remove_duplicates()
        target.trim_operators()
        self.print(f"REMAIN: {self.token_list.tokens}")

    def build(self):
        self.print("Building fraction...")
        return Fraction.from_lists(self.nom, self.den)