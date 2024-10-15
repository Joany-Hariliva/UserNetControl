import psutil
import socket

def get_system_info():
    info = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "ip_address": socket.gethostbyname(socket.gethostname())
    }
    return info
