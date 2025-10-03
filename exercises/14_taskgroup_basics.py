"""
Exercise 14: TaskGroup Basics - Structured Concurrency

OBJECTIVE:
Learn to use asyncio.TaskGroup (Python 3.11+) for structured concurrency
where failures in one task affect sibling tasks.

TASK:
Use TaskGroup to run multiple tasks. When one fails, observe that
siblings are cancelled and the failure propagates as ExceptionGroup.

HINT: Use `async with asyncio.TaskGroup() as tg:` and `tg.create_task()`
For Python < 3.11, we'll provide a fallback.
"""

import asyncio
import sys


async def successful_task(name, duration):
    """A task that completes successfully."""
    print(f"  {name}: Starting (duration {duration}s)")
    await asyncio.sleep(duration)
    print(f"  {name}: Completed!")
    return f"result_{name}"


async def failing_task(name, delay):
    """A task that fails after a delay."""
    print(f"  {name}: Starting (will fail after {delay}s)")
    await asyncio.sleep(delay)
    print(f"  {name}: Raising exception!")
    raise ValueError(f"{name} failed!")


async def run_with_taskgroup():
    """
    Run tasks using TaskGroup.
    
    TODO: Use TaskGroup to run tasks. Handle ExceptionGroup on failure.
    """
    if sys.version_info < (3, 11):
        print("  (TaskGroup requires Python 3.11+, using gather fallback)")
        # Fallback for older Python
        try:
            results = await asyncio.gather(
                successful_task("Task-A", 0.1),
                failing_task("Task-B", 0.15),
                successful_task("Task-C", 0.3),
                return_exceptions=False,
            )
            return results
        except Exception as e:
            print(f"  Caught exception: {e}")
            raise
    
    # TODO: Use TaskGroup for Python 3.11+
    # async with asyncio.TaskGroup() as tg:
    #     tg.create_task(successful_task("Task-A", 0.1))
    #     tg.create_task(failing_task("Task-B", 0.15))
    #     tg.create_task(successful_task("Task-C", 0.3))
    
    pass  # Replace this
