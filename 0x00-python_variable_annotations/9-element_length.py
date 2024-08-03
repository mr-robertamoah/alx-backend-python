#!/usr/bin/env python3
"""
contains a type-annotated element_length function
"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of turples
    """
    return [(i, len(i)) for i in lst]
