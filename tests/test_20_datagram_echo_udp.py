"""Tests for Exercise 20"""

import asyncio
import importlib.util
from pathlib import Path

exercise_path = Path(__file__).parent.parent / "exercises" / "20_datagram_echo_udp.py"
spec = importlib.util.spec_from_file_location("ex20", exercise_path)
ex20 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex20)


async def test():
    loop = asyncio.get_event_loop()
    
    print("Starting UDP echo server...\n")
    
    server_transport, server_protocol = await loop.create_datagram_endpoint(
        lambda: ex20.EchoServerProtocol(),
        local_addr=('127.0.0.1', 9998)
    )
    
    print(f"Server listening on {server_transport.get_extra_info('sockname')}\n")
    
    print("Creating UDP client...\n")
    
    messages = ["Hello", "UDP", "World"]
    on_done = loop.create_future()
    
    client_transport, client_protocol = await loop.create_datagram_endpoint(
        lambda: ex20.EchoClientProtocol(messages, on_done),
        remote_addr=('127.0.0.1', 9998)
    )
    
    try:
        responses = await asyncio.wait_for(on_done, timeout=2.0)
        print(f"\nReceived all {len(responses)} echoes!")
        
        assert set(responses) == set(messages),             f"Echoes don't match! Sent {messages}, got {responses}"
        
    finally:
        print("\nClosing transports...")
        client_transport.close()
        server_transport.close()
    
    print("\n✓ UDP echo server and client work!")
    print("✓ Datagrams sent and echoed successfully!")
    print("\nNote: UDP is unreliable - in production, handle lost packets!")


if __name__ == "__main__":
    asyncio.run(test())
