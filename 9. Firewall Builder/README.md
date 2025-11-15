# 🔥 Firewall Builder  
**Educational Packet Filtering & Rule-Based Firewall Simulator (Python + Tkinter)**

This project is a safe, fully **offline simulator** that demonstrates how **firewalls filter network traffic** using **rules, port blocking, and packet inspection**, without touching any real network interfaces.

---

# 📘 What Is a Firewall?

A firewall is a network security device (software or hardware) that monitors **incoming and outgoing packets** and decides whether to **allow, block, or log** them based on predefined rules.

Key types of firewall rules:
- **Allow** – Let the packet pass
- **Deny / Drop** – Block the packet silently
- **Log** – Record packet info for analysis

This simulator **visualizes the process** of packet evaluation step-by-step.

---

# 🧠 Key Concepts Demonstrated

### 🔹 1. Packet Filtering
Each packet is evaluated against rules that consider:
- Source IP  
- Destination IP  
- Protocol (TCP/UDP/ICMP)  
- Port (e.g., 80, 22, 443)

### 🔹 2. Rule Evaluation Order
Rules are processed **top-down**, and the first matching rule determines the action.

### 🔹 3. Port Blocking
Simulate denying access to specific ports (HTTP, SSH, FTP) to illustrate real-world firewall usage.

### 🔹 4. Logging
Each packet logs its decision and the rule that applied:
```
Packet[192.168.1.5:1234 -> 203.0.113.10:80, TCP] -> BLOCKED by Rule #2 (Port 80)
```

### 🔹 5. Packet Flow Visualization

```
Packet -> Firewall -> Rule Check -> Action (Allow/Block/Log) -> Client / Network
```
---

# 🏗️ Architecture
```
+-------------------+
| Packet Generator  |
+-------------------+
        |
        v
+-------------------+ +--------------------------+
| Rule Evaluation   | ----> | Decision & Logging |
+-------------------+ +--------------------------+
        |
        v
+-------------------+
| Packet Flow Panel |
+-------------------+
```
---

# ▶️ Running the Simulator
```
python firewall_builder.py
```

# 🔒 Security & Safety Disclaimer

This project:
- **Does NOT interact with the real network**  
- **Does NOT modify OS firewall rules**  
- **Is safe for classroom, tutorials, and personal study**  

It **only simulates packet evaluation** to teach firewall concepts.

---

# 📦 Files

| File | Description |
|------|-------------|
| `firewall_simulator.py` | Main Tkinter application |
| `README.md` | Documentation |

---

# 🚀 Future Enhancements
- Add **custom rule editor** (allow users to add/remove rules)  
- Add **logging export**  
- Simulate **stateful inspection** (tracking TCP connections)  
- Animated packet flow with color-coded rule matches  

---