"""Tests for Exercise 03: gather vs as_completed"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "03_gather_vs_as_completed.py"
spec = importlib.util.spec_from_file_location("ex03", exercise_path)
ex03 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex03)


async def test():
    """Test both approaches and verify ordering differences."""
    # Test gather (should preserve input order)
    gather_results = await ex03.use_gather()
    print(f"Gather results: {gather_results}")
    assert len(gather_results) == 3, "Gather should return 3 results"
    assert gather_results == ["task_A", "task_B", "task_C"], \
        f"Gather should preserve order: expected ['task_A', 'task_B', 'task_C'], got {gather_results}"
    
    # Test as_completed (should be in completion order)
    as_completed_results = await ex03.use_as_completed()
    print(f"As-completed results: {as_completed_results}")
    assert len(as_completed_results) == 3, "As_completed should return 3 results"
    assert as_completed_results == ["task_B", "task_C", "task_A"], \
        f"As_completed should be in completion order (B→C→A), got {as_completed_results}"
    
    # Verify same set of results
    assert set(gather_results) == set(as_completed_results), \
        "Both should return the same set of results"
    
    print("\n✓ gather preserves order, as_completed gives completion order!")


if __name__ == "__main__":
    asyncio.run(test())
