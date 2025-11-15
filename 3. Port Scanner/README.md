# Simple Python Port Scanner (with Tkinter GUI)

A beginner-friendly port scanner that uses Python sockets to perform a TCP handshake and optionally grab service banners.  
Includes both a **terminal version** and a **Tkinter graphical interface**.

---

## 📌 Workflow

1. User enters a target (IP/domain) and port range.  
2. Scanner tries a **TCP connect()** to each port:
   - If connection succeeds → **Port is OPEN**
   - If connection fails → **Port is CLOSED**
3. For open ports, the scanner tries **banner grabbing**:
   - Some services send identifying text (e.g., SSH, HTTP)
4. Results are displayed in terminal or GUI.

---

## ⭐ Features

- Simple to understand  
- No external libraries  
- Works on Linux, Windows, macOS  
- TCP handshake based scanning  
- Optional banner grabbing  
- Tkinter GUI version included  
- Fast scanning with socket timeouts  

---

## 🧰 Requirements (and Why)

| Requirement | Why |
|------------|-----|
| Python 3 | Required to run the scripts |
| Tkinter (GUI only) | Used to display results in the window |
| Internet/local network | Needed to scan remote or LAN devices |

No root/sudo required because we use **TCP connect()**, not raw sockets.

---

## ▶️ Steps to Run

### **Run the Terminal Version**
```
python3 port_scanner.py
```
