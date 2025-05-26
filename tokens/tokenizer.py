import re
import utils
from tokens.tokens import *


class UnitTokenizer:
    def __init__(self):
        self.unit_string = ""

    @staticmethod
    def coarse_tokenize(raw):
        pattern = r'\d+\.\d+|[-+]?\d+|[a-zA-ZμΩ]+|\^|[*\/()]|√'
        return re.findall(pattern, raw)

    @staticmethod
    def split_prefix_and_unit(raw):
        if utils.is_number(raw):
            return UnitToken(TokenTypeEnum.Number, raw)

        if len(raw) == 1:
            if raw.isalpha():
                return UnitToken(TokenTypeEnum.Dimension, DimToken("1", raw))
            else:
                return UnitToken(TokenTypeEnum.Operator, raw)

        prefixes = ["p", "n", "μ", "u", "m", "c", "dk", "da", "d", "h", "k", "M", "G", "T"]
        for prefix in prefixes:
            if raw.startswith(prefix):
                return UnitToken(TokenTypeEnum.Dimension, DimToken(prefix, raw[len(prefix):]))

        return UnitToken(TokenTypeEnum.Unknown, raw)

    def tokenize_with_whitespace(self):
        parts = self.unit_string.split()
        tokens = [self.coarse_tokenize(part) for part in parts]
        return utils.flatten(tokens)

    def tokenize(self):
        parts = self.tokenize_with_whitespace()
        tokens = [self.split_prefix_and_unit(part) for part in parts]
        return tokens
