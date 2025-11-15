import tkinter as tk
from tkinter import ttk
import psutil
import time
import threading

class RealTimeMonitor:
    def __init__(self, ui):
        self.ui = ui
        self.running = False

        # Initial counters
        self.prev = psutil.net_io_counters()

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.update_loop, daemon=True).start()
            self.ui.log("Monitoring started...")

    def stop(self):
        self.running = False
        self.ui.log("Monitoring stopped.")

    def update_loop(self):
        while self.running:
            now = psutil.net_io_counters()

            # Calculate bytes per second
            upload_bps = now.bytes_sent - self.prev.bytes_sent
            download_bps = now.bytes_recv - self.prev.bytes_recv

            # Packets
            packets_sent = now.packets_sent - self.prev.packets_sent
            packets_recv = now.packets_recv - self.prev.packets_recv

            self.prev = now  # update baseline

            self.ui.update_stats(upload_bps, download_bps,
                                 now.bytes_sent, now.bytes_recv,
                                 packets_sent, packets_recv)

            time.sleep(1)


class MonitorUI:
    def __init__(self, root):
        self.root = root
        root.title("Real-Time Network Monitor")

        frame = ttk.Frame(root, padding=10)
        frame.grid()

        # Start/Stop Buttons
        ttk.Button(frame, text="Start", command=self.start_monitor).grid(row=0, column=0)
        ttk.Button(frame, text="Stop", command=self.stop_monitor).grid(row=0, column=1)

        # Stats Display
        labels = [
            "Upload Speed (B/s):", "Download Speed (B/s):",
            "Total Bytes Sent:", "Total Bytes Received:",
            "Packets Sent (last 1s):", "Packets Received (last 1s):"
        ]

        self.values = {}

        for i, label in enumerate(labels):
            ttk.Label(frame, text=label).grid(row=i+1, column=0, sticky="w")
            var = tk.StringVar(value="0")
            ttk.Label(frame, textvariable=var).grid(row=i+1, column=1, sticky="w")
            self.values[label] = var

        # Log box
        ttk.Label(frame, text="Event Log:").grid(row=7, column=0, sticky="nw")
        self.log_box = tk.Text(frame, width=60, height=10)
        self.log_box.grid(row=8, column=0, columnspan=2)

        self.monitor = RealTimeMonitor(self)

    def start_monitor(self):
        self.monitor.start()

    def stop_monitor(self):
        self.monitor.stop()

    def update_stats(self, up, down, total_up, total_down, ps, pr):
        self.values["Upload Speed (B/s):"].set(str(up))
        self.values["Download Speed (B/s):"].set(str(down))
        self.values["Total Bytes Sent:"].set(str(total_up))
        self.values["Total Bytes Received:"].set(str(total_down))
        self.values["Packets Sent (last 1s):"].set(str(ps))
        self.values["Packets Received (last 1s):"].set(str(pr))

    def log(self, text):
        self.log_box.insert(tk.END, text + "\n")
        self.log_box.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    ui = MonitorUI(root)
    root.mainloop()
