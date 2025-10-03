"""
Exercise 02: Coroutines vs Tasks - Fire & Await

OBJECTIVE:
Understand the difference between awaiting a coroutine directly vs
creating a task that runs concurrently.

TASK:
Implement two functions:
1. run_sequential: Await three coroutines one after another
2. run_concurrent: Create tasks for all three and await them together

The concurrent version should be much faster (roughly max of times, not sum).

HINT: Use asyncio.create_task() to schedule coroutines concurrently.
"""

import asyncio


async def fetch_data(name, delay):
    """Simulates fetching data with a delay."""
    print(f"  Fetching {name}...")
    await asyncio.sleep(delay)
    print(f"  Got {name}!")
    return f"data_{name}"


async def run_sequential():
    """
    Run three fetches sequentially (one after another).
    
    TODO: Implement sequential execution using direct await.
    """
    print("Running sequentially...")
    results = []
    
    # TODO: Await each fetch one by one
    # Replace these lines:
    pass
    pass
    pass
    
    return results


async def run_concurrent():
    """
    Run three fetches concurrently using tasks.
    
    TODO: Implement concurrent execution using asyncio.create_task().
    """
    print("Running concurrently...")
    results = []
    
    # TODO: Create tasks for each fetch and await them all
    # Hint: Create three tasks, then await them
    pass
    
    return results
