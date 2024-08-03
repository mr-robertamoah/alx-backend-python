#!/usr/bin/env python3
"""
contains annotated to_kv funciton
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a turple containing a string and float
    """
    return (k, v**2)
