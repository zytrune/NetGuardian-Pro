"""
NetGuardian Pro - Security Intelligence Engine
Generates system risk score and recommendations.
"""

from modules.system import get_cpu_usage, get_ram_usage, get_disk_usage
from modules.network import get_network_status
from modules.scanner import COMMON_PORTS
from modules.state import last_open_ports

DANGEROUS_PORTS = {
    23: "Telnet",
    21: "FTP",
    3389: "RDP",
    445: "SMB"
}


def calculate_security_score():
    score = 100
    recommendations = []

    cpu = get_cpu_usage()
    ram = get_ram_usage()
    disk = get_disk_usage()
    network_status = get_network_status()

    # High CPU
    if cpu > 85:
        score -= 10
        recommendations.append("High CPU usage detected. Investigate running processes.")

    # High RAM
    if ram > 90:
        score -= 10
        recommendations.append("High RAM usage detected. Possible memory pressure.")

    # Low Disk
    if disk > 90:
        score -= 15
        recommendations.append("Disk nearly full. Run system cleanup.")

    # Network disconnected
    if network_status == "Disconnected":
        score -= 5
        recommendations.append("System currently offline.")

    # Dangerous ports open
    for port in last_open_ports:
        if port in DANGEROUS_PORTS:
            score -= 15
            recommendations.append(
                f"Potentially insecure port open: {port} ({DANGEROUS_PORTS[port]})"

                 
                )

    if score < 0:
        score = 0

    # Determine risk level
    if score >= 80:
        level = "Low"
    elif score >= 50:
        level = "Moderate"
    else:
        level = "High"

    return {
        "score": score,
        "level": level,
        "recommendations": recommendations
    }