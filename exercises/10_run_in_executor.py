"""
Exercise 10: run_in_executor - Offload the CPU

OBJECTIVE:
Keep the event loop responsive by offloading CPU-bound work to a thread pool.

TASK:
Run a CPU-intensive function in an executor while keeping a ticker responsive.
Without the executor, the ticker would freeze during the CPU work.

HINT: Use loop.run_in_executor(None, func, args...) or asyncio.to_thread (3.9+)
"""

import asyncio
import time
import hashlib


def cpu_intensive_work(n):
    """
    A CPU-bound function (blocks the event loop if run directly).
    This computes hashes in a loop - very CPU intensive!
    """
    print("  CPU work starting...")
    result = []
    for i in range(n):
        # Compute hash (CPU intensive)
        h = hashlib.sha256(f"data_{i}".encode()).hexdigest()
        result.append(h)
    print("  CPU work done!")
    return len(result)


async def ticker(duration, tick_times):
    """Prints ticks to show the event loop is responsive."""
    start = time.time()
    tick_count = 0
    while time.time() - start < duration:
        tick_times.append(time.time())
        print(f"  tick {tick_count}")
        tick_count += 1
        await asyncio.sleep(0.05)
    return tick_count


async def run_cpu_work_blocking(n):
    """
    BAD: Runs CPU work directly, blocking the event loop.
    
    DO NOT CHANGE THIS METHOD - it demonstrates the problem.
    """
    # This blocks the event loop!
    return cpu_intensive_work(n)


async def run_cpu_work_offloaded(n):
    """
    GOOD: Offloads CPU work to a thread pool.
    
    TODO: Use run_in_executor to run cpu_intensive_work without blocking.
    """
    loop = asyncio.get_event_loop()
    
    # TODO: Use run_in_executor to run cpu_intensive_work in a thread
    # result = await loop.run_in_executor(None, cpu_intensive_work, n)
    result = None  # Replace this
    
    return result
