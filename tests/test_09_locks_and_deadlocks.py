"""Tests for Exercise 09"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "09_locks_and_deadlocks.py"
spec = importlib.util.spec_from_file_location("ex09", exercise_path)
ex09 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex09)


async def test():
    import time
    
    print("Testing BAD approach (holding lock during async work)...")
    counter_bad = ex09.SharedCounter()
    start = time.time()
    
    tasks = [asyncio.create_task(ex09.hammer_counter_bad(counter_bad, 3)) for _ in range(2)]
    await asyncio.gather(*tasks)
    
    bad_time = time.time() - start
    print(f"  Bad approach: {bad_time:.2f}s, final value: {counter_bad.value}")
    
    print("\nTesting GOOD approach (releasing lock before async work)...")
    counter_good = ex09.SharedCounter()
    start = time.time()
    
    tasks = [asyncio.create_task(ex09.hammer_counter_good(counter_good, 3)) for _ in range(2)]
    await asyncio.gather(*tasks)
    
    good_time = time.time() - start
    print(f"  Good approach: {good_time:.2f}s, final value: {counter_good.value}")
    
    assert counter_good.value == 6, f"Expected 6, got {counter_good.value}"
    
    print(f"\n✓ Good approach is {bad_time/good_time:.1f}x faster!")
    print("✓ Deadlock avoided by not awaiting while holding lock!")


if __name__ == "__main__":
    asyncio.run(test())
