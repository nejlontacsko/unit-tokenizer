import re
import utils


class UnitTokenizer:
    def __init__(self, unit_string):
        self.unit_string = unit_string

    def tokenize(self):
        parts = self.tokenize_with_whitespace()
        tokens = [self.split_prefix_and_unit(part) for part in parts]
        return tokens

    def coarse_tokenize(self, raw):
        pattern = r'[a-zA-ZμΩ]+|\^?[-+]?\d+|[*\/()]|√'
        return re.findall(pattern, raw)

    def tokenize_with_whitespace(self):
        parts = self.unit_string.split()
        tokens = [self.coarse_tokenize(part) for part in parts]
        return utils.flatten(tokens)

    def split_prefix_and_unit(self, raw):
        if len(raw) == 1:
            return ["1", raw]

        prefixes = ["p", "n", "μ", "u", "m", "c", "dk", "da", "d", "h", "k", "M", "G", "T"]
        for prefix in prefixes:
            if raw.startswith(prefix):
                return [prefix, raw[len(prefix):]]

        return ["0", raw]

