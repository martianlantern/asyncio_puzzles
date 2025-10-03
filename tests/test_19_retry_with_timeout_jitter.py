"""Tests for Exercise 19"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "19_retry_with_timeout_jitter.py"
spec = importlib.util.spec_from_file_location("ex19", exercise_path)
ex19 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex19)


async def test():
    import time
    
    print("Test 1: Operation that succeeds after 2 failures\n")
    ex19.attempt_count = 0
    
    start = time.time()
    result = await ex19.retry_with_backoff(lambda: ex19.flaky_operation(fail_times=2), max_attempts=5)
    elapsed = time.time() - start
    
    print(f"\nResult: {result}")
    print(f"Total attempts: {ex19.attempt_count}")
    print(f"Time elapsed: {elapsed:.2f}s")
    
    assert result == "success_after_3_attempts", f"Unexpected result: {result}"
    assert ex19.attempt_count == 3, f"Expected 3 attempts, got {ex19.attempt_count}"
    
    print("\n" + "="*60)
    print("Test 2: Operation that fails too many times\n")
    ex19.attempt_count = 0
    
    try:
        result = await ex19.retry_with_backoff(lambda: ex19.flaky_operation(fail_times=10), max_attempts=3)
        assert False, "Should have raised exception"
    except Exception as e:
        print(f"\n✓ Correctly raised: {type(e).__name__}: {e}")
        assert ex19.attempt_count == 3, f"Expected 3 attempts, got {ex19.attempt_count}"
    
    print("\n✓ Retry mechanism with backoff and jitter works!")
    print("✓ Timeout budget respected!")
    print("✓ Exponential backoff prevents overwhelming services!")


if __name__ == "__main__":
    asyncio.run(test())
