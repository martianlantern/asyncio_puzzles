"""Tests for Exercise 16"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "16_contextvars_isolation.py"
spec = importlib.util.spec_from_file_location("ex16", exercise_path)
ex16 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex16)


async def test():
    print("Running multiple concurrent requests with isolated contexts...\n")
    
    results = await asyncio.gather(
        ex16.process_request("REQ-001", 3),
        ex16.process_request("REQ-002", 3),
        ex16.process_request("REQ-003", 3),
    )
    
    assert len(results) == 3, f"Expected 3 results, got {len(results)}"
    assert results == ["result_REQ-001", "result_REQ-002", "result_REQ-003"],         f"Unexpected results: {results}"
    
    print("\n✓ All requests maintained isolated context!")
    print("✓ ContextVars provide per-task state isolation!")


if __name__ == "__main__":
    asyncio.run(test())
