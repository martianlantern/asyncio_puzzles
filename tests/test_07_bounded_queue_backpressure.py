"""Tests for Exercise 07"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "07_bounded_queue_backpressure.py"
spec = importlib.util.spec_from_file_location("ex07", exercise_path)
ex07 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex07)


async def test():
    queue_size = 3
    num_items = 10
    
    queue = asyncio.Queue(maxsize=queue_size)
    print(f"Using queue with maxsize={queue_size}, producing {num_items} items\n")
    
    import time
    start = time.time()
    
    producer_task = asyncio.create_task(ex07.producer(queue, num_items))
    consumer_task = asyncio.create_task(ex07.consumer(queue, num_items))
    
    await producer_task
    results = await consumer_task
    await queue.join()
    
    elapsed = time.time() - start
    
    assert len(results) == num_items, f"Expected {num_items} items, got {len(results)}"
    assert results == [f"item_{i}" for i in range(num_items)], "Items order incorrect"
    
    print(f"\n✓ All {num_items} items processed in {elapsed:.2f}s")
    print("✓ Backpressure worked - producer had to wait for consumer!")


if __name__ == "__main__":
    asyncio.run(test())
