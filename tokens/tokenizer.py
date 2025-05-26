import re
import utils
from tokens.tokens import *


class UnitTokenizer:
    def __init__(self):
        self.unit_string = ""
        self.known_compounds = [
            "cd", "Torr", "Pa", "furlong"
        ]

    @staticmethod
    def coarse_tokenize(raw):
        pattern = r'\d+\.\d+|[-+]?\d+|[a-zA-ZμΩ]+|\^|[*\/()]|√'
        return re.findall(pattern, raw)

    @staticmethod
    def split_prefix_and_unit(raw):
        # Handle numbers first
        if utils.is_number(raw):
            return UnitToken(TokenTypeEnum.Number, raw)

        # Handle the 1 character long tokens
        if len(raw) == 1:
            if raw.isalpha():
                return UnitToken(TokenTypeEnum.Dimension, DimToken("1", raw))
            else:
                return UnitToken(TokenTypeEnum.Operator, raw)

        # Handle the longer tokens
        #  at first let's try to find prefixes
        prefixes = ["f", "p", "n", "μ", "u", "m", "c", "dk", "da", "d", "h", "k", "M", "G", "T", "P"]
        for prefix in prefixes:
            if raw.startswith(prefix):
                return UnitToken(TokenTypeEnum.Dimension, DimToken(prefix, raw[len(prefix):]))

        # If no prefix was found, let's try to find a unit's name
        if raw.isalpha():
            return UnitToken(TokenTypeEnum.Dimension, DimToken("1", raw))

        return UnitToken(TokenTypeEnum.Unknown, raw)

    def tokenize_with_whitespace(self):
        parts = self.unit_string.split()
        tokens = [self.coarse_tokenize(part) for part in parts]
        return utils.flatten(tokens)

    def tokenize(self):
        parts = self.tokenize_with_whitespace()

        # Handle the case when the first letter of a unit is also a symbol for a prefix
        compound_tokens, indices, remaining_parts = self.filter_compound_tokens(parts)

        #tokens += [self.split_prefix_and_unit(part) for part in parts]
        compound_map = dict(zip(indices, compound_tokens))
        tokens = []
        j = 0
        for i in range(len(remaining_parts) + len(indices)):
            if i in compound_map:
                tokens.append(compound_map[i])
            else:
                tokens.append(self.split_prefix_and_unit(remaining_parts[j]))
                j += 1

        return tokens
        return tokens

    def filter_compound_tokens(self, parts):
        matched_compounds = []
        indices = []
        filtered_list = []

        for i in range(len(parts)):
            if parts[i] in self.known_compounds:
                matched_compounds.append(parts[i])
                indices.append(i)
            else:
                filtered_list.append(parts[i])

        tokens = []
        for compound in matched_compounds:
            tokens.append(UnitToken(TokenTypeEnum.Dimension, DimToken("1", compound)))

        return tokens, indices, filtered_list

