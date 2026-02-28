import requests
import time

def check_email_breaches(email):
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"

    headers = {
        "User-Agent": "attack-surface-monitor"
    }

    try:
        response = requests.get(url, headers=headers)

        # Add delay to avoid rate blocking
        time.sleep(1.5)

        if response.status_code == 200:
            data = response.json()

            if "Breaches" in data and data["Breaches"]:
                return [breach["Name"] for breach in data["Breaches"]]

        return []

    except Exception as e:
        print("Breach check error:", e)
        return []
