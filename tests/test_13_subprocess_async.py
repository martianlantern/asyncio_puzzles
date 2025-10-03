"""Tests for Exercise 13"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "13_subprocess_async.py"
spec = importlib.util.spec_from_file_location("ex13", exercise_path)
ex13 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex13)


async def test():
    import sys
    import time
    
    print("Test 1: Simple Python print")
    returncode, stdout, stderr = await ex13.run_python_code("print('Hello from subprocess')")
    
    assert returncode == 0, f"Expected returncode 0, got {returncode}"
    assert "Hello from subprocess" in stdout, f"Unexpected stdout: {stdout}"
    print(f"  stdout: {stdout.strip()}")
    
    print("\nTest 2: Print to stderr")
    returncode, stdout, stderr = await ex13.run_python_code("import sys; print('Error!', file=sys.stderr)")
    
    assert returncode == 0, f"Expected returncode 0, got {returncode}"
    assert "Error!" in stderr, f"Expected stderr to contain 'Error!', got: {stderr}"
    print(f"  stderr: {stderr.strip()}")
    
    print("\nTest 3: Exit with error code")
    returncode, stdout, stderr = await ex13.run_python_code("import sys; sys.exit(42)")
    
    assert returncode == 42, f"Expected returncode 42, got {returncode}"
    
    print("\nTest 4: Running multiple subprocesses concurrently")
    start = time.time()
    
    results = await asyncio.gather(
        ex13.run_python_code("import time; time.sleep(0.2); print('A')"),
        ex13.run_python_code("import time; time.sleep(0.2); print('B')"),
        ex13.run_python_code("import time; time.sleep(0.2); print('C')"),
    )
    
    elapsed = time.time() - start
    print(f"  Ran 3 subprocesses in {elapsed:.2f}s (concurrent!)")
    assert elapsed < 0.5, "Subprocesses should run concurrently"
    
    print("\n✓ All subprocess tests passed!")
    print("✓ Async subprocess communication works!")


if __name__ == "__main__":
    asyncio.run(test())
