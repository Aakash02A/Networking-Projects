import tkinter as tk
from tkinter import ttk

# ------------------------------
# Firewall Simulator Core
# ------------------------------
class FirewallSimulator:
    def __init__(self, ui):
        self.ui = ui
        # Predefined rules: list of dicts
        # Top-down priority: first match applies
        self.rules = [
            {"action": "ALLOW", "protocol": "TCP", "port": 22},   # Allow SSH
            {"action": "BLOCK", "protocol": "TCP", "port": 80},   # Block HTTP
            {"action": "ALLOW", "protocol": "TCP", "port": 443},  # Allow HTTPS
            {"action": "BLOCK", "protocol": "UDP", "port": 53},   # Block DNS over UDP
        ]

    def send_packet(self, src_ip, dst_ip, protocol, port):
        packet = f"Packet[{src_ip} -> {dst_ip}, {protocol}:{port}]"
        self.ui.log(f"[CLIENT] Sending: {packet}")

        # Evaluate packet against rules
        for idx, rule in enumerate(self.rules, 1):
            if rule["protocol"] == protocol and rule["port"] == port:
                action = rule["action"]
                self.ui.log(f"[FIREWALL] Rule #{idx} matched: {action} ({protocol}:{port})")
                self.ui.log(f"[RESULT] {action}ED {packet}\n")
                return

        # Default policy
        self.ui.log(f"[FIREWALL] No matching rule. DEFAULT ALLOW {packet}\n")

# ------------------------------
# UI Class
# ------------------------------
class Firewall_UI:
    def __init__(self, root):
        self.root = root
        root.title("Firewall Simulator - Educational")

        self.frame = ttk.Frame(root, padding=10)
        self.frame.grid()

        # Source IP
        ttk.Label(self.frame, text="Source IP:").grid(row=0, column=0, sticky="w")
        self.src_entry = ttk.Entry(self.frame, width=15)
        self.src_entry.grid(row=0, column=1)
        self.src_entry.insert(0, "192.168.1.5")

        # Destination IP
        ttk.Label(self.frame, text="Destination IP:").grid(row=0, column=2, sticky="w")
        self.dst_entry = ttk.Entry(self.frame, width=15)
        self.dst_entry.grid(row=0, column=3)
        self.dst_entry.insert(0, "203.0.113.10")

        # Protocol
        ttk.Label(self.frame, text="Protocol:").grid(row=1, column=0, sticky="w")
        self.proto_entry = ttk.Entry(self.frame, width=10)
        self.proto_entry.grid(row=1, column=1)
        self.proto_entry.insert(0, "TCP")

        # Port
        ttk.Label(self.frame, text="Port:").grid(row=1, column=2, sticky="w")
        self.port_entry = ttk.Entry(self.frame, width=10)
        self.port_entry.grid(row=1, column=3)
        self.port_entry.insert(0, "80")

        # Send Button
        self.send_btn = ttk.Button(self.frame, text="Send Packet", command=self.send_packet)
        self.send_btn.grid(row=2, column=0, columnspan=4, pady=5)

        # Log Box
        ttk.Label(self.frame, text="Event Log:").grid(row=3, column=0, sticky="nw")
        self.log_box = tk.Text(self.frame, width=80, height=20)
        self.log_box.grid(row=4, column=0, columnspan=4)

        self.sim = FirewallSimulator(self)

    def send_packet(self):
        src_ip = self.src_entry.get()
        dst_ip = self.dst_entry.get()
        protocol = self.proto_entry.get().upper()
        try:
            port = int(self.port_entry.get())
        except ValueError:
            self.log("[ERROR] Invalid port")
            return
        self.sim.send_packet(src_ip, dst_ip, protocol, port)

    # Logging
    def log(self, text):
        self.log_box.insert(tk.END, text + "\n")
        self.log_box.see(tk.END)

# ------------------------------
# Start App
# ------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = Firewall_UI(root)
    root.mainloop()
