#!/usr/bin/env python3
"""
contains async_comprehension coroutine
"""

from typing import List
from importlib import import_module as using


async_generator = using("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    returns a list of floats
    """
    nums = []
    async for num in async_generator():
        nums.append(num)
    return nums
