import tkinter as tk
from tkinter import ttk

# -------------------------------------------------------
# Mock Encryption (Simple & Safe)
# -------------------------------------------------------
def mock_encrypt(data: str) -> str:
    return "".join(chr((ord(c) + 2)) for c in data)

def mock_decrypt(data: str) -> str:
    return "".join(chr((ord(c) - 2)) for c in data)


# -------------------------------------------------------
# VPN Simulator Logic
# -------------------------------------------------------
class VPNSimulator:
    def __init__(self, ui):
        self.ui = ui
        self.vpn_enabled = False

    def toggle_vpn(self):
        self.vpn_enabled = not self.vpn_enabled
        status = "ENABLED" if self.vpn_enabled else "DISABLED"

        self.ui.update_routing_table(self.vpn_enabled)
        self.ui.log(f"[INFO] VPN {status}")

    def send_packet(self, message: str):
        if not message.strip():
            self.ui.log("[WARN] No message entered!")
            return

        self.ui.log(f"[CLIENT] Message to send → {message}")

        # Create inner packet
        inner_packet = f"INNER({message})"
        self.ui.log(f"[STEP] Inner packet created → {inner_packet}")

        if self.vpn_enabled:
            # Encrypt
            encrypted = mock_encrypt(inner_packet)
            self.ui.log(f"[STEP] Encrypted → {encrypted}")

            # Encapsulate
            outer_packet = f"OUTER[TUNNEL]::{encrypted}"
            self.ui.log(f"[STEP] Encapsulated → {outer_packet}")

            # Tunnel simulation
            self.ui.log("[TUNNEL] Packet moving through secure VPN tunnel...")

            # Server decapsulation
            decrypted = mock_decrypt(encrypted)
            self.ui.log(f"[SERVER] Decrypted inner packet → {decrypted}")

            # Extract final message
            delivered_msg = decrypted.replace("INNER(", "").replace(")", "")
            self.ui.log(f"[SERVER] Final Delivered Message → {delivered_msg}")

        else:
            # No VPN → direct internet
            self.ui.log("[NETWORK] Sending packet in clear-text...")
            self.ui.log(f"[SERVER] Delivered → {message}")


# -------------------------------------------------------
# Tkinter UI Layer
# -------------------------------------------------------
class VPN_UI:
    def __init__(self, root):
        self.root = root
        root.title("VPN Simulator (Educational)")
        root.geometry("850x550")

        main = ttk.Frame(root, padding=10)
        main.grid()

        # ---------------- Input Section ----------------
        ttk.Label(main, text="Enter Message:").grid(row=0, column=0, sticky="w")

        self.msg_entry = ttk.Entry(main, width=45)
        self.msg_entry.grid(row=0, column=1, padx=5, pady=5)

        self.send_button = ttk.Button(main, text="Send Packet", command=self.send_packet)
        self.send_button.grid(row=0, column=2, padx=5)

        self.vpn_button = ttk.Button(main, text="Toggle VPN", command=self.toggle_vpn)
        self.vpn_button.grid(row=1, column=2, pady=5)

        # ---------------- Routing Table ----------------
        ttk.Label(main, text="Routing Table:").grid(row=1, column=0, sticky="nw")

        self.routing_box = tk.Text(main, width=40, height=6, borderwidth=2, relief="groove")
        self.routing_box.grid(row=1, column=1, padx=5)

        # Initial routing table
        self.update_routing_table(False)

        # ---------------- Log Window ----------------
        ttk.Label(main, text="Event Log:").grid(row=2, column=0, sticky="nw")

        self.log_box = tk.Text(main, width=90, height=25, borderwidth=2, relief="groove")
        self.log_box.grid(row=2, column=1, columnspan=2, pady=5)

        # Bind logic engine
        self.sim = VPNSimulator(self)

    # Actions
    def toggle_vpn(self):
        self.sim.toggle_vpn()

    def send_packet(self):
        msg = self.msg_entry.get()
        self.sim.send_packet(msg)

    # Logging
    def log(self, text: str):
        self.log_box.insert(tk.END, text + "\n")
        self.log_box.see(tk.END)

    # Routing Table Renderer
    def update_routing_table(self, vpn_active: bool):
        self.routing_box.delete("1.0", tk.END)

        if vpn_active:
            table = (
                "Destination         Interface\n"
                "0.0.0.0/0           tun0 (VPN)\n"
                "10.8.0.0/24         tun0\n"
                "Local Network       eth0\n"
            )
        else:
            table = (
                "Destination         Interface\n"
                "0.0.0.0/0           eth0\n"
                "Local Network       eth0\n"
            )

        self.routing_box.insert("1.0", table)


# -------------------------------------------------------
# Run Application
# -------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = VPN_UI(root)
    root.mainloop()
