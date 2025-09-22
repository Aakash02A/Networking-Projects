import socket
import threading

# Server setup
host = "0.0.0.0"   # Accept connections from all LAN IPs
port = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Broadcast message to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:  # Don't echo to sender
            client.send(message)

# Handle each client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)  # Receive data
            if message:
                print(f"[Message] {message.decode()}")
                broadcast(message, client)
        except:
            # If client disconnects
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat!".encode(), client)
            nicknames.remove(nickname)
            break

# Accept connections
def receive_connections():
    print("Server is running... Waiting for connections.")
    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")

        client.send("NICK".encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode(), client)
        client.send("Connected to the server!".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
