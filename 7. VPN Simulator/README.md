# 🛡️ VPN Simulator  
**Educational Virtual Private Network Tunneling & Encryption Visualizer (Python + Tkinter)**

This project is a safe, non‑networking educational simulator that explains **how a VPN works internally** — including **tunneling, encapsulation, mock encryption, routing-table switching, and packet flow** — without touching any real network interfaces.

---

# 📘 What Is a VPN?

A **Virtual Private Network (VPN)** creates a secure, encrypted communication channel (tunnel) between a client and a server.  
Real VPNs (IPSec, OpenVPN, WireGuard) operate at OS kernel level and modify routing tables so that traffic flows through this encrypted tunnel.

This simulator **mimics the concepts**, not the OS behavior.

---

# 🧠 Key Concepts Demonstrated

### 🔹 1. **Tunneling**
Original packets are wrapped inside new packets:

```
[ Outer Header | Encrypted Inner Packet ]
```

This allows private traffic to move inside a secure tunnel.

---

### 🔹 2. **Encryption (Simulated)**
In real VPNs: AES, ChaCha20, RSA, Diffie–Hellman  
In this simulator: **Mock encryption** using reversible string transformation, purely for visualization.

---

### 🔹 3. **Routing Tables**
Normally:

| Destination | Interface |
|------------|-----------|
| Internet   | eth0      |

After VPN:

| Destination | Interface |
|------------|-----------|
| Internet   | tun0 (VPN Tunnel) |

The simulator displays this switch visually.

---

### 🔹 4. **Packet Flow Visualization**

Flow:
```
Client → [Inner Packet] → Encrypt → Encapsulate → Tunnel → Decapsulate → Server
```

The UI shows each stage step‑by‑step.

---

# 🏗️ Architecture

```
+-------------------+
| User Input Pane   |
+-------------------+
        |
        v
+-------------------+ +-------------------------+
| Packet Generator  | ----> | Encryption Module |
+-------------------+ +-------------------------+
        | |
        v v
+------------------------------------------------+
| Tunneling & Encapsulation                      |
+------------------------------------------------+
        |
        v
+-------------------+
| Routing Table UI  |
+-------------------+
        |
        v
+-------------------+
| Packet Flow Panel |
+-------------------+
```

---

# 📷 Screenshots (optional to add later)
- Home screen  
- Routing table before VPN  
- After enabling VPN  
- Packet passing through tunnel  

---

# ▶️ Running the Simulator

```
python vpn_simulator.py
```

---
# 🔒 Security Disclaimer

This project:
- **Does NOT perform real VPN tunneling**
- **Does NOT modify system routing tables**
- **Does NOT create real encrypted channels**
- **Is strictly for educational demonstration**

Safe for students, training, and academic projects.

---

# 📚 Protocol Comparison (Educational Only)

| Feature | IPSec | OpenVPN | WireGuard |
|---------|--------|----------|------------|
| Layer | Network (L3) | Transport (L4) | Kernel/L3 |
| Encryption | AES | AES / BF / others | ChaCha20 |
| Speed | Medium | Medium | Very fast |
| Config | Complex | Moderate | Simple |
| Simulator Support | Conceptual | Conceptual | Conceptual |

---

# 📦 Files

| File | Description |
|------|-------------|
| `vpn_simulator.py` | Main Tkinter application |
| `README.md` | Documentation |

---

# 😊 Author Notes

This simulator is designed to give students and beginners a hands‑on, visual understanding of how VPNs encapsulate and protect data.  
Feel free to extend it with:
- Animated packet flow  
- Real crypto library (still simulated)  
- Visual tunnel diagrams

---