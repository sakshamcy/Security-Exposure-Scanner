def calculate_risk(open_ports, ssl_status):
    high_risk_ports = [21, 23, 3306]
    risk_score = 0

    for port in open_ports:
        if port in high_risk_ports:
            risk_score += 3

    if len(open_ports) > 3:
        risk_score += 2

    if "Expired" in ssl_status:
        risk_score += 2

    # Determine level
    if risk_score >= 5:
        return "High"
    elif risk_score >= 3:
        return "Medium"
    else:
        return "Low"
