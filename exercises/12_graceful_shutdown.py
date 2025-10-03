"""
Exercise 12: Graceful Shutdown - SIGINT Hygiene

OBJECTIVE:
Learn to handle signals (Ctrl-C) gracefully and shut down servers without
leaving pending tasks or warnings.

TASK:
Set up a long-running server with signal handlers that cancel tasks cleanly.
On shutdown, ensure all tasks complete and no warnings appear.

HINT: Use signal.signal() on Unix or handle KeyboardInterrupt for Windows.
"""

import asyncio
import signal
import sys


shutdown_event = asyncio.Event()


async def long_running_task(name, duration):
    """A task that runs for a while and can be cancelled."""
    print(f"  {name}: Starting (will run for {duration}s)")
    try:
        await asyncio.sleep(duration)
        print(f"  {name}: Completed normally")
    except asyncio.CancelledError:
        print(f"  {name}: Cancelled, cleaning up...")
        raise


async def worker_loop():
    """A worker that runs until shutdown."""
    print("Worker: Starting...")
    try:
        counter = 0
        while not shutdown_event.is_set():
            print(f"  Worker: tick {counter}")
            counter += 1
            await asyncio.sleep(0.5)
    except asyncio.CancelledError:
        print("  Worker: Received cancellation")
        raise
    finally:
        print("  Worker: Cleanup complete")


def setup_signal_handlers():
    """
    Set up signal handlers for graceful shutdown.
    
    TODO: Register signal handlers that set the shutdown_event.
    """
    if sys.platform == 'win32':
        # Windows doesn't support signal handlers well, skip for now
        print("  (Signal handlers not set up on Windows)")
        return
    
    def signal_handler(sig, frame):
        print(f"\n! Received signal {sig}, initiating shutdown...")
        # TODO: Set the shutdown_event
        # shutdown_event.set() - but we need to do this in the event loop
        # Use asyncio.get_event_loop().call_soon_threadsafe(shutdown_event.set)
        pass  # Replace this
    
    # TODO: Register handler for SIGINT (Ctrl-C) and SIGTERM
    # signal.signal(signal.SIGINT, signal_handler)
    # signal.signal(signal.SIGTERM, signal_handler)
    pass


async def main_with_graceful_shutdown():
    """
    Run tasks and handle graceful shutdown.
    
    TODO: Implement proper task cleanup on shutdown.
    """
    setup_signal_handlers()
    
    # Start tasks
    tasks = [
        asyncio.create_task(long_running_task("Task-1", 100)),
        asyncio.create_task(long_running_task("Task-2", 100)),
        asyncio.create_task(worker_loop()),
    ]
    
    # Wait for shutdown signal
    # TODO: Wait for shutdown_event to be set
    # await shutdown_event.wait()
    pass
    
    print("\nShutting down tasks...")
    
    # TODO: Cancel all tasks
    for task in tasks:
        pass  # Replace with task.cancel()
    
    # TODO: Wait for all tasks to finish cancelling
    # Use gather with return_exceptions=True to collect results/errors
    pass
    
    print("All tasks cleaned up!")
