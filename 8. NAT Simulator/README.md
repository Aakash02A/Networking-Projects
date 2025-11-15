# 🖧 NAT Simulator  
**Educational Network Address Translation (NAT) Visualizer — Python + Tkinter**

This project is a safe, fully **offline simulator** that demonstrates how **NAT works** in modern networks.  
It teaches **private/public IP mapping, translation tables, and packet forwarding**, without touching real network interfaces.

---

# 📘 What Is NAT?

**Network Address Translation (NAT)** allows devices in a private network to communicate with the internet using a **single public IP address or a pool of public IPs**.

Key types:
- **Static NAT:** One-to-one mapping between private and public IPs  
- **Dynamic NAT:** Maps private IPs to public IPs from a pool  
- **Port Address Translation (PAT/NAT overload):** Multiple private IPs share a single public IP using different ports

This simulator **visualizes these concepts** safely in Python + Tkinter.

---

# 🧠 Key Concepts Demonstrated

### 🔹 1. Private → Public IP Mapping
Example:
```
192.168.1.5:3456 -> 203.0.113.10:60001
```

### 🔹 2. Translation Table
Tracks active connections:

| Private IP       | Private Port | Public IP      | Public Port |
|-----------------|--------------|----------------|-------------|
| 192.168.1.5     | 3456         | 203.0.113.10   | 60001       |
| 192.168.1.6     | 3457         | 203.0.113.10   | 60002       |

### 🔹 3. Packet Flow Visualization
```
Private Host -> NAT Simulator -> Public Network
Public Network -> NAT Simulator -> Private Host
```

Shows how headers are modified and how reverse translation works.

### 🔹 4. Port Address Translation (PAT)
Multiple private hosts can share the same public IP by assigning **unique source ports**.

---

# 🏗️ Architecture

+-------------------+
| User Input Pane   |
+-------------------+
        |
        v
+-------------------+ +-----------------------+
| Packet Generator  | ----> | NAT Translation |
+-------------------+ +-----------------------+
        | |
        v v
+------------------------------------------------+
| Translation Table / Routing View               |
+------------------------------------------------+
        |
        v
+-------------------+
| Packet Flow Panel |
+-------------------+


---

# ▶️ Running the Simulator
``
python nat_simulator.py
```

---

# 🔒 Security & Safety Disclaimer

This project:
- **Does NOT modify actual network traffic**
- **Does NOT require administrative privileges**
- **Is safe for classroom and personal study**
- **Demonstrates only conceptual NAT behavior**

---

# 📦 Files

| File | Description |
|------|-------------|
| `nat_simulator.py` | Main Tkinter application |
| `README.md` | Documentation |

---
