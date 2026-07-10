"""
NetGuardian Pro - Diagnostics Module
Handles network diagnostic tools.
"""

import subprocess
import socket
import platform


# ==============================
# Ping Test
# ==============================
def run_ping(host):
    try:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "4", host]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )

        return result.stdout
    except Exception as e:
        return f"Ping failed: {e}"


# ==============================
# DNS Lookup
# ==============================
def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        return f"{domain} resolves to {ip}"
    except Exception as e:
        return f"DNS lookup failed: {e}"