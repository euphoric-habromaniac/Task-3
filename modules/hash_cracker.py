import hashlib

def crack_hash(target_hash, hash_type, wordlist_path):
    print("\n🔓 Attempting to crack hash...")
    try:
        with open(wordlist_path, "r") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"❌ Could not read wordlist: {e}")
        return

    for pwd in passwords:
        if hash_type == "md5":
            hashed = hashlib.md5(pwd.encode()).hexdigest()
        elif hash_type == "sha1":
            hashed = hashlib.sha1(pwd.encode()).hexdigest()
        else:
            print("❌ Unsupported hash type. Use 'md5' or 'sha1'.")
            return

        if hashed == target_hash:
            print(f"✅ Hash cracked! Password: {pwd}")
            return

    print("❌ Failed to crack the hash with provided wordlist.")

# Credits: euphoric-habromaniac