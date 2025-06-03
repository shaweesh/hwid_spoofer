import subprocess
import uuid
from utils.registry_tools import write_registry_value, delete_registry_value
from utils.storage import save_original_value, load_original_value

def get_system_uuid():
    try:
        output = subprocess.check_output("wmic csproduct get uuid", shell=True)
        lines = output.decode().split('\n')
        uuid_line = [line.strip() for line in lines if line.strip() and "UUID" not in line]
        return uuid_line[0] if uuid_line else "N/A"
    except:
        return "N/A"

def generate_fake_uuid():
    return str(uuid.uuid4()).upper()

def spoof_uuid():
    real = get_system_uuid()
    save_original_value("system_uuid", real)

    fake_uuid = generate_fake_uuid()
    reg_path = r"HKEY_LOCAL_MACHINE\SOFTWARE\FakeUUID"
    write_registry_value(reg_path, "UUID", fake_uuid)
    print(f"[+] Fake UUID written: {fake_uuid}")

def reset_uuid():
    delete_registry_value(r"HKEY_LOCAL_MACHINE\SOFTWARE\FakeUUID", "UUID")
    print("[+] Fake UUID removed.")
