import socket
import tkinter as tk
from tkinter import scrolledtext
import threading

def scan_port(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))

        # Banner grabbing attempt
        try:
            banner = sock.recv(1024).decode(errors="ignore").strip()
        except:
            banner = "No banner"

        sock.close()
        return True, banner

    except:
        return False, None


def start_scan(target, start_port, end_port, textbox):
    textbox.insert(tk.END, f"Scanning {target}...\n")

    for port in range(start_port, end_port + 1):
        status, banner = scan_port(target, port)

        if status:
            textbox.insert(tk.END, f"[OPEN] Port {port} | Banner: {banner}\n")
        else:
            textbox.insert(tk.END, f"[CLOSED] Port {port}\n")

        textbox.see(tk.END)


def run_scan(entry_target, entry_start, entry_end, textbox):
    target = entry_target.get()
    start_port = int(entry_start.get())
    end_port = int(entry_end.get())

    thread = threading.Thread(
        target=start_scan,
        args=(target, start_port, end_port, textbox),
        daemon=True
    )
    thread.start()


def main():
    root = tk.Tk()
    root.title("Simple Port Scanner")

    tk.Label(root, text="Target:").pack()
    entry_target = tk.Entry(root, width=40)
    entry_target.pack()

    tk.Label(root, text="Start Port:").pack()
    entry_start = tk.Entry(root, width=20)
    entry_start.pack()

    tk.Label(root, text="End Port:").pack()
    entry_end = tk.Entry(root, width=20)
    entry_end.pack()

    output = scrolledtext.ScrolledText(root, width=80, height=20)
    output.pack()

    tk.Button(
        root,
        text="Start Scan",
        command=lambda: run_scan(entry_target, entry_start, entry_end, output)
    ).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
