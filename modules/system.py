import psutil
import platform
import socket

def get_system_info():
    return {
        "Computer Name": socket.gethostname(),
        "Operating System": platform.system() + " " + platform.release(),
        "Processor": platform.processor(),
        "CPU Usage": f"{psutil.cpu_percent()}%",
        "RAM Usage": f"{psutil.virtual_memory().percent}%"
    }