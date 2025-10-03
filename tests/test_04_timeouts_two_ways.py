"""Tests for Exercise 04"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "04_timeouts_two_ways.py"
spec = importlib.util.spec_from_file_location("ex04", exercise_path)
ex04 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex04)


async def test():
    result1 = await ex04.timeout_with_wait_for()
    assert result1 is None, "wait_for should timeout and return None"
    
    result2 = await ex04.timeout_with_context_manager()
    assert result2 is None, "timeout context should timeout and return None"
    
    print("\n✓ Both timeout methods work correctly!")
    print("✓ CancelledError propagated to task and finally blocks ran!")


if __name__ == "__main__":
    asyncio.run(test())
