import subprocess
import random
import os
from utils.storage import save_original_value, load_original_value

def get_current_volume_serial():
    import ctypes
    serial_number = ctypes.c_ulong()
    ctypes.windll.kernel32.GetVolumeInformationW(
        "C:\\", None, 0, ctypes.byref(serial_number), None, None, None, 0)
    return format(serial_number.value, '04X')

def generate_random_volume_id():
    part1 = ''.join(random.choices('0123456789ABCDEF', k=4))
    part2 = ''.join(random.choices('0123456789ABCDEF', k=4))
    return f"{part1}-{part2}"

def spoof_volume_id(drive_letter='C', volume_id=None):
    tool = 'volumeid.exe'
    if not os.path.exists(tool):
        print(f"[-] {tool} not found.")
        return False

    if not volume_id:
        volume_id = generate_random_volume_id()

    current_id = get_current_volume_serial()
    save_original_value("volume_serial", current_id)

    try:
        subprocess.run([tool, f"{drive_letter}:", volume_id], check=True)
        return volume_id
    except subprocess.CalledProcessError:
        return False

def reset_volume_id():
    original_id = load_original_value("volume_serial")
    if not original_id:
        print("[-] Original Volume Serial not found.")
        return
    print(f"[!] Please run: volumeid.exe C: {original_id}")
    print("[!] Admin rights and reboot may be required.")
