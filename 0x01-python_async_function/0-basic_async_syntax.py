#!/usr/bin/env python3

"""
contains an async wait_random function
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random number of seconds
    """
    seconds = random.random() * max_delay
    await asyncio.sleep(seconds)
    return seconds
