import requests
import re

def scan_emails(domain):
    try:
        url = f"https://{domain}"
        response = requests.get(url, timeout=5)

        # Regex pattern for emails
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"

        emails = re.findall(email_pattern, response.text)

        unique_emails = list(set(emails))

        return {
            "count": len(unique_emails),
            "emails": unique_emails
        }

    except Exception as e:
        return {
            "count": 0,
            "emails": [],
            "error": str(e)
        }
