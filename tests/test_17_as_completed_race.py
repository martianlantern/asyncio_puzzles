"""Tests for Exercise 17"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "17_as_completed_race.py"
spec = importlib.util.spec_from_file_location("ex17", exercise_path)
ex17 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex17)


async def test():
    print("Racing three mirrors (different speeds)...\n")
    
    result = await ex17.race_mirrors()
    
    print(f"\nWinner returned: {result}")
    
    assert result == "data_from_Mirror-B", f"Expected Mirror-B (fastest), got {result}"
    assert ex17.cleanup_count == 3,         f"Expected cleanup for 3 tasks, got {ex17.cleanup_count}. Check finally blocks!"
    
    print("\n✓ First result returned successfully!")
    print("✓ Slower mirrors were cancelled!")
    print("✓ All tasks cleaned up properly!")


if __name__ == "__main__":
    asyncio.run(test())
