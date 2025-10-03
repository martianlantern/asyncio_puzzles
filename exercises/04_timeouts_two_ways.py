"""
Exercise 04: Timeouts - wait_for vs asyncio.timeout

OBJECTIVE:
Learn two ways to implement timeouts: asyncio.wait_for() and
asyncio.timeout() context manager. Understand exception handling for both.

TASK:
Implement timeouts using both approaches and handle exceptions correctly.
The slow_task should be cancelled when it times out.

HINT: wait_for raises asyncio.TimeoutError, timeout context manager also
raises TimeoutError. The task receives CancelledError internally.
"""

import asyncio
import sys


async def slow_task(duration, name):
    """A task that takes a long time."""
    try:
        print(f"  {name}: Starting work (will take {duration}s)...")
        await asyncio.sleep(duration)
        print(f"  {name}: Finished!")
        return f"result_{name}"
    except asyncio.CancelledError:
        print(f"  {name}: Got CancelledError, cleaning up...")
        raise
    finally:
        print(f"  {name}: Finally block executed")


async def timeout_with_wait_for():
    """
    Use asyncio.wait_for to timeout a slow task.
    
    TODO: Wrap slow_task with wait_for and handle the timeout.
    """
    print("Method 1: Using wait_for()...")
    
    try:
        # TODO: Use asyncio.wait_for to timeout after 0.2 seconds
        # The task takes 1 second but should timeout at 0.2s
        result = await asyncio.wait_for(slow_task(1, "task_A"), timeout=0.2)
        return result
    except asyncio.TimeoutError:
        print("  ✓ Caught TimeoutError from wait_for")
        return None


async def timeout_with_context_manager():
    """
    Use asyncio.timeout context manager to timeout a slow task.
    
    TODO: Use asyncio.timeout() context manager (Python 3.11+).
    For older Python, use asyncio.wait_for instead.
    """
    print("\nMethod 2: Using timeout context manager...")
    
    # Check Python version
    if sys.version_info < (3, 11):
        print("  (Skipping - requires Python 3.11+, falling back to wait_for)")
        return await timeout_with_wait_for()
    
    try:
        # TODO: Use async with asyncio.timeout(0.2) to timeout
        async with asyncio.timeout(0.2):
            result = await slow_task(1, "task_A")
        return result
    except TimeoutError:  # Note: TimeoutError, not asyncio.TimeoutError in 3.11+
        print("  ✓ Caught TimeoutError from context manager")
        return None
