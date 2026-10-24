from packet_capture import capture_packets
from traffic_analysis import analyze_packets
from detection import detect_suspicious
from report_generator import generate_report

def main():
    packets = capture_packets(100)

    ip_data, protocol_data = analyze_packets(packets)

    anomalous_ips = detect_suspicious(ip_data)

    print("\n[+] IP Summary->", ip_data)
    print("[+] Protocol Summary->", protocol_data)
    print("[+] Anomalous IPs->", anomalous_ips)

    generate_report(ip_data, protocol_data, anomalous_ips)

if __name__ == "__main__":
    main()
