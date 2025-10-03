"""
Exercise 20: Datagram Echo - UDP Fire-and-Forget

OBJECTIVE:
Learn to use asyncio for UDP communication with create_datagram_endpoint.
Unlike TCP (streams), UDP is connectionless and unreliable.

TASK:
Create a UDP echo server and client. Send datagrams and verify echoes.
Handle the fact that UDP messages can be lost or reordered.

HINT: Use asyncio.create_datagram_endpoint() with a Protocol class.
"""

import asyncio


class EchoServerProtocol(asyncio.DatagramProtocol):
    """
    UDP echo server protocol.
    
    TODO: Implement datagram receiving and echoing.
    """
    
    def connection_made(self, transport):
        self.transport = transport
        print("  Server: UDP socket ready")
    
    def datagram_received(self, data, addr):
        """
        Called when a datagram is received.
        
        TODO: Echo the data back to the sender.
        """
        message = data.decode()
        print(f"  Server: Received {message!r} from {addr}")
        
        # TODO: Send the data back using self.transport.sendto(data, addr)
        pass  # Replace this


class EchoClientProtocol(asyncio.DatagramProtocol):
    """
    UDP echo client protocol.
    
    TODO: Implement datagram receiving and tracking responses.
    """
    
    def __init__(self, messages, on_done):
        self.messages = messages
        self.on_done = on_done
        self.transport = None
        self.responses = []
    
    def connection_made(self, transport):
        self.transport = transport
        print("  Client: UDP socket ready")
        
        # Send all messages
        # TODO: Send each message using self.transport.sendto(msg.encode())
        for msg in self.messages:
            print(f"  Client: Sending {msg!r}")
            pass  # Replace with actual send
    
    def datagram_received(self, data, addr):
        """
        Called when a datagram is received (echo response).
        
        TODO: Store the response and check if we're done.
        """
        message = data.decode()
        print(f"  Client: Received echo {message!r}")
        
        # TODO: Append to responses
        pass  # Replace this
        
        # Check if we got all responses
        if len(self.responses) == len(self.messages):
            self.on_done.set_result(self.responses)
    
    def error_received(self, exc):
        print(f"  Client: Error received: {exc}")
