from scapy.all import sniff

def capture_packets(count=50):
    print("[+] Capturing packets...")
    packets = sniff(count=count)
    print(f"[+] Captured {len(packets)} packets")
    return packets

if __name__ == "__main__":
    capture_packets()
