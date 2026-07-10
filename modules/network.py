"""
NetGuardian Pro - Network Module
Handles network information retrieval.
"""

import psutil
import socket
import requests


# ==============================
# Local IP Address
# ==============================
def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except:
        try:
            hostname = socket.gethostname()
            return socket.gethostbyname(hostname)
        except:
            return "Unavailable"


# ==============================
# Public IP Address
# ==============================
def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org", timeout=1.5)
        return response.text.strip()
    except:
        return "Unavailable"


# ==============================
# Network Status
# ==============================
def get_network_status():
    try:
        conn = socket.create_connection(("8.8.8.8", 53), timeout=1.5)
        conn.close()
        return "Connected"
    except:
        return "Disconnected"


# ==============================
# Network Traffic
# ==============================
def get_network_usage():
    counters = psutil.net_io_counters()
    sent = counters.bytes_sent / (1024 * 1024)
    received = counters.bytes_recv / (1024 * 1024)
    return round(sent, 2), round(received, 2)