import subprocess

def set_ip_address(interface, ip_address, netmask):
    if platform.system() == "Windows":
        command = f"netsh interface ip set address name={interface} static {ip_address} {netmask}"
    else:
        command = f"sudo ifconfig {interface} {ip_address} netmask {netmask}"

    subprocess.run(command, shell=True)

def get_ip_address(interface):
    if platform.system() == "Windows":
        command = f"ipconfig /all"
    else:
        command = f"ifconfig {interface}"

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
