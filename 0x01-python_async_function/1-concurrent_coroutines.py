#!/usr/bin/env python3

"""
contains an async wait_n function
"""

from typing import List
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns a sorted list of delays
    """

    delays = await asyncio.gather(
        *list(map(lambda i: wait_random(max_delay), range(n)))
    )
    return sorted(delays)
