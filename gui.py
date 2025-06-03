import tkinter as tk
from tkinter import messagebox, scrolledtext
import mac_spoofer
import volume_spoofer
import bios_spoofer
import uuid_spoofer
from utils.storage import show_all_original_values
from tkinter import simpledialog


# إعداد النافذة
root = tk.Tk()
root.title("HWID Spoofer GUI")
root.geometry("520x520")
root.configure(bg="#1e1e1e")  # خلفية داكنة

# عنوان
title = tk.Label(root, text="🛠️ HWID Spoofer", font=("Helvetica", 18, "bold"), bg="#1e1e1e", fg="#00ffff")
title.pack(pady=10)

# منطقة الإخراج
output = scrolledtext.ScrolledText(root, width=62, height=14, bg="#2b2b2b", fg="white")
output.pack(pady=10)

def log(msg):
    output.insert(tk.END, msg + "\n")
    output.see(tk.END)

# دوال الوظائف
def spoof_mac():
    choice = messagebox.askquestion("MAC Spoof", "Do you want to enter a custom MAC address?")
    
    if choice == "yes":
        user_mac = simpledialog.askstring("Enter MAC", "Enter MAC address (e.g., 001122334455):")
        if user_mac and len(user_mac) == 12:
            adapter = mac_spoofer.get_network_adapter_guid()
            if mac_spoofer.spoof_mac(adapter, user_mac):
                log(f"[+] MAC spoofed to {user_mac}")
            else:
                log("[-] Failed to spoof MAC")
        else:
            log("[-] Invalid MAC entered or cancelled.")
    else:
        adapter = mac_spoofer.get_network_adapter_guid()
        new_mac = mac_spoofer.generate_random_mac()
        if mac_spoofer.spoof_mac(adapter, new_mac):
            log(f"[+] MAC spoofed to {new_mac}")
        else:
            log("[-] Failed to spoof MAC")

def spoof_volume():
    choice = messagebox.askquestion("Volume Serial Spoof", "Do you want to enter a custom Volume Serial?")
    
    if choice == "yes":
        user_id = simpledialog.askstring("Enter Volume Serial", "Format: ABCD-1234 (8 hex digits)")
        if user_id and len(user_id) == 9 and "-" in user_id:
            result = volume_spoofer.spoof_volume_id(volume_id=user_id)
            if result:
                log(f"[+] Volume Serial spoofed to {user_id}")
            else:
                log("[-] Failed to spoof Volume Serial")
        else:
            log("[-] Invalid Volume Serial format.")
    else:
        result = volume_spoofer.spoof_volume_id()
        if result:
            log(f"[+] Volume Serial spoofed to {result}")
        else:
            log("[-] Failed to spoof Volume Serial")

def spoof_bios():
    bios_spoofer.spoof_bios_serial()
    log("[+] BIOS Serial spoofed (mock)")

def spoof_uuid():
    uuid_spoofer.spoof_uuid()
    log("[+] UUID spoofed (mock)")

def reset_all():
    mac_spoofer.reset_mac()
    volume_spoofer.reset_volume_id()
    bios_spoofer.reset_bios_serial()
    uuid_spoofer.reset_uuid()
    log("[*] All spoofed values reset (where possible)")

def show_originals():
    log("[=] Stored Original HWID Values:")
    show_all_original_values()

# أزرار مع ستايل
def styled_button(text, command, color):
    return tk.Button(root, text=text, width=30, command=command, bg=color, fg="white", font=("Arial", 10, "bold"))

styled_button("🔄 Spoof MAC Address", spoof_mac, "#007acc").pack(pady=3)
styled_button("🔄 Spoof Volume Serial", spoof_volume, "#007acc").pack(pady=3)
styled_button("🔄 Spoof BIOS Serial (Mock)", spoof_bios, "#007acc").pack(pady=3)
styled_button("🔄 Spoof UUID (Mock)", spoof_uuid, "#007acc").pack(pady=3)
styled_button("🧹 Reset All Spoofed Values", reset_all, "#cc3300").pack(pady=6)
styled_button("📂 Show Original HWID Values", show_originals, "#ffaa00").pack(pady=2)

# تشغيل الواجهة
root.mainloop()
