"""
NetGuardian Pro - Reports Module
Handles report generation and saving.
"""

import os
from datetime import datetime

from modules.system import (
    get_cpu_usage,
    get_ram_usage,
    get_disk_usage,
    get_system_uptime,
    get_system_info,
)

from modules.network import (
    get_local_ip,
    get_public_ip,
    get_network_status,
    get_network_usage,
)


# ==============================
# Generate Full Report
# ==============================
def generate_report():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    system_info = get_system_info()
    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()
    uptime = get_system_uptime()

    local_ip = get_local_ip()
    public_ip = get_public_ip()
    status = get_network_status()
    sent, received = get_network_usage()

    report = f"""
================================================
   NetGuardian Pro - System Report
================================================
   Generated: {timestamp}
================================================

SYSTEM INFORMATION
--------------------------------------------------
   OS:            {system_info['OS']}
   OS Version:    {system_info['OS Version']}
   Processor:     {system_info['Processor']}
   Uptime:        {uptime}

PERFORMANCE
--------------------------------------------------
   CPU Usage:     {cpu}%
   RAM Usage:     {ram}%
   Disk Usage:    {disk}%

NETWORK
--------------------------------------------------
   Local IP:      {local_ip}
   Public IP:     {public_ip}
   Status:        {status}
   Data Sent:     {sent} MB
   Data Received: {received} MB

================================================
   End of Report
================================================
"""
    return report


# ==============================
# Save Report to File
# ==============================
def save_report(report):
    reports_dir = "reports"

    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"report_{timestamp}.txt"
    filepath = os.path.join(reports_dir, filename)

    with open(filepath, "w") as file:
        file.write(report)

    return filepath