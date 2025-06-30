import os
from modules import port_scanner, brute_forcer, web_vuln_scanner, dir_scanner, hash_cracker

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print("="*60)
    print("🛠️  PYTHON PENETRATION TESTING TOOLKIT 🛠️")
    print("="*60)
    print("1. 🔍 Port Scanner")
    print("2. 🔑 Brute Forcer (Login)")
    print("3. 🌐 Web Vulnerability Scanner")
    print("4. 📁 Directory Scanner")
    print("5. 🔓 Hash Cracker")
    print("0. ❌ Exit")
    print("="*60)

def main():
    while True:
        clear_screen()
        print_menu()
        choice = input("📥 Enter your choice: ").strip()

        match choice:
            case '1':
                target_ip = input("🔗 Enter target IP address: ").strip()
                try:
                    port_scanner.scan_ports(target_ip)
                except Exception as e:
                    print(f"❌ Error: {e}")

            case '2':
                url = input("🌐 Enter login form URL: ").strip()
                usernames = input("👤 Enter comma-separated usernames: ").split(",")
                passwords = input("🔐 Enter comma-separated passwords: ").split(",")
                try:
                    brute_forcer.brute_force_login(url, [u.strip() for u in usernames], [p.strip() for p in passwords])
                except Exception as e:
                    print(f"❌ Error: {e}")

            case '3':
                url = input("🌐 Enter target website URL: ").strip()
                try:
                    web_vuln_scanner.scan_website(url)
                except Exception as e:
                    print(f"❌ Error: {e}")

            case '4':
                url = input("🌐 Enter website URL to scan: ").strip()
                wordlist = input("📄 Enter path to wordlist file: ").strip()
                if not os.path.isfile(wordlist):
                    print("❌ Invalid wordlist path.")
                else:
                    try:
                        dir_scanner.scan_directories(url, wordlist)
                    except Exception as e:
                        print(f"❌ Error: {e}")

            case '5':
                hash_value = input("🔢 Enter hash to crack: ").strip()
                hash_type = input("🔣 Enter hash type (md5/sha1): ").strip().lower()
                wordlist = input("📄 Enter path to wordlist file: ").strip()
                if not os.path.isfile(wordlist):
                    print("❌ Invalid wordlist path.")
                else:
                    try:
                        hash_cracker.crack_hash(hash_value, hash_type, wordlist)
                    except Exception as e:
                        print(f"❌ Error: {e}")

            case '0':
                print("👋 Exiting toolkit. Goodbye!")
                break

            case _:
                print("⚠️ Invalid choice. Please try again.")

        input("\n🔁 Press Enter to return to menu...")

if __name__ == "__main__":
    main()


# Credits: euphoric-habromaniac