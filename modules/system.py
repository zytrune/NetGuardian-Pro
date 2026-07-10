"""
NetGuardian Pro - System Monitoring Module
Handles system statistics retrieval.
"""

import psutil
import platform
import time
from datetime import timedelta


# ==============================
# CPU Usage
# ==============================
def get_cpu_usage():
    return psutil.cpu_percent(interval=None)


# ==============================
# RAM Usage
# ==============================
def get_ram_usage():
    memory = psutil.virtual_memory()
    return memory.percent


# ==============================
# Disk Usage
# ==============================
def get_disk_usage():
    disk = psutil.disk_usage("C:/")  # Windows main drive
    return disk.percent


# ==============================
# System Uptime
# ==============================
def get_system_uptime():
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    return str(timedelta(seconds=int(uptime_seconds)))


# ==============================
# Basic System Info
# ==============================
def get_system_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Processor": platform.processor(),
    }