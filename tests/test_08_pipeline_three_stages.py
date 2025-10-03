"""Tests for Exercise 08"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "08_pipeline_three_stages.py"
spec = importlib.util.spec_from_file_location("ex08", exercise_path)
ex08 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex08)


async def test():
    input_data = ["apple", "banana", "cherry", "date", "fig"]
    expected_output = [item.upper() for item in input_data]
    
    transform_queue = asyncio.Queue()
    persist_queue = asyncio.Queue()
    results = []
    
    stage1 = asyncio.create_task(ex08.ingest(input_data, transform_queue))
    stage2 = asyncio.create_task(ex08.transform(transform_queue, persist_queue))
    stage3 = asyncio.create_task(ex08.persist(persist_queue, results))
    
    await asyncio.gather(stage1, stage2, stage3)
    
    print(f"\nResults: {results}")
    assert len(results) == len(input_data), f"Expected {len(input_data)} results, got {len(results)}"
    assert results == expected_output, f"Expected {expected_output}, got {results}"
    
    print("\n✓ Pipeline processed all items correctly!")
    print("✓ Graceful shutdown with sentinels works!")


if __name__ == "__main__":
    asyncio.run(test())
