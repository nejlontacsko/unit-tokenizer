import itertools
from typing import List, Optional, Any


def flatten(list_of_lists):
    return list(itertools.chain.from_iterable(list_of_lists))


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def match_pattern_and_remove(tokens: List[Any], pattern: List[Any]) -> Optional[Any]:
    n = len(pattern)
    for i in range(len(tokens) - n + 1):
        if tokens[i:i + n] == pattern:
            if i > 0:
                before = tokens[i - 1]
                del tokens[i - 1:i + n]
                return before
            else:
                del tokens[i:i + n]
                return None
    return None