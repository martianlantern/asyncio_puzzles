"""Tests for Exercise 18"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "18_shield_and_finally.py"
spec = importlib.util.spec_from_file_location("ex18", exercise_path)
ex18 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex18)


async def test():
    print("Starting worker with critical section...\n")
    
    task = asyncio.create_task(ex18.worker_with_critical_section())
    await asyncio.sleep(0.15)
    
    print("\n! Cancelling task during critical section...")
    task.cancel()
    
    try:
        await task
    except asyncio.CancelledError:
        print("\n✓ Task was cancelled")
    
    assert ex18.commit_completed,         "Critical commit should have completed despite cancellation! Use shield()."
    assert ex18.cleanup_ran, "Finally block should have run"
    
    print("\n✓ Critical commit completed despite cancellation!")
    print("✓ Shield protected the critical operation!")
    print("\nNote: Use shield() sparingly - overuse can make cancellation ineffective!")


if __name__ == "__main__":
    asyncio.run(test())
