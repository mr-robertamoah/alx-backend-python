#!/usr/bin/env python3

"""
contains an async task_wait_n function
"""

from typing import List
import asyncio


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns a sorted list of delays
    """

    delays = await asyncio.gather(
        *list(map(lambda i: task_wait_random(max_delay), range(n)))
    )
    return sorted(delays)
