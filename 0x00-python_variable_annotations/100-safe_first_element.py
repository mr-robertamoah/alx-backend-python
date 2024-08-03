#!/usr/bin/env python3
"""
containing type-annotated safe_first_element function
"""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return any type or none
    """

    if lst:
        return lst[0]
    else:
        return None
