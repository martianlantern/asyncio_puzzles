"""
Exercise 15: TaskGroup vs gather - Failure Semantics

OBJECTIVE:
Understand the different error handling semantics between TaskGroup
and gather with return_exceptions.

TASK:
Run the same set of tasks using both TaskGroup and gather, and observe:
- TaskGroup: Cancels all siblings on first failure, raises ExceptionGroup
- gather(return_exceptions=True): Lets all tasks complete, returns exceptions as values

HINT: Use return_exceptions=True with gather to get different behavior.
"""

import asyncio
import sys
import time


async def task_work(name, duration, should_fail=False):
    """A task that either succeeds or fails."""
    try:
        print(f"  {name}: Starting (duration {duration}s)")
        await asyncio.sleep(duration)
        
        if should_fail:
            print(f"  {name}: Failing!")
            raise ValueError(f"{name} error")
        
        print(f"  {name}: Completed successfully")
        return f"result_{name}"
    except asyncio.CancelledError:
        print(f"  {name}: Cancelled by sibling failure!")
        raise


async def test_with_taskgroup():
    """
    Test failure handling with TaskGroup.
    
    TODO: Implement using TaskGroup (or gather without return_exceptions for fallback).
    """
    print("Method 1: TaskGroup (cancels siblings on failure)")
    
    if sys.version_info < (3, 11):
        print("  (Using gather without return_exceptions as fallback)")
        try:
            results = await asyncio.gather(
                task_work("TG-A", 0.1, False),
                task_work("TG-B", 0.15, True),  # This fails
                task_work("TG-C", 0.5, False),  # Should be cancelled
            )
            return results
        except Exception as e:
            return e
    
    # TODO: Use TaskGroup for Python 3.11+
    # try:
    #     async with asyncio.TaskGroup() as tg:
    #         tg.create_task(task_work("TG-A", 0.1, False))
    #         tg.create_task(task_work("TG-B", 0.15, True))
    #         tg.create_task(task_work("TG-C", 0.5, False))
    # except (ExceptionGroup, ValueError) as e:
    #     return e
    
    pass  # Replace this


async def test_with_gather():
    """
    Test failure handling with gather(return_exceptions=True).
    
    TODO: Implement using gather with return_exceptions=True.
    """
    print("\nMethod 2: gather(return_exceptions=True) (all tasks complete)")
    
    # TODO: Use gather with return_exceptions=True
    # results = await asyncio.gather(
    #     task_work("G-A", 0.1, False),
    #     task_work("G-B", 0.15, True),  # This fails
    #     task_work("G-C", 0.5, False),  # Should still complete!
    #     return_exceptions=True
    # )
    results = []  # Replace this
    
    return results
