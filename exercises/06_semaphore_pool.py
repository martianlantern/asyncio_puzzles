"""
Exercise 06: Semaphore Pool - Concurrency Budget

OBJECTIVE:
Learn to limit the number of concurrent operations using asyncio.Semaphore.

TASK:
Process N jobs but ensure at most K jobs run concurrently.
Track the maximum concurrent jobs to verify the semaphore works.

HINT: Use `async with semaphore:` to acquire/release slots automatically.
"""

import asyncio


# Global counter to track concurrent jobs
concurrent_jobs = 0
max_concurrent = 0


async def job(job_id, semaphore):
    """
    Execute a job with semaphore protection.
    
    TODO: Use the semaphore to limit concurrency.
    """
    global concurrent_jobs, max_concurrent
    
    # TODO: Use `async with semaphore:` to limit concurrency
    # Remove the pass and add proper semaphore usage
    
    # Update counters
    concurrent_jobs += 1
    max_concurrent = max(max_concurrent, concurrent_jobs)
    
    print(f"  Job {job_id} started (concurrent: {concurrent_jobs})")
    await asyncio.sleep(0.1)  # Simulate work
    
    concurrent_jobs -= 1
    print(f"  Job {job_id} finished")
    
    return f"result_{job_id}"


async def run_jobs_with_limit(num_jobs, max_concurrent_jobs):
    """
    Run multiple jobs with a concurrency limit.
    
    TODO: Create a semaphore and pass it to all jobs.
    """
    global concurrent_jobs, max_concurrent
    concurrent_jobs = 0
    max_concurrent = 0
    
    # TODO: Create a semaphore with max_concurrent_jobs slots
    semaphore = None  # Replace this
    
    # Create all job tasks
    tasks = [
        asyncio.create_task(job(i, semaphore))
        for i in range(num_jobs)
    ]
    
    # Wait for all to complete
    results = await asyncio.gather(*tasks)
    return results
