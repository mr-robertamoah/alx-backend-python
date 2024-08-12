#!/usr/bin/env python3
"""
contains measure_runtime coroutine
"""

from importlib import import_module as using
import time
import asyncio


async_comprehension = using("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    returns the time taken to run 4 async_comprehension coroutines
    """
    start_time = time.time()
    await asyncio.gather(
        *list(async_comprehension() for i in range(4))
    )
    return (time.time() - start_time)
