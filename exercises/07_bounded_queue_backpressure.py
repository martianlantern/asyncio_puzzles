"""
Exercise 07: Bounded Queue - Producer/Consumer Backpressure

OBJECTIVE:
Use asyncio.Queue with maxsize to apply backpressure when producer is
faster than consumer.

TASK:
Create a bounded queue where a fast producer will block when the queue
is full, waiting for the slow consumer to catch up.

HINT: Use asyncio.Queue(maxsize=N) to create a bounded queue.
"""

import asyncio
import time


async def producer(queue, num_items):
    """
    Produce items quickly and put them in the queue.
    
    TODO: Put items into the queue.
    """
    print("Producer starting...")
    for i in range(num_items):
        item = f"item_{i}"
        print(f"  Producer: creating {item}")
        
        # TODO: Put item into queue using await queue.put(item)
        # This will block if queue is full (backpressure!)
        pass  # Replace this
        
        print(f"  Producer: {item} queued")
        await asyncio.sleep(0.01)  # Simulate some work between productions
    
    print("Producer done!")


async def consumer(queue, num_items):
    """
    Consume items slowly from the queue.
    
    TODO: Get items from the queue.
    """
    print("Consumer starting...")
    results = []
    
    for i in range(num_items):
        # TODO: Get item from queue using item = await queue.get()
        item = None  # Replace this
        
        print(f"  Consumer: processing {item}")
        await asyncio.sleep(0.05)  # Slow processing
        results.append(item)
        
        # TODO: Mark task as done using queue.task_done()
        pass  # Replace this
    
    print("Consumer done!")
    return results
