"""Tests for Exercise 11"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "11_tcp_echo_streams.py"
spec = importlib.util.spec_from_file_location("ex11", exercise_path)
ex11 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex11)


async def test():
    host = '127.0.0.1'
    port = 9999
    
    server = await ex11.start_echo_server(host, port)
    await asyncio.sleep(0.1)
    
    test_message = "Hello, asyncio!"
    try:
        response = await ex11.echo_client(host, port, test_message)
        
        assert response == test_message, f"Echo failed: sent {test_message!r}, got {response!r}"
        
        print("\n✓ Echo server works correctly!")
    finally:
        server.close()
        await server.wait_closed()
        print("✓ Server closed cleanly!")


if __name__ == "__main__":
    asyncio.run(test())
