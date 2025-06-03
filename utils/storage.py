import json
import os

STORAGE_FILE = "original_values.json"

def save_original_value(key, value):
    data = {}
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            data = json.load(f)

    if key not in data:
        data[key] = value
        with open(STORAGE_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print(f"[+] Saved original value for {key}.")
    else:
        print(f"[=] Original value for {key} already stored, skipping.")


def load_original_value(key):
    if not os.path.exists(STORAGE_FILE):
        return None
    with open(STORAGE_FILE, "r") as f:
        data = json.load(f)
    return data.get(key, None)

def show_all_original_values():
    print("\n=== Stored Original HWID Values ===")
    if not os.path.exists(STORAGE_FILE):
        print("[-] No original values stored yet.")
        return

    with open(STORAGE_FILE, "r") as f:
        data = json.load(f)

    if not data:
        print("[-] Storage file is empty.")
        return

    for key, value in data.items():
        print(f"{key}: {value}")

