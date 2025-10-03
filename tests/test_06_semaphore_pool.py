"""Tests for Exercise 06"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "06_semaphore_pool.py"
spec = importlib.util.spec_from_file_location("ex06", exercise_path)
ex06 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex06)


async def test():
    num_jobs = 10
    max_allowed = 3
    
    print(f"Running {num_jobs} jobs with max {max_allowed} concurrent...")
    results = await ex06.run_jobs_with_limit(num_jobs, max_allowed)
    
    assert len(results) == num_jobs, f"Expected {num_jobs} results, got {len(results)}"
    print(f"\nMax concurrent jobs observed: {ex06.max_concurrent}")
    assert ex06.max_concurrent <= max_allowed,         f"Concurrency limit violated! Max was {ex06.max_concurrent}, limit was {max_allowed}"
    assert ex06.max_concurrent >= 2,         f"Concurrency too low ({ex06.max_concurrent}). Did you use the semaphore correctly?"
    
    print(f"\n✓ Semaphore successfully limited concurrency to {max_allowed}!")


if __name__ == "__main__":
    asyncio.run(test())
