"""Tests for Exercise 15"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "15_taskgroup_vs_gather.py"
spec = importlib.util.spec_from_file_location("ex15", exercise_path)
ex15 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex15)


async def test():
    import time
    
    start = time.time()
    tg_result = await ex15.test_with_taskgroup()
    tg_time = time.time() - start
    
    print(f"  TaskGroup result: {tg_result}")
    print(f"  Time: {tg_time:.2f}s")
    
    import sys
    if sys.version_info >= (3, 11):
        assert isinstance(tg_result, (ExceptionGroup, ValueError)), "TaskGroup should raise exception"
    assert tg_time < 0.4, "TaskGroup should cancel quickly (before TG-C completes)"
    
    start = time.time()
    gather_results = await ex15.test_with_gather()
    gather_time = time.time() - start
    
    print(f"  gather results: {gather_results}")
    print(f"  Time: {gather_time:.2f}s")
    
    assert len(gather_results) == 3, f"gather should return 3 results, got {len(gather_results)}"
    assert isinstance(gather_results[1], ValueError), "Second result should be the exception"
    assert gather_results[0] == "result_G-A", "First task should succeed"
    assert gather_results[2] == "result_G-C", "Third task should succeed despite sibling failure"
    assert gather_time >= 0.5, "gather should wait for all tasks (including the 0.5s one)"
    
    print("\n✓ TaskGroup cancels siblings and fails fast!")
    print("✓ gather(return_exceptions=True) lets all tasks complete!")


if __name__ == "__main__":
    asyncio.run(test())
