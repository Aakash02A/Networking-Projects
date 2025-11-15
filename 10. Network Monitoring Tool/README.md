# 📡 Real-Time Network Monitoring Tool  
A safe, real-time bandwidth monitoring tool built using **Python**, **Tkinter**, and **psutil**.

Unlike simulators, this version reads **actual network usage** from your system:
- Bytes sent per second
- Bytes received per second
- Packets sent/received
- Total bandwidth statistics

This tool does **not** capture packets, inspect payloads, or perform sniffing.  
It only accesses OS-level network counters using the `psutil` library, making it **safe, legal, and suitable for students, labs, and learning environments**.

---

## 🚀 Features

### ✔ Real-time Bandwidth Monitoring
Continuously displays:
- **Upload speed (bytes/sec)**
- **Download speed (bytes/sec)**
- **Total bytes sent/received**
- **Packets sent/received**

### ✔ Graph-Friendly Architecture
Bandwidth values update once per second.  
(You can easily add live graphs later — matplotlib supported.)

### ✔ Cross-Platform
Works on:
- Windows  
- macOS  
- Linux  

### ✔ Safe & Permission-Free
- No raw sockets  
- No packet sniffing  
- No admin/root rights needed  

---

## 🧠 Learning Outcomes

By using this tool, you will learn:

### 🔹 How operating systems track network usage
- NIC counters  
- Bytes-per-second calculation  
- Packet statistics  

### 🔹 How monitoring dashboards work
- Timed loops  
- UI state updates  
- Real-time metrics  

### 🔹 How to build system tools with Python
- Using `psutil`  
- Tkinter GUI design  
- Thread-safe UI updates  

---

## 🏗️ Architecture
```
+------------------------------+
| psutil.net_io_counters()     |
+------------------------------+
                |
                v
+------------------------------+
| Bandwidth Calculator         |
| (delta bytes / delta time)   |
+------------------------------+
                |
                v
+------------------------------+
| Tkinter GUI Display          |
+------------------------------+
```
## ▶️ Run the Program
```
python realtime_monitor.py
```