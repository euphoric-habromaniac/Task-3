import socket
from tqdm import tqdm

def scan_ports(ip):
    print(f"\n🔍 Scanning ports on {ip}...")
    open_ports = []
    for port in tqdm(range(1, 1025), desc="⚡ Ports", unit="port"):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except:
            continue

    if open_ports:
        print("\n✅ Open ports found:")
        for port in open_ports:
            print(f"  - Port {port}")
    else:
        print("❌ No open ports found.")

# Credits: euphoric-habromaniac