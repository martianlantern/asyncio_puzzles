"""
Exercise 13: Subprocess Async - Talk to a Child

OBJECTIVE:
Learn to spawn and communicate with subprocesses asynchronously.

TASK:
Use asyncio.create_subprocess_exec to run a subprocess and capture its
stdout and stderr without blocking the event loop.

HINT: Use asyncio.create_subprocess_exec() and communicate() to get output.
"""

import asyncio
import sys


async def run_subprocess(command, *args):
    """
    Run a subprocess and capture output.
    
    TODO: Create a subprocess and capture stdout/stderr.
    """
    print(f"Running: {command} {' '.join(args)}")
    
    # TODO: Create subprocess using asyncio.create_subprocess_exec
    # proc = await asyncio.create_subprocess_exec(
    #     command, *args,
    #     stdout=asyncio.subprocess.PIPE,
    #     stderr=asyncio.subprocess.PIPE
    # )
    proc = None  # Replace this
    
    # TODO: Communicate with the process (wait and get output)
    # stdout, stderr = await proc.communicate()
    stdout, stderr = None, None  # Replace this
    
    print(f"  Process exited with code {proc.returncode}")
    
    return proc.returncode, stdout.decode(), stderr.decode()


async def run_python_code(code):
    """
    Run Python code in a subprocess.
    
    TODO: Use run_subprocess to run Python with -c flag.
    """
    # TODO: Call run_subprocess with python and -c
    # return await run_subprocess(sys.executable, "-c", code)
    pass  # Replace this
