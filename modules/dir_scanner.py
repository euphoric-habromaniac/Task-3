import requests

def scan_directories(url, wordlist_path):
    print(f"\n📁 Scanning directories on {url}...")
    try:
        with open(wordlist_path, "r") as file:
            paths = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"❌ Could not read wordlist: {e}")
        return

    found = False
    for path in paths:
        target = f"{url.rstrip('/')}/{path}"
        try:
            res = requests.get(target)
            if res.status_code == 200:
                print(f"✅ Found: {target}")
                found = True
        except Exception as e:
            print(f"⚠️ Failed to check {target}: {e}")

    if not found:
        print("❌ No directories found from wordlist.")


# Credits: euphoric-habromaniac