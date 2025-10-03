"""Tests for Exercise 05"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "05_cancellation_cleanup.py"
spec = importlib.util.spec_from_file_location("ex05", exercise_path)
ex05 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex05)


async def test():
    resource = ex05.Resource("test_file")
    task = asyncio.create_task(ex05.worker_with_resource(resource))
    await asyncio.sleep(0.1)
    
    print("\n! Cancelling task...")
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("✓ Task was cancelled")
    
    assert not resource.is_open, "Resource should not be open after cancellation"
    assert resource.is_closed, "Resource should be closed after cancellation (check finally block)"
    
    print("\n✓ Resource was properly cleaned up despite cancellation!")


if __name__ == "__main__":
    asyncio.run(test())
