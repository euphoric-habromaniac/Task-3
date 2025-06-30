import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

SQL_PAYLOADS = ["' OR '1'='1", "'; DROP TABLE users; --"]
XSS_PAYLOADS = ["<script>alert('XSS')</script>", '" onmouseover="alert(1)"']
SQL_ERRORS = ["sql syntax", "mysql_fetch", "unterminated string", "warning", "error"]

def get_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"❌ Error fetching forms: {e}")
        return []

def get_form_details(form):
    details = {"action": form.get("action"), "method": form.get("method", "get").lower(), "inputs": []}
    for input_tag in form.find_all(["input", "textarea"]):
        input_name = input_tag.get("name")
        if not input_name:
            continue
        input_type = input_tag.get("type", "text")
        details["inputs"].append({"name": input_name, "type": input_type})
    return details

def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details["action"])
    data = {}
    for input in form_details["inputs"]:
        if input["type"] in ["text", "search", "textarea"]:
            data[input["name"]] = payload
    try:
        if form_details["method"] == "post":
            return requests.post(target_url, data=data)
        return requests.get(target_url, params=data)
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None

def test_sql_injection(url):
    print("\n🛡️  Testing for SQL Injection...")
    forms = get_forms(url)
    found = False
    for i, form in enumerate(forms, start=1):
        details = get_form_details(form)
        for payload in SQL_PAYLOADS:
            response = submit_form(details, url, payload)
            if not response:
                continue
            for error in SQL_ERRORS:
                if error in response.text.lower():
                    print(f"[!] Possible SQL Injection in form #{i} with payload: {payload}")
                    found = True
                    break
    if not found:
        print("✅ No SQL Injection detected.")

def test_xss(url):
    print("\n🛡️  Testing for Cross-Site Scripting (XSS)...")
    forms = get_forms(url)
    found = False
    for i, form in enumerate(forms, start=1):
        details = get_form_details(form)
        for payload in XSS_PAYLOADS:
            response = submit_form(details, url, payload)
            if not response:
                continue
            if payload in response.text:
                print(f"[!] Possible XSS vulnerability in form #{i} with payload: {payload}")
                found = True
                break
    if not found:
        print("✅ No XSS vulnerabilities detected.")

def scan_website(url):
    print("\n🔎 Scanning website for vulnerabilities...")
    test_sql_injection(url)
    test_xss(url)
    print("\n✅ Scan complete.")

# Credits: euphoric-habromaniac