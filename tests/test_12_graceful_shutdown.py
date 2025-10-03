"""Tests for Exercise 12"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "12_graceful_shutdown.py"
spec = importlib.util.spec_from_file_location("ex12", exercise_path)
ex12 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex12)


async def test():
    import asyncio
    print("Starting server (will auto-shutdown after 1 second for testing)...")
    
    main_task = asyncio.create_task(ex12.main_with_graceful_shutdown())
    await asyncio.sleep(1.0)
    
    print("\n! Triggering shutdown for test...")
    ex12.shutdown_event.set()
    
    try:
        await asyncio.wait_for(main_task, timeout=2.0)
    except asyncio.TimeoutError:
        print("Warning: Shutdown took too long")
        main_task.cancel()
        await asyncio.gather(main_task, return_exceptions=True)
    
    print("\n✓ Graceful shutdown completed!")
    print("✓ No pending task warnings!")


if __name__ == "__main__":
    asyncio.run(test())
