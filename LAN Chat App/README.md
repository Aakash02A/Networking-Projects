# LAN Chat Application (TCP)

##  Workflow

1. **Server Initialization**
   - Server creates a TCP socket.
   - Binds to `IP:Port` (e.g., `192.168.1.10:5000`).
   - Starts listening for incoming connections.

2. **Client Connection**
   - Client creates a TCP socket.
   - Connects to server using its LAN IP and port.
   - Sends nickname to server.

3. **Message Exchange**
   - Client types a message → sends to server.
   - Server receives the message → broadcasts to all other clients.
   - Each client thread continuously:
     - Listens for new messages (receive).
     - Allows user to type and send messages (send).

4. **Threading**
   - Server: Each client handled in a separate thread.
   - Client: Two threads → one for receiving, one for sending.

5. **Disconnection**
   - If a client disconnects, server removes them from the list.
   - Remaining clients are notified.
