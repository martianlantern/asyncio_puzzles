"""
Exercise 01: Event Loop Basics - Yield or Starve

OBJECTIVE:
Understand why the event loop can't preempt a running coroutine and learn
how to make long-running operations "cooperative" by yielding control.

TASK:
You have two coroutines:
1. A busy worker that loops N times doing computation
2. A ticker that should print ticks every ~10ms

Currently, the ticker doesn't run until the busy worker finishes.
Fix the busy_worker to yield control periodically so both run concurrently.

HINT: Use `await asyncio.sleep(0)` to yield control back to the event loop.
"""

import asyncio


async def ticker():
    """Prints a tick every ~10ms."""
    for i in range(5):
        print(f"  tick {i}")
        await asyncio.sleep(0.01)


async def busy_worker(n):
    """
    Does busy work for n iterations.
    
    TODO: Add cooperative yielding so the ticker can run!
    Hint: Yield every 100 iterations or so with `await asyncio.sleep(0)`
    """
    print("Starting busy work...")
    for i in range(n):
        # Simulate CPU-bound work
        _ = sum(range(100))
        
        # TODO: Add your code here to yield control periodically
        # Replace this pass statement
        pass
        
    print("Busy work done!")


async def main():
    """Run both coroutines concurrently."""
    # Start both tasks
    ticker_task = asyncio.create_task(ticker())
    worker_task = asyncio.create_task(busy_worker(10000))
    
    # Wait for both to complete
    await ticker_task
    await worker_task
