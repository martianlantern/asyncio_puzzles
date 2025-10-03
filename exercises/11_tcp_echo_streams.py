"""
Exercise 11: TCP Echo Server - Streams 101

OBJECTIVE:
Learn to use asyncio streams for TCP communication.

TASK:
Build a simple TCP echo server and client. The server echoes back any
data it receives. Test it by sending data from a client.

HINT: Use asyncio.start_server() and asyncio.open_connection()
"""

import asyncio


async def handle_echo_client(reader, writer):
    """
    Handle a single client connection.
    
    TODO: Read data from client and echo it back.
    """
    addr = writer.get_extra_info('peername')
    print(f"  Server: Client connected from {addr}")
    
    try:
        # TODO: Read data from the reader
        # Use: data = await reader.read(1024)
        data = None  # Replace this
        
        if data:
            message = data.decode()
            print(f"  Server: Received {message!r}")
            
            # TODO: Write the same data back (echo)
            # Use: writer.write(data) and await writer.drain()
            pass  # Replace this
            
            print(f"  Server: Echoed back")
    finally:
        print(f"  Server: Closing connection")
        writer.close()
        await writer.wait_closed()


async def start_echo_server(host, port):
    """
    Start the echo server.
    
    TODO: Start a server using asyncio.start_server()
    """
    # TODO: Use asyncio.start_server(handle_echo_client, host, port)
    server = None  # Replace this
    
    addr = server.sockets[0].getsockname()
    print(f"Server listening on {addr}")
    
    return server


async def echo_client(host, port, message):
    """
    Connect to the echo server and send a message.
    
    TODO: Open a connection and send/receive data.
    """
    print(f"Client: Connecting to {host}:{port}")
    
    # TODO: Open connection using asyncio.open_connection(host, port)
    reader, writer = None, None  # Replace this
    
    # Send message
    print(f"Client: Sending {message!r}")
    # TODO: Write message and drain
    # writer.write(message.encode())
    # await writer.drain()
    pass  # Replace this
    
    # Receive echo
    # TODO: Read response
    data = None  # Replace this
    
    response = data.decode()
    print(f"Client: Received {response!r}")
    
    # Close
    writer.close()
    await writer.wait_closed()
    
    return response
