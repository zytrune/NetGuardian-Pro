"""
NetGuardian Pro - Security Scanner Module
Handles controlled multi-threaded port scanning.
"""
from modules.state import last_open_ports
import socket
import threading

# Known common services
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt",
}

print_lock = threading.Lock()


def scan_port(target, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        result = sock.connect_ex((target, port))

        if result == 0:
            with print_lock:
                service = COMMON_PORTS.get(port, "Unknown")
                open_ports.append((port, service))

        sock.close()
    except Exception:
        pass


def run_port_scan(target, start_port=1, end_port=1024, update_progress_callback=None):
    try:
        target_ip = socket.gethostbyname(target)
    except Exception:
        return f"Scan failed: Cannot resolve target '{target}'."

    if start_port < 1 or end_port > 65535 or start_port >= end_port:
        return "Invalid port range. Ports must be between 1 and 65535."

    open_ports = []
    total_ports = end_port - start_port + 1
    scanned = 0
    lock = threading.Lock()

    def scan_range(port):
        nonlocal scanned
        scan_port(target_ip, port, open_ports)

        with lock:
            scanned += 1
            if update_progress_callback:
                progress = int((scanned / total_ports) * 100)
                update_progress_callback(progress)

    threads = []
    max_threads = 100

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_range, args=(port,))
        threads.append(t)
        t.start()

        if len(threads) >= max_threads:
            for th in threads:
                th.join()
            threads.clear()

    for th in threads:
        th.join()
    last_open_ports.clear()
    for port, _ in open_ports:
        last_open_ports.append(port)





    report = f"\nScan Results for: {target} ({target_ip})\n"
    report += "=" * 60 + "\n"

    if open_ports:
        report += f"{'PORT':<10}{'STATUS':<10}{'SERVICE':<20}\n"
        report += "-" * 60 + "\n"
        for port, service in sorted(open_ports):
            report += f"{port:<10}{'OPEN':<10}{service:<20}\n"
    else:
        report += "No open ports detected in selected range.\n"

    report += "=" * 60 + "\n"
    return report