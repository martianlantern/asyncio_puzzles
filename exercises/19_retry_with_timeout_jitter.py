"""
Exercise 19: Retry with Timeout & Jitter - Responsible Retries

OBJECTIVE:
Implement a robust retry mechanism with exponential backoff, jitter,
and a global timeout budget.

TASK:
Create a retry wrapper that:
1. Retries failed operations with exponential backoff
2. Adds jitter to avoid thundering herd
3. Respects a global timeout budget
4. Distinguishes between retryable and non-retryable errors

HINT: Use asyncio.wait_for for timeout, random.uniform for jitter.
"""

import asyncio
import random
import time


attempt_count = 0


async def flaky_operation(fail_times=2):
    """
    An operation that fails the first N times, then succeeds.
    
    DO NOT MODIFY THIS FUNCTION.
    """
    global attempt_count
    attempt_count += 1
    
    print(f"  Attempt #{attempt_count}...")
    await asyncio.sleep(0.05)
    
    if attempt_count <= fail_times:
        print(f"  Attempt #{attempt_count} failed!")
        raise ConnectionError("Service unavailable")
    
    print(f"  Attempt #{attempt_count} succeeded!")
    return f"success_after_{attempt_count}_attempts"


async def retry_with_backoff(coro_func, max_attempts=5, base_delay=0.1, max_delay=2.0, timeout=10.0):
    """
    Retry a coroutine with exponential backoff and jitter.
    
    TODO: Implement retry logic with:
    - Exponential backoff: delay = min(base_delay * (2 ** attempt), max_delay)
    - Jitter: actual_delay = delay * random.uniform(0.5, 1.5)
    - Global timeout budget
    - Return result on success, raise on exhaustion
    """
    start_time = time.time()
    
    for attempt in range(max_attempts):
        try:
            # Check if we've exceeded timeout budget
            elapsed = time.time() - start_time
            remaining = timeout - elapsed
            
            if remaining <= 0:
                raise TimeoutError("Retry budget exhausted")
            
            # TODO: Try the operation with the remaining timeout
            # Use asyncio.wait_for(coro_func(), timeout=remaining)
            result = None  # Replace this
            
            # Success!
            return result
            
        except (ConnectionError, asyncio.TimeoutError) as e:
            # These are retryable errors
            if attempt == max_attempts - 1:
                # Last attempt, give up
                raise Exception(f"Max retries ({max_attempts}) exceeded") from e
            
            # Calculate backoff with jitter
            # TODO: Implement exponential backoff with jitter
            # delay = min(base_delay * (2 ** attempt), max_delay)
            # jittered_delay = delay * random.uniform(0.5, 1.5)
            
            jittered_delay = 0.1  # Replace with actual calculation
            
            print(f"  Retrying in {jittered_delay:.3f}s...")
            await asyncio.sleep(jittered_delay)
        
        except Exception as e:
            # Non-retryable error
            print(f"  Non-retryable error: {e}")
            raise
