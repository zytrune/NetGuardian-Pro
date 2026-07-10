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
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except:
        return "Unavailable"


# ==============================
# Public IP Address
# ==============================
def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org", timeout=3)
        return response.text
    except:
        return "Unavailable"


# ==============================
# Network Status
# ==============================
def get_network_status():
    try:
        requests.get("https://www.google.com", timeout=3)
        return "Connected"
    except:
        return "Disconnected"


# ==============================
# Network Traffic
# ==============================
def get_network_usage():
    counters = psutil.net_io_counters()
    sent = counters.bytes_sent / (1024 * 1024)      # MB
    received = counters.bytes_recv / (1024 * 1024)  # MB
    return round(sent, 2), round(received, 2)