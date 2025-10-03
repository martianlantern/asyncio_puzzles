"""
Exercise 08: Pipeline - Three-Stage Assembly Line

OBJECTIVE:
Build a multi-stage pipeline with proper shutdown using queue sentinels.

TASK:
Create a 3-stage pipeline: ingest → transform → persist
Each stage reads from one queue and writes to the next.
Implement graceful shutdown with sentinel values.

HINT: Use None as a sentinel value to signal "no more items".
"""

import asyncio


async def ingest(input_data, transform_queue):
    """
    Stage 1: Ingest raw data and send to transform stage.
    
    TODO: Put items into transform_queue, then send sentinel.
    """
    print("Ingest stage starting...")
    for item in input_data:
        print(f"  Ingest: {item}")
        # TODO: Put item into transform_queue
        pass
        await asyncio.sleep(0.02)
    
    # TODO: Send sentinel (None) to signal end
    print("Ingest: sending sentinel")
    pass
    print("Ingest stage done!")


async def transform(transform_queue, persist_queue):
    """
    Stage 2: Transform data and send to persist stage.
    
    TODO: Get items from transform_queue, transform them, put to persist_queue.
    Stop when receiving sentinel.
    """
    print("Transform stage starting...")
    while True:
        # TODO: Get item from transform_queue
        item = None
        
        # Check for sentinel
        if item is None:
            print("Transform: received sentinel")
            # TODO: Forward sentinel to next stage
            pass
            break
        
        # Transform the item
        transformed = item.upper()
        print(f"  Transform: {item} -> {transformed}")
        
        # TODO: Put transformed item into persist_queue
        pass
        await asyncio.sleep(0.02)
    
    print("Transform stage done!")


async def persist(persist_queue, results):
    """
    Stage 3: Persist/save final data.
    
    TODO: Get items from persist_queue and save them. Stop on sentinel.
    """
    print("Persist stage starting...")
    while True:
        # TODO: Get item from persist_queue
        item = None
        
        # Check for sentinel
        if item is None:
            print("Persist: received sentinel")
            break
        
        # "Save" the item
        print(f"  Persist: saving {item}")
        results.append(item)
        await asyncio.sleep(0.02)
    
    print("Persist stage done!")
