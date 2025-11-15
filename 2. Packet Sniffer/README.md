# Simple Tkinter Packet Sniffer (Linux)

A basic Python packet sniffer with a Tkinter GUI that captures real network packets on Linux (Parrot OS, Kali, Ubuntu, etc).  
It displays Ethernet, IP, TCP, and UDP details in a scrollable window.

---

## 📌 Workflow

1. Create a **raw socket** using `AF_PACKET` to capture packets.
2. Bind the socket to a network interface (example: `wlan0`).
3. Continuously read raw packet bytes using `recvfrom()`.
4. Split the packet into:
   - Ethernet header  
   - IP header (if IPv4)  
   - TCP/UDP headers (if applicable)
5. Display the decoded packet info in a Tkinter GUI.

---

## ⭐ Features

- Simple Tkinter GUI  
- Captures **real packets** (WiFi or Ethernet)  
- Shows:
  - Source/Destination MAC
  - IP addresses
  - Protocol numbers
  - TCP/UDP ports  
- Auto-scrolling text view  
- Beginner-friendly code  
- No external libraries required

---

## 🧰 Requirements (and Why)

| Requirement | Why It Is Needed |
|------------|------------------|
| **Python 3** | Runs the program |
| **Tkinter** | Used to build the GUI window |
| **Linux OS** | Raw sockets require Linux (`AF_PACKET`) |
| **sudo permission** | Needed to sniff real network packets |
| **Network interface (wlan0/eth0)** | Packets are captured from this device |

---

## ▶️ How to Run the Sniffer

```
Find your network interface
Run:
    ip a
```

```
Look for your WiFi/Ethernet name:
- wlan0  
- wlp2s0  
- eth0  

Update the interface in the code (if needed)
INTERFACE = "wlan0"

```
```
sudo python3 sniffer_gui.py
```

---