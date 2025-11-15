"""
Simple HTTP Forward Proxy (Educational Only)
--------------------------------------------
This proxy:
 - Handles basic HTTP GET/POST over port 80.
 - Supports HTTPS tunneling via CONNECT method (no interception).
 - Does NOT inspect or modify HTTPS data.
 - Logs only minimal metadata.
 - Requires explicit client configuration.

This is a safe, minimal learning example — not for production.
"""

import socket
import threading

BUFFER_SIZE = 4096

def handle_client(client_socket, client_addr):
    print(f"[INFO] Connection from {client_addr}")

    # Read the client request line + headers (simple blocking read)
    request = client_socket.recv(BUFFER_SIZE)
    if not request:
        client_socket.close()
        return

    # Decode safely
    try:
        header = request.decode("iso-8859-1")
    except:
        header = ""

    first_line = header.split("\n")[0]
    print(f"[REQ] {first_line.strip()}")

    # Parse method, URL, version
    try:
        method, url, http_version = first_line.split()
    except ValueError:
        client_socket.close()
        return

    # === Case 1: HTTPS CONNECT tunnel ======================================
    if method.upper() == "CONNECT":
        host, port = url.split(":")
        port = int(port)

        try:
            # Create tunnel to remote server
            remote = socket.create_connection((host, port))
            client_socket.sendall(b"HTTP/1.1 200 Connection established\r\n\r\n")

            # Relay bytes both ways
            relay(client_socket, remote)
        except Exception as e:
            print("[ERR] HTTPS tunnel error:", e)

        client_socket.close()
        return

    # === Case 2: Normal HTTP request ========================================
    # Extract host header for HTTP forwarding
    host = None
    for line in header.split("\n"):
        if line.lower().startswith("host:"):
            host = line.split(":", 1)[1].strip()
            break

    if not host:
        client_socket.close()
        return

    # Default HTTP port
    remote_port = 80

    # Connect to origin server
    try:
        remote = socket.create_connection((host, remote_port))
        remote.sendall(request)  # forward original request
    except Exception as e:
        print("[ERR] Unable to connect to host:", e)
        client_socket.close()
        return

    # Relay server response back to client
    relay(client_socket, remote)
    client_socket.close()


def relay(sock1, sock2):
    """Bidirectional byte relay between two sockets."""
    def forward(src, dst):
        try:
            while True:
                data = src.recv(BUFFER_SIZE)
                if not data:
                    break
                dst.sendall(data)
        except:
            pass

    t1 = threading.Thread(target=forward, args=(sock1, sock2))
    t2 = threading.Thread(target=forward, args=(sock2, sock1))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def start_proxy(host="0.0.0.0", port=8080):
    print(f"[INFO] Starting HTTP Proxy on {host}:{port} ...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    while True:
        client_socket, client_addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_addr), daemon=True).start()


if __name__ == "__main__":
    start_proxy()
