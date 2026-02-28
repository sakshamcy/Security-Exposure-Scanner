import socket

def scan_ports(domain):
    common_ports = [21, 22, 80, 443, 3306, 8080]
    open_ports = []

    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((domain, port))

            if result == 0:
                open_ports.append(port)

            sock.close()

        except:
            pass

    return open_ports
