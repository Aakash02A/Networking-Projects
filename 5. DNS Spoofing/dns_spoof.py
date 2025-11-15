"""
dns_spoof_simulator.py

Educational DNS spoofing / cache-poisoning simulator (SIMULATION ONLY).
No real network activity. Use for teaching/demonstration.

Requirements: Python 3.x (tkinter is part of standard lib)
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time
import threading
import random

# --- Simulation backend (no network) ---

class DNSResolverSim:
    def __init__(self, log_callback):
        # cache: name -> (ip, ttl_expiry_timestamp, source)
        # source: "auth" (authoritative), "cache", "attacker"
        self.cache = {}
        self.log = log_callback
        # simulated authoritative database
        self.auth_db = {
            "example.com": ("93.184.216.34", 300),
            "bank.com": ("192.0.2.10", 600),
            "service.local": ("10.0.0.5", 120),
        }
        self.lock = threading.Lock()

    def query(self, name):
        """Simulate a client query to the resolver."""
        now = time.time()
        with self.lock:
            # expire any stale cache entries
            expired = [k for k, v in self.cache.items() if v[1] <= now]
            for k in expired:
                del self.cache[k]
                self.log(f"[CACHE] TTL expired for {k}")

            if name in self.cache:
                ip, expiry, source = self.cache[name]
                remain = int(expiry - now)
                self.log(f"[RESOLVER] Cache HIT for {name} -> {ip} (source={source}, ttl={remain}s)")
                return ip, source
            else:
                # cache miss -> perform "recursive" query (simulated delay)
                self.log(f"[RESOLVER] Cache MISS for {name}. Querying authoritative servers...")
        # simulate network delay and potential attacker reply race (but this is simulated)
        time.sleep(random.uniform(0.3, 1.0))

        # Simulate authoritative response (if known), else NXDOMAIN
        with self.lock:
            if name in self.auth_db:
                ip, ttl = self.auth_db[name]
                expiry = time.time() + ttl
                self.cache[name] = (ip, expiry, "auth")
                self.log(f"[AUTH] Authoritative response: {name} -> {ip} (ttl={ttl}s)")
                return ip, "auth"
            else:
                self.log(f"[AUTH] NXDOMAIN (no record for {name})")
                return None, "auth"

    def inject_attacker_record(self, name, ip, fake_ttl=3600):
        """Simulate attacker injecting forged record into resolver cache."""
        now = time.time()
        with self.lock:
            expiry = now + fake_ttl
            self.cache[name] = (ip, expiry, "attacker")
            self.log(f"[ATTACK] Forged record injected: {name} -> {ip} (ttl={fake_ttl}s)")

    def clear_cache(self):
        with self.lock:
            self.cache.clear()
            self.log("[RESOLVER] Cache cleared by operator.")

    def get_cache_snapshot(self):
        now = time.time()
        with self.lock:
            snapshot = []
            for name, (ip, expiry, source) in self.cache.items():
                ttl = max(0, int(expiry - now))
                snapshot.append((name, ip, ttl, source))
            return snapshot

# --- GUI ---

class DNSGui:
    def __init__(self, root):
        self.root = root
        root.title("DNS Spoofing Simulator — Educational (NO NETWORK)")

        # logger area
        self.log_area = scrolledtext.ScrolledText(root, height=12, state="disabled", wrap="word")
        self.log_area.pack(fill="both", padx=8, pady=(8,4), expand=False)

        # top frame: query controls
        top_frame = ttk.Frame(root)
        top_frame.pack(fill="x", padx=8, pady=4)

        ttk.Label(top_frame, text="Domain name:").grid(row=0, column=0, sticky="w")
        self.domain_var = tk.StringVar(value="example.com")
        self.domain_entry = ttk.Entry(top_frame, textvariable=self.domain_var, width=30)
        self.domain_entry.grid(row=0, column=1, sticky="w", padx=(4,8))

        self.query_btn = ttk.Button(top_frame, text="Query Resolver", command=self.perform_query)
        self.query_btn.grid(row=0, column=2, padx=(0,8))

        self.clear_log_btn = ttk.Button(top_frame, text="Clear Log", command=self.clear_log)
        self.clear_log_btn.grid(row=0, column=3)

        # middle frame: cache display and attacker controls
        mid_frame = ttk.Frame(root)
        mid_frame.pack(fill="both", expand=True, padx=8, pady=4)

        # left: cache table
        cache_frame = ttk.LabelFrame(mid_frame, text="Resolver Cache")
        cache_frame.pack(side="left", fill="both", expand=True, padx=(0,8))

        self.cache_tree = ttk.Treeview(cache_frame, columns=("ip","ttl","src"), show="headings", height=8)
        self.cache_tree.heading("ip", text="IP")
        self.cache_tree.heading("ttl", text="TTL (s)")
        self.cache_tree.heading("src", text="Source")
        self.cache_tree.pack(fill="both", expand=True, padx=4, pady=4)

        # right: attacker controls
        attack_frame = ttk.LabelFrame(mid_frame, text="Attacker (SIMULATION ONLY)")
        attack_frame.pack(side="right", fill="y", expand=False)

        ttk.Label(attack_frame, text="Target domain:").pack(anchor="w", padx=6, pady=(6,0))
        self.atk_domain = tk.StringVar(value="example.com")
        ttk.Entry(attack_frame, textvariable=self.atk_domain, width=24).pack(padx=6)

        ttk.Label(attack_frame, text="Fake IP:").pack(anchor="w", padx=6, pady=(6,0))
        self.atk_ip = tk.StringVar(value="203.0.113.55")
        ttk.Entry(attack_frame, textvariable=self.atk_ip, width=24).pack(padx=6)

        ttk.Label(attack_frame, text="Fake TTL (s):").pack(anchor="w", padx=6, pady=(6,0))
        self.atk_ttl = tk.IntVar(value=3600)
        ttk.Entry(attack_frame, textvariable=self.atk_ttl, width=24).pack(padx=6, pady=(0,6))

        ttk.Button(attack_frame, text="Inject Forged Record", command=self.inject_forged).pack(padx=6, pady=(0,8), fill="x")
        ttk.Button(attack_frame, text="Clear Resolver Cache", command=self.clear_cache).pack(padx=6, pady=(0,8), fill="x")
        ttk.Button(attack_frame, text="Simulate Authoritative Change", command=self.simulate_auth_change).pack(padx=6, pady=(0,8), fill="x")

        # bottom: status / legend
        bottom = ttk.Frame(root)
        bottom.pack(fill="x", padx=8, pady=(0,8))
        ttk.Label(bottom, text="Legend: source=auth (authoritative response), cache (cached), attacker (forged)").pack(anchor="w")

        # backend
        self.sim = DNSResolverSim(self.log)
        # refresh cache view periodically
        self.refresh_cache_periodically()

    # --- UI actions ---
    def log(self, msg):
        ts = time.strftime("%H:%M:%S")
        self.log_area.configure(state="normal")
        self.log_area.insert("end", f"{ts} {msg}\n")
        self.log_area.see("end")
        self.log_area.configure(state="disabled")

    def clear_log(self):
        self.log_area.configure(state="normal")
        self.log_area.delete("1.0", "end")
        self.log_area.configure(state="disabled")

    def perform_query(self):
        name = self.domain_var.get().strip()
        if not name:
            messagebox.showwarning("Input required", "Please enter a domain name.")
            return
        # run query in background thread to avoid blocking UI
        threading.Thread(target=self._query_thread, args=(name,), daemon=True).start()

    def _query_thread(self, name):
        ip, source = self.sim.query(name)
        if ip:
            self.log(f"[CLIENT] Final resolution for {name} -> {ip} (resolved_by={source})")
        else:
            self.log(f"[CLIENT] {name} could not be resolved (NXDOMAIN)")

    def inject_forged(self):
        name = self.atk_domain.get().strip()
        ip = self.atk_ip.get().strip()
        ttl = int(self.atk_ttl.get())
        if not name or not ip:
            messagebox.showwarning("Input required", "Attacker target and IP required.")
            return
        self.sim.inject_attacker_record(name, ip, fake_ttl=ttl)
        self.refresh_cache_view()

    def clear_cache(self):
        self.sim.clear_cache()
        self.refresh_cache_view()

    def simulate_auth_change(self):
        """Simulate authoritative record change; used to show mismatch detection."""
        name = self.atk_domain.get().strip()
        # Change authoritative DB to a different IP (simulated)
        with self.sim.lock:
            if name in self.sim.auth_db:
                old_ip, old_ttl = self.sim.auth_db[name]
                new_ip = ".".join(str(random.randint(1, 250)) for _ in range(4))
                self.sim.auth_db[name] = (new_ip, old_ttl)
                self.log(f"[SIM-AUTH] Authoritative DB changed: {name} -> {new_ip}")
            else:
                # create a new auth record
                new_ip = ".".join(str(random.randint(1, 250)) for _ in range(4))
                self.sim.auth_db[name] = (new_ip, 300)
                self.log(f"[SIM-AUTH] Authoritative DB added: {name} -> {new_ip}")
        self.refresh_cache_view()

    def refresh_cache_view(self):
        # update tree
        for i in self.cache_tree.get_children():
            self.cache_tree.delete(i)
        snapshot = self.sim.get_cache_snapshot()
        for name, ip, ttl, src in snapshot:
            self.cache_tree.insert("", "end", values=(f"{name} → {ip}", ttl, src))

    def refresh_cache_periodically(self):
        self.refresh_cache_view()
        # schedule next refresh
        self.root.after(1000, self.refresh_cache_periodically)


def main():
    root = tk.Tk()
    app = DNSGui(root)
    root.geometry("820x520")
    root.mainloop()

if __name__ == "__main__":
    main()
