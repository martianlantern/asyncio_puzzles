# 🐍 Asyncio Puzzles

20 progressive puzzles from basics to advanced patterns for mastering python's asyncio
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/exercises-20-green" alt="20 Exercises">
</p>

## 🚀 Quick Start

```bash
# Clone and run
git clone https://github.com/yourusername/asyncio_puzzles.git
cd asyncio_puzzles
uv init
uv run runner.py

# Run specific exercise
python3 runner.py 05_cancellation_cleanup
```

## 📚 Exercises

| # | Name | Concepts | APIs | Difficulty |
|---|------|----------|------|------------|
| 01 | Event Loop Basics | Cooperative yielding | `asyncio.sleep(0)` | ⭐ |
| 02 | Coroutines vs Tasks | Sequential vs concurrent | `create_task()`, `gather()` | ⭐ |
| 03 | gather vs as_completed | Result ordering | `gather()`, `as_completed()` | ⭐ |
| 04 | Timeouts | Time limits | `wait_for()`, `timeout()` | ⭐⭐ |
| 05 | Cancellation | Resource cleanup | `CancelledError`, `finally` | ⭐⭐ |
| 06 | Semaphore | Limit concurrency | `Semaphore()` | ⭐⭐ |
| 07 | Queue | Producer/consumer | `Queue(maxsize)` | ⭐⭐ |
| 08 | Pipeline | Multi-stage processing | `Queue`, sentinels | ⭐⭐⭐ |
| 09 | Locks | Avoid deadlocks | `Lock()` | ⭐⭐⭐ |
| 10 | Executor | CPU-bound work | `run_in_executor()` | ⭐⭐⭐ |
| 11 | TCP Streams | Network I/O | `start_server()`, `open_connection()` | ⭐⭐⭐ |
| 12 | Shutdown | Signal handling | `signal`, task cancellation | ⭐⭐⭐ |
| 13 | Subprocess | External commands | `create_subprocess_exec()` | ⭐⭐⭐ |
| 14 | TaskGroup | Structured concurrency | `TaskGroup()` (3.11+) | ⭐⭐⭐⭐ |
| 15 | TaskGroup vs gather | Error handling | `TaskGroup()`, `gather()` | ⭐⭐⭐⭐ |
| 16 | ContextVars | Task-local state | `ContextVar()` | ⭐⭐⭐⭐ |
| 17 | Race | First result wins | `as_completed()`, cancellation | ⭐⭐⭐⭐ |
| 18 | Shield | Protect operations | `shield()` | ⭐⭐⭐⭐⭐ |
| 19 | Retry | Resilient calls | Backoff, jitter, timeout | ⭐⭐⭐⭐⭐ |
| 20 | UDP | Datagram protocol | `create_datagram_endpoint()` | ⭐⭐⭐⭐⭐ |

## Puzzle Map

```
01 Event Loop
  ↓
02 Tasks → 03 gather/as_completed
  ↓          ↓
  └─────────→ 04 Timeouts
              ↓
              05 Cancellation
              ↓
     ┌────────┼────────┐
     ↓        ↓        ↓
   06 Sem   07 Queue  09 Locks
     ↓        ↓        ↓
     └────────┼────────┘
              ↓
           08 Pipeline
              ↓
         10 Executor
              ↓
    ┌─────────┼─────────┐
    ↓         ↓         ↓
11 TCP    13 Subproc  12 Shutdown
    ↓
14 TaskGroup → 15 TaskGroup vs gather
    ↓
    ↓
16 ContextVars
    ↓
17 Race → 18 Shield → 19 Retry
                        ↓
                    20 UDP
```

## How to start solving

1. Open an exercise you want to solve in `exercises/` and Fix the TODO markers
2. Test your solution with `python3 runner.py`
3. Repeat

**Example:**
```python
# exercises/02_coroutines_vs_tasks.py
async def run_concurrent():
    """TODO: Implement concurrent execution using asyncio.create_task()"""
    results = []
    pass  # ← Replace this with your code
    return results
```

## 📖 Resources

- [Python asyncio docs](https://docs.python.org/3/library/asyncio.html)
- [PEP 492 - async/await](https://www.python.org/dev/peps/pep-0492/)

## 🤝 Contributing - Adding New Puzzles

Want to add a new puzzle? Follow this structure:

```
Add Exercise 21: Connection Pool

- exercises/21_connection_pool.py (starter code)
- tests/test_21_connection_pool.py (comprehensive tests)
- README.md (updated table and map)
```

Happy puzzle creating!