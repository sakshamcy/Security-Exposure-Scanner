import dns.resolver

def find_subdomains(domain):
    subdomains = ["www", "mail", "dev", "test", "admin"]
    found = []

    for sub in subdomains:
        try:
            dns.resolver.resolve(f"{sub}.{domain}", "A")
            found.append(f"{sub}.{domain}")
        except:
            pass

    return found
