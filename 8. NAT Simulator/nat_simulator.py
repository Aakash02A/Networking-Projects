import tkinter as tk
from tkinter import ttk

# ------------------------------
# NAT Simulator Core
# ------------------------------
class NATSimulator:
    def __init__(self, ui):
        self.ui = ui
        self.public_ip = "203.0.113.10"
        self.translation_table = {}  # key: (private_ip, private_port) -> (public_ip, public_port)
        self.next_port = 60000

    def send_packet(self, private_ip, private_port, message):
        key = (private_ip, private_port)

        # Allocate public port if not already mapped
        if key not in self.translation_table:
            public_port = self.next_port
            self.next_port += 1
            self.translation_table[key] = (self.public_ip, public_port)
            self.ui.log(f"[NAT] Mapping created: {private_ip}:{private_port} -> {self.public_ip}:{public_port}")
        else:
            public_port = self.translation_table[key][1]
            self.ui.log(f"[NAT] Existing mapping used: {private_ip}:{private_port} -> {self.public_ip}:{public_port}")

        # Simulate packet going to public network
        outer_packet = f"Packet[{self.public_ip}:{public_port}] -> Internet | Data: {message}"
        self.ui.log(f"[NETWORK] Sending: {outer_packet}")

        # Simulate response from public network
        response = f"Response for {message}"
        self.receive_packet(public_port, response)

        # Update routing table view
        self.ui.update_translation_table(self.translation_table)

    def receive_packet(self, public_port, message):
        # Reverse lookup: public port -> private IP/port
        for (priv_ip, priv_port), (pub_ip, pub_port) in self.translation_table.items():
            if pub_port == public_port:
                self.ui.log(f"[NAT] Translating back: {pub_ip}:{pub_port} -> {priv_ip}:{priv_port}")
                self.ui.log(f"[CLIENT] Delivered to {priv_ip}:{priv_port}: {message}")
                break

# ------------------------------
# UI Class
# ------------------------------
class NAT_UI:
    def __init__(self, root):
        self.root = root
        root.title("NAT Simulator - Educational")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.grid()

        # Private IP input
        ttk.Label(self.frame, text="Private IP:").grid(row=0, column=0, sticky="w")
        self.ip_entry = ttk.Entry(self.frame, width=15)
        self.ip_entry.grid(row=0, column=1, padx=5)
        self.ip_entry.insert(0, "192.168.1.5")

        # Private Port input
        ttk.Label(self.frame, text="Private Port:").grid(row=0, column=2, sticky="w")
        self.port_entry = ttk.Entry(self.frame, width=8)
        self.port_entry.grid(row=0, column=3, padx=5)
        self.port_entry.insert(0, "3456")

        # Message input
        ttk.Label(self.frame, text="Message:").grid(row=1, column=0, sticky="w")
        self.msg_entry = ttk.Entry(self.frame, width=40)
        self.msg_entry.grid(row=1, column=1, columnspan=3, padx=5)

        # Send button
        self.send_btn = ttk.Button(self.frame, text="Send Packet", command=self.send_packet)
        self.send_btn.grid(row=1, column=4, padx=5)

        # Translation table
        ttk.Label(self.frame, text="Translation Table:").grid(row=2, column=0, sticky="w")
        self.table_box = tk.Text(self.frame, width=60, height=8)
        self.table_box.grid(row=3, column=0, columnspan=5, pady=5)

        # Logs
        ttk.Label(self.frame, text="Event Log:").grid(row=4, column=0, sticky="nw")
        self.log_box = tk.Text(self.frame, width=80, height=15)
        self.log_box.grid(row=5, column=0, columnspan=5)

        # Initialize simulator
        self.sim = NATSimulator(self)

    # Button callback
    def send_packet(self):
        ip = self.ip_entry.get()
        try:
            port = int(self.port_entry.get())
        except ValueError:
            self.log("[ERROR] Invalid port")
            return
        msg = self.msg_entry.get()
        self.sim.send_packet(ip, port, msg)

    # Logging
    def log(self, text):
        self.log_box.insert(tk.END, text + "\n")
        self.log_box.see(tk.END)

    # Translation table renderer
    def update_translation_table(self, table):
        self.table_box.delete("1.0", tk.END)
        self.table_box.insert(tk.END, "Private IP:Port -> Public IP:Port\n")
        for (priv_ip, priv_port), (pub_ip, pub_port) in table.items():
            self.table_box.insert(tk.END, f"{priv_ip}:{priv_port} -> {pub_ip}:{pub_port}\n")

# ------------------------------
# Start App
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = NAT_UI(root)
    root.mainloop()
