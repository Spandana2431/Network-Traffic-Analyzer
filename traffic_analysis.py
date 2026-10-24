from scapy.layers.inet import IP, TCP, UDP
from collections import Counter

def analyze_packets(packets):
    ip_counter = Counter()
    protocol_counter = Counter()

    for pkt in packets:
        if IP in pkt:
            src = pkt[IP].src
            ip_counter[src] += 1

            if TCP in pkt:
                protocol_counter['TCP'] += 1
            elif UDP in pkt:
                protocol_counter['UDP'] += 1
            else:
                protocol_counter['OTHER'] += 1

    return ip_counter, protocol_counter
