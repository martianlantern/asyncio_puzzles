"""
Exercise 09: Locks and Deadlocks - The Footgun

OBJECTIVE:
Understand how improper lock usage can cause deadlocks, and learn patterns
to avoid them.

TASK:
Fix a deadlock scenario where holding a lock while awaiting can cause issues.
The pattern: acquire lock, copy data out, release lock, THEN do async work.

HINT: Don't await while holding a lock! Get what you need and release quickly.
"""

import asyncio


class SharedCounter:
    """A shared counter with a lock."""
    
    def __init__(self):
        self.value = 0
        self.lock = asyncio.Lock()
    
    async def increment_bad(self):
        """
        BAD: Holds lock while doing async work.
        
        This is currently implemented - DO NOT CHANGE THIS METHOD.
        """
        async with self.lock:
            old_value = self.value
            # BAD: Awaiting while holding lock!
            await asyncio.sleep(0.1)  # Simulate slow operation
            self.value = old_value + 1
    
    async def increment_good(self):
        """
        GOOD: Release lock before doing async work.
        
        TODO: Implement this correctly!
        """
        # TODO: Acquire lock, read value, release lock, then do async work
        # Pattern:
        # 1. async with self.lock: read self.value into local variable
        # 2. Release lock (automatic when exiting context)
        # 3. Do async work (sleep)
        # 4. async with self.lock: write new value
        
        pass  # Replace with correct implementation


async def hammer_counter_bad(counter, n):
    """Try to increment using the bad method (will be slow)."""
    for _ in range(n):
        await counter.increment_bad()


async def hammer_counter_good(counter, n):
    """Try to increment using the good method (should be faster)."""
    for _ in range(n):
        await counter.increment_good()
