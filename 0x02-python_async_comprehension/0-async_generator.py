#!/usr/bin/env python3
"""
contains async_generator coroutine
"""

import asyncio
import random


async def async_generator():
    """
    sleeps for a second and yields random float
    """
    await asyncio.sleep(1)
    yield random.random() * 10
