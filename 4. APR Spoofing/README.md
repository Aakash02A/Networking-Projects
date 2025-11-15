# ARP Spoofer (Python + Tkinter)

A simple beginner-friendly ARP Spoofing tool built using **Python**, **Scapy**, and **Tkinter**.
This project demonstrates how ARP Poisoning and MITM (Man-In-The-Middle) attacks work at OSI Layer 2.

---

## 🚀 Features
- 🔥 ARP Spoofing (Victim ↔ Router)
- 🧪 Man-in-the-Middle Basics
- 🎨 Simple Tkinter GUI
- 🧠 Educational project
- 🖥 Works on Parrot OS / Kali / Linux

---

## 📡 Workflow (How It Works)
1. ARP normally maps IP → MAC address on a LAN.
2. The attacker sends spoofed ARP replies:
   - To victim: "I am the router"
   - To router: "I am the victim"
3. Both devices update their ARP tables.
4. Attacker becomes MITM.
5. Traffic flows through attacker.

---

## 📦 Requirements
- Python 3
- Scapy: `pip install scapy`
- Tkinter (preinstalled on Linux)
- Root privileges (ARP is Layer-2)

---

## 🛠 Steps to Run

### 1. Install Scapy
```
pip install scapy
```

### 2. Run the Script
```
sudo python3 arp_gui.py
```

### 3. In the GUI
- Enter **Target IP** (victim)
- Enter **Gateway IP** (router)
- Click **Start Attack**

---