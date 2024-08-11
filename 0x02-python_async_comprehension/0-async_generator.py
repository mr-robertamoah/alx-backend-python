#!/usr/bin/env python3
"""
contains async_generator coroutine
"""

import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    sleeps for a second and yields random float
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
