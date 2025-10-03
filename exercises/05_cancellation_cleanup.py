"""
Exercise 05: Cancellation Cleanup - Don't Leak

OBJECTIVE:
Learn to handle cancellation properly and ensure resources are cleaned up.

TASK:
Create a task that acquires a resource, then cancel it mid-execution.
Ensure the resource is properly released in a finally block.

HINT: Use try/finally blocks to guarantee cleanup, even when cancelled.
"""

import asyncio


class Resource:
    """A simulated resource that must be cleaned up."""
    
    def __init__(self, name):
        self.name = name
        self.is_open = False
        self.is_closed = False
    
    async def open(self):
        """Open/acquire the resource."""
        print(f"  Opening resource: {self.name}")
        await asyncio.sleep(0.05)
        self.is_open = True
        print(f"  ✓ Resource opened: {self.name}")
    
    async def close(self):
        """Close/release the resource."""
        print(f"  Closing resource: {self.name}")
        await asyncio.sleep(0.05)
        self.is_closed = True
        self.is_open = False
        print(f"  ✓ Resource closed: {self.name}")


async def worker_with_resource(resource):
    """
    A worker that uses a resource and must clean up even if cancelled.
    
    TODO: Add proper cancellation handling with finally block.
    """
    # TODO: Add try/except/finally block to handle cancellation
    # The resource should be closed even if this coroutine is cancelled
    
    await resource.open()
    
    # Simulate doing work
    print(f"  Working with {resource.name}...")
    await asyncio.sleep(1.0)  # This will be interrupted
    
    print(f"  Work complete with {resource.name}")
    # TODO: Make sure close() is called even on cancellation
