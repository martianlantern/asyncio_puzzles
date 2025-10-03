"""
Exercise 17: as_completed Race - First Past the Post

OBJECTIVE:
Learn to race multiple sources and use the first successful result while
cancelling the remaining tasks.

TASK:
Start multiple "mirror" fetches with different delays. Use as_completed
to get the first result, then cancel the remaining tasks.

HINT: Use asyncio.as_completed() and remember to cancel unused tasks.
"""

import asyncio


cleanup_count = 0


async def fetch_from_mirror(mirror_name, delay, should_fail=False):
    """
    Fetch data from a mirror with a specific delay.
    
    TODO: Add cleanup tracking in finally block.
    """
    global cleanup_count
    
    try:
        print(f"  {mirror_name}: Starting (delay {delay}s)")
        await asyncio.sleep(delay)
        
        if should_fail:
            raise Exception(f"{mirror_name} failed")
        
        print(f"  {mirror_name}: Completed!")
        return f"data_from_{mirror_name}"
    except asyncio.CancelledError:
        print(f"  {mirror_name}: Cancelled")
        raise
    finally:
        # TODO: Increment cleanup_count to track cleanup
        pass  # Replace this


async def race_mirrors():
    """
    Race multiple mirrors and return the first successful result.
    
    TODO: Use as_completed to get first result, then cancel others.
    """
    global cleanup_count
    cleanup_count = 0
    
    # Create tasks for three mirrors with different speeds
    tasks = [
        asyncio.create_task(fetch_from_mirror("Mirror-A", 0.3)),
        asyncio.create_task(fetch_from_mirror("Mirror-B", 0.1)),  # Fastest
        asyncio.create_task(fetch_from_mirror("Mirror-C", 0.5)),
    ]
    
    result = None
    winner = None
    
    # TODO: Use as_completed to iterate over tasks as they complete
    # Get the first successful result, then cancel the rest
    # Hint: for coro in asyncio.as_completed(tasks): ...
    
    pass  # Replace this implementation
    
    # Make sure remaining tasks are cancelled
    # TODO: Cancel all remaining tasks
    for task in tasks:
        if not task.done():
            pass  # Replace with task.cancel()
    
    # Wait for cancellations to complete
    await asyncio.gather(*tasks, return_exceptions=True)
    
    return result
