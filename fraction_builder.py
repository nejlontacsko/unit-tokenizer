from fraction import Fraction
from token_list import TokenList
from token_matcher import match_pattern_prev_index, ExactMatch, NegativeMatch, OptionalMatch, PositiveMatch
from tokens import UnitToken, TokenTypeEnum, DimToken


class FractionBuilder:
    def __init__(self, token_list: TokenList):
        self.fraction = Fraction()
        self.token_list = token_list

    def find_nominators(self):
        print(">> Finding nominators")
        pattern = [
            ExactMatch(UnitToken.pow()),
            PositiveMatch(),
            #OptionalMatch(ExactMatch(UnitToken.mul()))
        ]
        self.find_part(pattern)

    def find_denominators(self):
        print(">> Finding denominators")
        pattern = [
            ExactMatch(UnitToken.pow()),
            NegativeMatch(),
            #OptionalMatch(ExactMatch(UnitToken.mul()))
        ]
        self.find_part(pattern)

    def find_part(self, pattern):
        found = UnitToken(TokenTypeEnum.Dimension, DimToken("place", "holder"))
        while found and len(self.token_list.tokens) > 0:
            result = match_pattern_prev_index(self.token_list.tokens, pattern)
            if result is not None:
                found = self.token_list.tokens[result]
                exponent = abs(float(self.token_list.tokens[result + 2].value))
                del self.token_list.tokens[result:result + 3]
                print(f">> Index: {result} > Found {found} with exponent {exponent}")
            else:
                found = None
                exponent = 0.0
            self.token_list.remove_duplicates()
            self.token_list.trim_operators()
            print(f">>\t\tremain: {self.token_list.tokens}")