import socket

def scan_port(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)

        # Try TCP connection (TCP handshake)
        sock.connect((target, port))

        try:
            # Try banner grabbing
            banner = sock.recv(1024).decode().strip()
        except:
            banner = "No banner"

        sock.close()
        return True, banner

    except:
        return False, None


if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    print(f"\nScanning {target}...\n")

    for port in range(start, end + 1):
        open_status, banner = scan_port(target, port)

        if open_status:
            print(f"[OPEN] Port {port}  --> Banner: {banner}")
        else:
            print(f"[CLOSED] Port {port}")
