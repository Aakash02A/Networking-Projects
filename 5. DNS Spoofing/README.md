# DNS Spoofing Simulator (Educational Only)

A fully safe, **network-isolated** DNS Spoofing & Cache Poisoning **simulator** built using **Python + Tkinter**.  
This project visually demonstrates how DNS resolution, caching, forged responses, and TTL expiration work — **without sending or receiving any network packets.**

This tool is ideal for:
- Cybersecurity students  
- Teachers explaining DNS vulnerabilities  
- Demonstrations of cache poisoning concepts  
- Lab environments where real attacks cannot be executed  

---

## ⚠️ Disclaimer

This simulator **DOES NOT** perform real DNS spoofing or any network-level exploitation.  
It only models the logic **locally** for educational and defensive awareness purposes.

---

# 📘 Table of Contents
1. [Overview](#overview)  
2. [How DNS Spoofing Works](#how-dns-spoofing-works)  
3. [Simulator Features](#simulator-features)  
4. [Project Structure](#project-structure)  
5. [Installation](#installation)  
6. [Running the Program](#running-the-program)  
7. [How to Use the Simulator](#how-to-use-the-simulator)  
8. [Screenshots (optional section placeholder)](#screenshots)  
9. [Future Enhancements](#future-enhancements)  
10. [License](#license)

---

# 🔍 Overview

DNS spoofing (also known as DNS cache poisoning) is an attack technique where an adversary injects **false DNS records** into a DNS resolver’s cache, causing users to be redirected to malicious IP addresses.

This project simulates:
- DNS queries  
- Resolver cache behavior  
- Authoritative responses  
- Attacker-injected forged records  
- TTL expiration and cache refresh  
- Mismatched authoritative records  

All behavior is self-contained inside Python classes — providing a safe and interactive learning tool.

---

# 🌐 How DNS Spoofing Works

### **1. What is DNS Spoofing?**
DNS spoofing is the manipulation of DNS lookup results to trick users into visiting harmful or incorrect IP addresses.

### **2. Where It Occurs**
- ISP/corporate recursive DNS resolvers  
- Local OS DNS caches  
- Compromised routers  
- Man-in-the-middle network positions  

### **3. Why Attackers Use It**
- Redirect to phishing websites  
- Intercept login credentials  
- Inject malware  
- Traffic surveillance  
- Bypass trust and authentication  

### **4. Why It’s Dangerous**
A poisoned resolver can affect **thousands of users** automatically and silently.

### **5. Common Defenses**
- DNSSEC  
- Randomized ports and transaction IDs  
- Short cache TTLs  
- DoT / DoH (secure DNS transport)  
- Monitoring and anomaly detection  

The simulator below demonstrates **all cache-related behaviors** without doing any real attack.

---

# ✨ Simulator Features

### 🧩 Core Functions
- **Simulated DNS resolver**
- **Cache with TTL**
- **Authoritative server simulation**
- **Client-side queries**
- **Attacker-injected forged DNS records**

### 🕒 Real-time Behavior
- TTL decrement and expiration  
- Automatic cache refresh  
- Resolver HIT / MISS logic  
- Multi-threaded query simulation  

### 🖥️ GUI (Tkinter)
- Log window  
- Domain query interface  
- Resolver cache table  
- Attacker simulation panel  
- Buttons for:
  - Query
  - Inject forged record
  - Clear cache
  - Change authoritative record

### 🚫 Safe Simulation
- No packet interception  
- No ARP spoofing  
- No DNS server communication  
- No socket usage  

---

# Steps to run code 
```
python dns_spoof_simulator.py

```

# 🎮 How to Use the Simulator

## 1. Query a Domain
- Enter any domain (e.g., `example.com`)
- Click **“Query Resolver”**
- The log window will display:
  - **Cache HIT or MISS**
  - **Authoritative response**
  - **Final resolved IP**

---

## 2. View the Cache Table
The resolver cache table shows:
- **Domain**
- **IP address**
- **Remaining TTL**
- **Source** (`auth`, `attacker`, or `cache`)

---

## 3. Simulate an Attacker
Enter the following in the **Attacker Panel**:
- **Target domain**
- **Fake IP address**
- **Fake TTL**

Click **“Inject Forged Record”**.

Example log output:
```
[ATTACK] Forged record injected: bank.com -> 203.0.113.55
```

---

## 4. Simulate Authoritative Change
Demonstrates how a poisoned cache becomes inconsistent with the real authoritative data.

Shows mismatch between:
- Cached (forged) entries  
- Real authoritative entries  

---

## 5. Clear Cache
- Click **“Clear Resolver Cache”**
- This resets the resolver’s cache and removes any forged or legitimate cached records.

---
