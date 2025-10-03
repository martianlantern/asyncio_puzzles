"""Tests for Exercise 01: Event Loop Basics"""

import asyncio
import sys
import importlib.util
from pathlib import Path


# Load the exercise module dynamically
exercise_path = Path(__file__).parent.parent / "exercises" / "01_event_loop_basics.py"
spec = importlib.util.spec_from_file_location("ex01", exercise_path)
ex01 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex01)


async def test():
    """Test that ticks appear during busy work (not all at the end)."""
    import time
    
    start = time.time()
    
    # Capture output timing and worker state
    tick_times = []
    worker_done = False
    worker_done_time = None
    
    # Create instrumented ticker
    async def instrumented_ticker():
        for i in range(5):
            tick_times.append({
                'time': time.time() - start,
                'worker_done': worker_done
            })
            print(f"  tick {i}")
            await asyncio.sleep(0.01)
    
    # Create instrumented worker
    async def instrumented_worker():
        nonlocal worker_done, worker_done_time
        await ex01.busy_worker(10000)
        worker_done = True
        worker_done_time = time.time() - start
    
    # Run with instrumented versions
    ticker_task = asyncio.create_task(instrumented_ticker())
    worker_task = asyncio.create_task(instrumented_worker())
    
    await ticker_task
    await worker_task
    
    # Verify ticks appeared DURING busy work, not after
    if len(tick_times) >= 3:
        # Count how many ticks happened while worker was still running
        ticks_during_work = sum(1 for t in tick_times if not t['worker_done'])
        
        assert ticks_during_work >= 3, \
            f"Only {ticks_during_work} ticks happened during busy work (need at least 3). "\
            f"The busy worker must yield control with 'await asyncio.sleep(0)'!"
        
        # Verify ticks are reasonably spread
        first_tick_time = tick_times[0]['time']
        last_tick_time = tick_times[-1]['time']
        tick_spread = last_tick_time - first_tick_time
        
        assert tick_spread > 0.03, \
            f"Ticks are bunched together ({tick_spread:.3f}s spread). Worker should yield!"
    
    print("\n✓ Ticks appeared during busy work - cooperation works!")


if __name__ == "__main__":
    asyncio.run(test())
