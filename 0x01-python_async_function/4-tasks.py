#!/usr/bin/env python3
""" multiple coroutines """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutines at the same time with async
    """
    values = []

    for _ in range(n):
        values.append(await task_wait_random(max_delay))
    return sorted(values)
