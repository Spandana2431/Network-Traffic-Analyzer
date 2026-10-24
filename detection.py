def detect_suspicious(ip_counter, threshold=20):
    suspicious_ips = []

    for ip, count in ip_counter.items():
        if count > threshold:
            suspicious_ips.append((ip, count))

    return suspicious_ips
