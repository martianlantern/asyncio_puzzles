#!/usr/bin/env python3
"""
Asyncio Puzzles Runner
A Rustlings-style test runner for asyncio exercises.
"""
import sys
import importlib.util
import asyncio
from pathlib import Path
import traceback


class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_header():
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}")
    print("🐍 Asyncio Puzzles - Test Runner")
    print(f"{'='*70}{Colors.RESET}\n")


def load_module(filepath, module_name):
    """Dynamically load a module from a file path."""
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def run_exercise(exercise_file, test_file):
    """Run a single exercise with its test and return success status."""
    exercise_name = exercise_file.name
    print(f"{Colors.BOLD}Running: {exercise_name}{Colors.RESET}")
    
    try:
        # Load the test module (it will import the exercise)
        test_module = load_module(test_file, f"test_{exercise_name[:-3]}")
        
        # Look for a test function
        if hasattr(test_module, 'test'):
            # Run the test (it might be async or sync)
            test_func = test_module.test
            if asyncio.iscoroutinefunction(test_func):
                asyncio.run(test_func())
            else:
                test_func()
            
            print(f"{Colors.GREEN}✓ {exercise_name} - PASSED{Colors.RESET}\n")
            return True
        else:
            print(f"{Colors.RED}✗ {exercise_name} - No test() function found{Colors.RESET}\n")
            return False
            
    except AssertionError as e:
        print(f"{Colors.RED}✗ {exercise_name} - FAILED")
        print(f"  Assertion Error: {e}{Colors.RESET}\n")
        return False
    except Exception as e:
        print(f"{Colors.RED}✗ {exercise_name} - ERROR")
        print(f"  {type(e).__name__}: {e}")
        traceback.print_exc()
        print(f"{Colors.RESET}\n")
        return False


def main():
    print_header()
    
    exercises_dir = Path(__file__).parent / "exercises"
    tests_dir = Path(__file__).parent / "tests"
    
    if not exercises_dir.exists():
        print(f"{Colors.RED}Error: 'exercises' directory not found!{Colors.RESET}")
        sys.exit(1)
    
    if not tests_dir.exists():
        print(f"{Colors.RED}Error: 'tests' directory not found!{Colors.RESET}")
        sys.exit(1)
    
    # Get exercise file from command line or run all
    if len(sys.argv) > 1:
        exercise_name = sys.argv[1]
        if not exercise_name.endswith('.py'):
            exercise_name += '.py'
        
        exercise_path = exercises_dir / exercise_name
        if not exercise_path.exists():
            print(f"{Colors.RED}Error: Exercise '{exercise_name}' not found!{Colors.RESET}")
            sys.exit(1)
        
        # Find corresponding test
        test_name = f"test_{exercise_name}"
        test_path = tests_dir / test_name
        
        if not test_path.exists():
            print(f"{Colors.RED}Error: Test '{test_name}' not found!{Colors.RESET}")
            sys.exit(1)
        
        exercises = [(exercise_path, test_path)]
    else:
        # Run all exercises in order
        exercise_files = sorted(exercises_dir.glob("*.py"))
        exercises = []
        
        for ex_file in exercise_files:
            test_file = tests_dir / f"test_{ex_file.name}"
            if test_file.exists():
                exercises.append((ex_file, test_file))
            else:
                print(f"{Colors.YELLOW}Warning: No test found for {ex_file.name}{Colors.RESET}")
    
    passed = 0
    failed = 0
    
    for exercise_file, test_file in exercises:
        if run_exercise(exercise_file, test_file):
            passed += 1
        else:
            failed += 1
            # Stop on first failure (Rustlings-style)
            print(f"{Colors.YELLOW}{'='*70}")
            print(f"Fix the exercise above and run again!")
            print(f"{'='*70}{Colors.RESET}\n")
            break
    
    # Summary
    total = passed + failed
    if failed == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}{'='*70}")
        print(f"🎉 All exercises passed! ({passed}/{total})")
        print(f"{'='*70}{Colors.RESET}\n")
    else:
        print(f"\n{Colors.YELLOW}Progress: {passed}/{total} exercises completed{Colors.RESET}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
