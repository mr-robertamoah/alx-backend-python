#!/usr/bin/env python3
"""
contains annotated sum_mixed_list function
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns sum of ints and floats as a float
    """
    return sum(mxd_lst)
