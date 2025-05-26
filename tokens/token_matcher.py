from typing import List, Optional, Tuple
from tokens.tokens import *


class TokenPattern:
    """Abstract element. Concretization by inheriting into pattern matching logics."""
    def matches(self, token: UnitToken) -> bool:
        raise NotImplementedError()

class ExactMatch(TokenPattern):
    """Exact matching with a UnitToken. Uses the __eq__ operator."""
    def __init__(self, token: UnitToken):
        self.token = token

    def matches(self, token: Optional[UnitToken]) -> bool:
        if token is None:
            return False
        return token == self.token

    def __repr__(self):
        return f"ExactMatch({self.token})"


class NegativeMatch(TokenPattern):
    """Recognition of Negative number typed token, even if it is a string or float."""
    def matches(self, token: Optional[UnitToken]) -> bool:
        if token is None:
            return False
        if token.type != TokenTypeEnum.Number:
            return False
        val = token.value
        if isinstance(val, str):
            return val.strip().startswith("-")
        elif isinstance(val, (int, float)):
            return float(val) < 0
        return False

    def __repr__(self):
        return "NegativeMatch()"

class PositiveMatch(TokenPattern):
    """Recognition of Positive number typed token, even if it is a string or float."""
    def matches(self, token: Optional[UnitToken]) -> bool:
        if token is None:
            return False
        if token.type != TokenTypeEnum.Number:
            return False
        val = token.value
        if isinstance(val, str):
            return not val.strip().startswith("-")
        elif isinstance(val, (int, float)):
            return float(val) >= 0
        return False


class OptionalMatch(TokenPattern):
    """Optional pattern, barely working right now :("""
    def __init__(self, matcher: TokenPattern):
        self.matcher = matcher

    def matches(self, token: Optional[UnitToken]) -> bool:
        if token is None:
            return True
        return self.matcher.matches(token)

    def __repr__(self):
        return f"OptionalMatch({self.matcher})"



def match_pattern_prev_index(tokens: List[UnitToken], pattern: List[TokenPattern]):
    max_len = len(tokens)

    for start in range(max_len):
        for end in range(start + 1, max_len + 1):
            window = tokens[start:end]
            match = True
            for i, matcher in enumerate(pattern):
                if i >= len(window):
                    token = None
                else:
                    token = window[i]
                if not matcher.matches(token):
                    match = False
                    break

            if match:
                # before = tokens[start - 1] if start > 0 else None
                return start - 1
    return None