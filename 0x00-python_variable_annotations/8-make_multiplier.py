#!/usr/bin/env python3
"""
contains type-annotated make_multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function which returns the product of multiplier
    and its argument
    """

    def f(n: float) -> float:
        """
        returns a product of multiplier and n
        """
        return float(n * multiplier)

    return f
