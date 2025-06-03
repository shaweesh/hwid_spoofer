import subprocess
import random
import re
from utils.registry_tools import write_registry_value, delete_registry_value
from utils.storage import save_original_value, load_original_value

def get_network_adapter_guid():
    output = subprocess.check_output("getmac /v /fo list", shell=True).decode()
    matches = re.findall(r'Connection Name: (.+)\s+Network Adapter: (.+)', output)
    if matches:
        name, adapter = matches[0]
        return name
    return None

def get_mac_address():
    import uuid
    mac = hex(uuid.getnode()).replace('0x', '').upper()
    return ':'.join(mac[i:i+2] for i in range(0, 12, 2))

def generate_random_mac():
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    mac[0] = mac[0] & 0b11111110
    return ''.join(f'{x:02X}' for x in mac)

def spoof_mac(adapter_name, new_mac):
    original_mac = get_mac_address()
    save_original_value("mac_address", original_mac)

    key_path = fr"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\"

    found = False
    for i in range(0, 20):
        path = key_path + f"{i:04d}"
        try:
            name = subprocess.check_output(
                f'reg query "{path}" /v DriverDesc', shell=True
            ).decode()
            if adapter_name in name:
                subprocess.run(
                    f'reg add "{path}" /v NetworkAddress /d {new_mac} /f',
                    shell=True
                )
                found = True
                break
        except:
            continue
    return found

def reset_mac():
    print("[*] Resetting MAC Address spoof...")
    adapter = get_network_adapter_guid()
    original_mac = load_original_value("mac_address")
    if adapter and original_mac:
        print(f"[+] Restoring original MAC: {original_mac}")
        spoof_mac(adapter, original_mac.replace(":", ""))
    else:
        print("[-] Could not restore MAC. Value not found or adapter missing.")
