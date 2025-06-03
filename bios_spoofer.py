import subprocess
import random
import string
from utils.registry_tools import write_registry_value, delete_registry_value
from utils.storage import save_original_value, load_original_value

def get_bios_serial():
    try:
        output = subprocess.check_output("wmic bios get serialnumber", shell=True)
        lines = output.decode().split('\n')
        serial_line = [line.strip() for line in lines if line.strip() and "SerialNumber" not in line]
        return serial_line[0] if serial_line else "N/A"
    except:
        return "N/A"

def generate_fake_serial(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def spoof_bios_serial():
    real = get_bios_serial()
    save_original_value("bios_serial", real)

    fake_serial = generate_fake_serial()
    reg_path = r"HKEY_LOCAL_MACHINE\SOFTWARE\FakeBIOS"
    write_registry_value(reg_path, "SerialNumber", fake_serial)
    print(f"[+] Fake BIOS Serial written: {fake_serial}")

def reset_bios_serial():
    delete_registry_value(r"HKEY_LOCAL_MACHINE\SOFTWARE\FakeBIOS", "SerialNumber")
    print("[+] Fake BIOS Serial removed.")
