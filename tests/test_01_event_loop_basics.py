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
    
    # Capture output timing
    tick_times = []
    
    # Create instrumented ticker
    async def instrumented_ticker():
        for i in range(5):
            tick_times.append(time.time() - start)
            print(f"  tick {i}")
            await asyncio.sleep(0.01)
    
    # Run with instrumented ticker
    ticker_task = asyncio.create_task(instrumented_ticker())
    worker_task = asyncio.create_task(ex01.busy_worker(10000))
    
    await ticker_task
    await worker_task
    
    # Verify ticks were spread out (not all bunched at the end)
    if len(tick_times) >= 2:
        # The ticks should start early and be somewhat evenly spaced
        first_tick = tick_times[0]
        assert first_tick < 0.5, \
            f"First tick came too late ({first_tick:.3f}s). Busy worker isn't yielding!"
        
        # Check that ticks are reasonably spread
        tick_spread = tick_times[-1] - tick_times[0]
        assert tick_spread > 0.03, \
            f"Ticks are bunched together ({tick_spread:.3f}s spread). Worker should yield!"
    
    print("\n✓ Ticks appeared during busy work - cooperation works!")


if __name__ == "__main__":
    asyncio.run(test())
