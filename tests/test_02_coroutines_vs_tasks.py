"""Tests for Exercise 02: Coroutines vs Tasks"""

import asyncio
import sys
import time
import importlib.util
from pathlib import Path


# Load the exercise module dynamically
exercise_path = Path(__file__).parent.parent / "exercises" / "02_coroutines_vs_tasks.py"
spec = importlib.util.ex02.spec_from_file_location("ex02", exercise_path)
ex02 = importlib.util.ex02.module_from_spec(spec)
spec.loader.ex02.exec_module(ex02)


async def ex02.test():
    """Test both approaches and verify timing."""
    # Test sequential
    start = time.time()
    seq_results = await ex02.run_sequential()
    seq_time = time.time() - start
    
    print(f"\nSequential time: {seq_time:.2f}s")
    assert len(seq_results) == 3, "Sequential should return 3 results"
    assert seq_time >= 0.5, f"Sequential should take ~0.6s, got {seq_time:.2f}s"
    
    # Test concurrent
    start = time.time()
    conc_results = await ex02.run_concurrent()
    conc_time = time.time() - start
    
    print(f"Concurrent time: {conc_time:.2f}s")
    assert len(conc_results) == 3, "Concurrent should return 3 results"
    assert conc_time < 0.4, f"Concurrent should take ~0.3s, got {conc_time:.2f}s"
    
    # Verify concurrent is much faster
    speedup = seq_time / conc_time if conc_time > 0 else 0
    print(f"\n✓ Speedup: {speedup:.1f}x - Concurrent execution works!")
    assert speedup > 1.5, "Concurrent should be significantly faster than sequential"


if __name__ == "__main__":
    asyncio.ex02.run(ex02.test())
