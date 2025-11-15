import socket
import struct
import tkinter as tk
from tkinter import scrolledtext
import threading

INTERFACE = "wlan0"   # Change if needed (eth0, wlan1 etc.)

# ------------------------
# Parse Packet Headers
# ------------------------

def parse_ethernet_header(data):
    dest, src, proto = struct.unpack("!6s6sH", data[:14])
    return {
        "dest": dest.hex(":"),
        "src": src.hex(":"),
        "proto": proto
    }, data[14:]

def parse_ip_header(data):
    version_ihl = data[0]
    version = version_ihl >> 4
    ihl = (version_ihl & 0xF) * 4

    iph = struct.unpack("!BBHHHBBH4s4s", data[:20])

    return {
        "version": version,
        "src": socket.inet_ntoa(iph[8]),
        "dst": socket.inet_ntoa(iph[9]),
        "protocol": iph[6]
    }, data[ihl:]

def parse_tcp_header(data):
    tcph = struct.unpack("!HHLLBBHHH", data[:20])
    return {
        "src_port": tcph[0],
        "dst_port": tcph[1]
    }

def parse_udp_header(data):
    udph = struct.unpack("!HHHH", data[:8])
    return {
        "src_port": udph[0],
        "dst_port": udph[1]
    }

# ------------------------
# Sniffing Thread
# ------------------------

def sniff_packets(output_box):
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    sock.bind((INTERFACE, 0))

    output_box.insert(tk.END, f"[+] Sniffing on {INTERFACE} ...\n")

    while True:
        raw_data, _ = sock.recvfrom(65535)

        eth, payload = parse_ethernet_header(raw_data)
        line = f"\n--- Ethernet ---\nsrc: {eth['src']} → dst: {eth['dest']} | proto: {hex(eth['proto'])}\n"

        if eth["proto"] == 0x0800:  # IPv4
            ip, payload = parse_ip_header(payload)
            line += f"IP: {ip['src']} → {ip['dst']} | Protocol: {ip['protocol']}\n"

            if ip["protocol"] == 6:  # TCP
                tcp = parse_tcp_header(payload)
                line += f"TCP: {tcp['src_port']} → {tcp['dst_port']}\n"

            elif ip["protocol"] == 17:  # UDP
                udp = parse_udp_header(payload)
                line += f"UDP: {udp['src_port']} → {udp['dst_port']}\n"

        output_box.insert(tk.END, line)
        output_box.see(tk.END)


# ------------------------
# GUI
# ------------------------

def start_gui():
    root = tk.Tk()
    root.title("Simple Packet Sniffer (Linux)")

    output_box = scrolledtext.ScrolledText(root, height=30, width=100)
    output_box.pack()

    thread = threading.Thread(target=sniff_packets, args=(output_box,), daemon=True)
    thread.start()

    root.mainloop()

if __name__ == "__main__":
    start_gui()
