#!/usr/bin/env python3
"""
contains async_comprehension coroutine
"""

from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    returns a list of floats
    """
    nums = []
    async for num in async_generator():
        nums.append(num)
    return nums
