"""
Exercise 03: gather vs as_completed - Ordering Games

OBJECTIVE:
Learn the difference between asyncio.gather() (preserves order) and
asyncio.as_completed() (completion order).

TASK:
Run three tasks with different delays using both gather and as_completed.
Observe that gather returns results in the original order, while
as_completed yields results as they complete.

HINT: Use asyncio.gather() for ordered results and asyncio.as_completed() for
completion order iteration.
"""

import asyncio


async def delayed_task(name, delay):
    """A task that completes after a specific delay."""
    await asyncio.sleep(delay)
    print(f"  {name} completed (after {delay}s)")
    return name


async def use_gather():
    """
    Use asyncio.gather to run tasks and get results in order.
    
    TODO: Implement using asyncio.gather()
    """
    print("Using gather()...")
    
    # TODO: Use gather to run three tasks with delays: 0.3, 0.1, 0.2
    # Tasks: ("task_A", 0.3), ("task_B", 0.1), ("task_C", 0.2)
    results = await asyncio.gather(
        delayed_task("task_A", 0.3),
        delayed_task("task_B", 0.1),
        delayed_task("task_C", 0.2),
    )
    
    return results


async def use_as_completed():
    """
    Use asyncio.as_completed to process results as they complete.
    
    TODO: Implement using asyncio.as_completed()
    """
    print("\nUsing as_completed()...")
    
    # TODO: Use as_completed to iterate over tasks as they finish
    # Same tasks: ("task_A", 0.3), ("task_B", 0.1), ("task_C", 0.2)
    results = [await coro for coro in asyncio.as_completed(
        [
            delayed_task("task_A", 0.3),
            delayed_task("task_B", 0.1),
            delayed_task("task_C", 0.2),
        ]
    )]
    
    # Hint: for coro in asyncio.as_completed([...]): result = await coro
    
    return results
