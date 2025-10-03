"""Tests for Exercise 10"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "10_run_in_executor.py"
spec = importlib.util.spec_from_file_location("ex10", exercise_path)
ex10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex10)


async def test():
    import time
    work_amount = 50000
    
    print("Testing BLOCKING approach (CPU work on event loop)...")
    tick_times_blocking = []
    
    start = time.time()
    ticker_task = asyncio.create_task(ex10.ticker(1.0, tick_times_blocking))
    await asyncio.sleep(0.1)
    result1 = await ex10.run_cpu_work_blocking(work_amount)
    await ticker_task
    blocking_time = time.time() - start
    
    print(f"  Blocking approach: {len(tick_times_blocking)} ticks in {blocking_time:.2f}s")
    
    print("\nTesting EXECUTOR approach (CPU work in thread pool)...")
    tick_times_executor = []
    
    start = time.time()
    ticker_task = asyncio.create_task(ex10.ticker(1.0, tick_times_executor))
    await asyncio.sleep(0.1)
    result2 = await ex10.run_cpu_work_offloaded(work_amount)
    await ticker_task
    executor_time = time.time() - start
    
    print(f"  Executor approach: {len(tick_times_executor)} ticks in {executor_time:.2f}s")
    
    assert result2 is not None, "Executor didn't return result - did you implement it?"
    assert result1 == result2 == work_amount, "Results don't match"
    assert len(tick_times_executor) > len(tick_times_blocking),         "Executor should allow more ticks! Loop was still blocked."
    
    print(f"\n✓ Executor approach had {len(tick_times_executor)/len(tick_times_blocking):.1f}x more ticks!")
    print("✓ Event loop stayed responsive during CPU work!")


if __name__ == "__main__":
    asyncio.run(test())
