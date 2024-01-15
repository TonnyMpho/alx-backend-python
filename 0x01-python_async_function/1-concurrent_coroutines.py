#!/usr/bin/env python3
""" multiple coroutines """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    values = []

    for _ in range(n):
        values.append(await asyncio.create_task(wait_random(max_delay)))
    return sorted(values)
