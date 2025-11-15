# Simple HTTP Forward Proxy (Educational Only)

A minimal, non‑malicious **HTTP forward proxy** written in Python using raw sockets.  
This project demonstrates how HTTP requests can be forwarded from a client to an origin server through a proxy.

This proxy:
- Handles **HTTP traffic (port 80)**  
- Supports **HTTPS tunneling** using the `CONNECT` method without interception  
- Does **NOT** decrypt or modify HTTPS  
- Requires explicit proxy configuration in the client/browser  
- Is intended purely for **learning and research**

---

## ⚠️ Safety & Ethical Usage

This proxy is designed to be **safe**:
- No traffic interception  
- No packet modification  
- No header injection  
- No request rewriting  
- No transparent capturing of user data  

It serves as a teaching example of **how forward proxies work** internally.  
Do not deploy this as a production proxy or for security-sensitive tasks.

---

# 🔍 Overview

A forward proxy sits between a client and the destination server.  
Its job is to:
1. Accept client HTTP requests  
2. Parse the request line and headers  
3. Forward the request to the target server  
4. Receive the server’s response  
5. Relay the response back to the client  

This project focuses on the **basic forwarding path** and optional **HTTPS CONNECT tunneling**, without doing any deep inspection.

---

# ✨ Features

### 🔹 Supported
- HTTP GET/POST forwarding  
- HTTPS tunneling (`CONNECT host:port`)  
- Plain socket relaying  
- Threaded request handling  
- Minimal logging for learning  

### 🔸 Not Supported (By Design)
- Caching  
- Request filtering  
- Logging sensitive content  
- Transparent proxying  
- TLS interception / MITM  
- Authentication  
- Content modification  

These omissions keep the proxy simple, safe, and ethically restricted.

---

# 🛠️ Installation

### Requirements
- Python 3.x  
- No external libraries required  

---

# ▶️ Running the Proxy

```
python http_proxy.py
```

Default listens on:
```
http://localhost:8080
```
Configure your browser/client proxy settings:
```
HTTP Proxy: 127.0.0.1
Port: 8080
```

For HTTPS, the client will automatically use:
```
CONNECT example.com:443
```
The proxy only tunnels bytes — it never decrypts HTTPS.

# 📘 How It Works — Simple HTTP Forward Proxy

A forward proxy sits between a **client** (browser, script, device) and the **internet**.  
It receives HTTP requests, parses them, forwards them to the destination server, and returns the response back to the client.

Below is a clear, step‑by‑step explanation of how the proxy operates.

---

## **1️⃣ Client Sends an HTTP Request**

Example client request:
```
GET http://example.com/
 HTTP/1.1
Host: example.com
```


When this reaches the proxy, the proxy does the following:

### ✔ Parses the HTTP request  
It reads the **request line** (`GET http://example.com/ HTTP/1.1`) and the HTTP headers.

### ✔ Extracts the `Host` header  
This tells the proxy **where** the client wants to connect:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256
```


The proxy:

- Reads the response from the server
- Immediately sends the same bytes back to the client  
- Does not change or inspect any body content (non‑malicious behavior)

This is why forward proxies can be used for caching, filtering, or monitoring — but in our minimal safe learning proxy, we avoid such features.

---

## **3️⃣ Handling HTTPS With the `CONNECT` Method**

When the client wants to visit an **HTTPS** website (e.g., https://example.com), it cannot send a normal GET request first because HTTPS is encrypted.

So the browser sends this to the proxy:

```
CONNECT example.com:443 HTTP/1.1
```

This means:

> “Proxy, please open a TCP tunnel to example.com on port 443.  
> I will handle the TLS encryption myself.”

### ✔ Proxy’s Job Here

1. Connect to `example.com:443`
2. Send back:

```
HTTP/1.1 200 Connection Established
```
3. From this point on, it **blindly relays encrypted bytes** between client and server.

The proxy does **not** inspect HTTPS traffic because it is encrypted.

---

## Summary Flow

```
Client → Proxy → Origin Server
↑ ↓
└────── Response ←────┘
```


### For HTTP
- Proxy reads, parses, forwards raw HTTP requests  
- Receives server response and relays it back

### For HTTPS
- Proxy uses CONNECT  
- Creates secure TCP tunnel  
- Blindly forwards encrypted data without modification

---