import socket
import threading

nickname = input("Enter your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))  # Replace with server LAN IP

# Receive messages from server
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "NICK":
                client.send(nickname.encode())
            else:
                print(message)
        except:
            print("Disconnected from server")
            client.close()
            break

# Send messages to server
def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode())

# Run threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
