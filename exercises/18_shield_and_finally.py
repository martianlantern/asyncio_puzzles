"""
Exercise 18: Shield and Finally - Critical Commit

OBJECTIVE:
Learn to use asyncio.shield() to protect critical operations from
cancellation, while still being cooperative around them.

TASK:
When a parent task is cancelled, a critical "commit" operation should
still complete. Use shield() to protect it, but understand the tradeoffs.

HINT: asyncio.shield(coro) protects the inner coroutine from cancellation
of the outer task, but the task can still be cancelled.
"""

import asyncio


commit_completed = False
cleanup_ran = False


async def critical_commit():
    """
    A critical operation that must complete even if parent is cancelled.
    """
    global commit_completed
    print("  Commit: Starting critical write...")
    await asyncio.sleep(0.2)
    commit_completed = True
    print("  Commit: ✓ Critical write completed!")
    return "committed"


async def worker_with_critical_section():
    """
    A worker that does regular work but has a critical commit that
    must not be interrupted.
    
    TODO: Use shield() to protect the critical commit.
    """
    global commit_completed, cleanup_ran
    commit_completed = False
    cleanup_ran = False
    
    try:
        # Regular work (can be cancelled)
        print("  Worker: Doing regular work...")
        await asyncio.sleep(0.1)
        
        # Critical section - must complete!
        print("  Worker: Entering critical section...")
        
        # TODO: Use asyncio.shield() to protect the commit
        # result = await asyncio.shield(critical_commit())
        result = None  # Replace this
        
        print(f"  Worker: Critical section done, result: {result}")
        
        # More regular work
        await asyncio.sleep(0.1)
        print("  Worker: All work done!")
        
    except asyncio.CancelledError:
        print("  Worker: Received cancellation!")
        # Even though we're cancelled, the shielded operation should have completed
        raise
    finally:
        cleanup_ran = True
        print("  Worker: Cleanup in finally block")
