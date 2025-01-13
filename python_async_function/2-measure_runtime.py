#!/usr/bin/env python3
import asyncio
import time
from typing import List
from _0_basic_async_syntax_ import wait_random
from 1-concurrent_coroutines_ import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the tiem it takes to run `wait_n` coroutines with `n` coroutines
    and `max_delay` seconds or delays.

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        float: _description_
    """
    
    start_time: float = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time: float = time.time()

    total_time: float = end_time - start_time
    return total_time / n
