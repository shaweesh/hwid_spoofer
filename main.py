import sys

def menu():
    print("\n=== HWID Spoofer CLI ===")
    print("1) Spoof MAC Address")
    print("2) Spoof Volume Serial")
    print("3) Spoof BIOS Serial (Mock)")
    print("4) Spoof UUID (Mock)")
    print("5) Reset Spoofed Values")
    print("6) Exit")
    print("7) Show Original HWID Values")



def main():
    while True:
        menu()
        choice = input(">> Choose an option: ").strip()

        if choice == '1':
            import mac_spoofer
        elif choice == '2':
            import volume_spoofer
        elif choice == '3':
            import bios_spoofer
        elif choice == '4':
            import uuid_spoofer
        elif choice == '5':
            import mac_spoofer
            import volume_spoofer
            import bios_spoofer
            import uuid_spoofer
            mac_spoofer.reset_mac()
            volume_spoofer.reset_volume_id()
            bios_spoofer.reset_bios_serial()
            uuid_spoofer.reset_uuid()
        elif choice == '6':
            print("Exiting.")
            sys.exit()
            elif choice == '7':
                from utils.storage import show_all_original_values
                show_all_original_values()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
