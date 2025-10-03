"""
Exercise 16: ContextVars Isolation - Per-Task Context

OBJECTIVE:
Learn to use contextvars.ContextVar to maintain task-local state that's
isolated between concurrent tasks (like thread-local storage, but for tasks).

TASK:
Create tasks that each have their own "request_id" context variable.
Verify that even when tasks are interleaved, each sees only its own value.

HINT: Use contextvars.ContextVar() and .set()/.get() methods.
"""

import asyncio
import contextvars

# TODO: Create a ContextVar for request_id
# request_id = contextvars.ContextVar('request_id', default=None)
request_id = None  # Replace this


async def process_request(req_id, steps):
    """
    Process a request with multiple async steps.
    Each request should maintain its own request_id.
    
    TODO: Set the context variable and verify isolation.
    """
    # TODO: Set the request_id context variable
    # request_id.set(req_id)
    pass  # Replace this
    
    print(f"  Request {req_id}: Started")
    
    for step in range(steps):
        # Simulate async work
        await asyncio.sleep(0.05)
        
        # TODO: Get the current request_id from context
        current_id = None  # Replace this with request_id.get()
        
        print(f"  Request {req_id}: Step {step}, context shows: {current_id}")
        
        # Verify isolation
        assert current_id == req_id, \
            f"Context leaked! Expected {req_id}, got {current_id}"
    
    print(f"  Request {req_id}: Completed")
    return f"result_{req_id}"
