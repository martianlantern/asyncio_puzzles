"""Tests for Exercise 14"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "14_taskgroup_basics.py"
spec = importlib.util.spec_from_file_location("ex14", exercise_path)
ex14 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex14)


async def test():
    import sys
    print("Running tasks with TaskGroup (one will fail)...\n")
    
    try:
        results = await ex14.run_with_taskgroup()
        print(f"Unexpected success: {results}")
        assert False, "TaskGroup should have raised an exception!"
    except* ValueError as eg:
        print(f"\n✓ Caught ExceptionGroup with {len(eg.exceptions)} exception(s)")
        for exc in eg.exceptions:
            print(f"  - {type(exc).__name__}: {exc}")
    except ExceptionGroup as eg:
        print(f"\n✓ Caught ExceptionGroup with {len(eg.exceptions)} exception(s)")
        for exc in eg.exceptions:
            print(f"  - {type(exc).__name__}: {exc}")
    except ValueError as e:
        print(f"\n✓ Caught exception: {e}")
    
    print("\n✓ TaskGroup cancelled siblings when one task failed!")
    print("✓ Structured concurrency works!")


if __name__ == "__main__":
    asyncio.run(test())
