# Network Traffic Analysis

A lightweight Python tool for capturing, analyzing, and reporting on local network traffic.

## Features

- **Packet Capture** – Captures network packets from the local interface
- **Traffic Analysis** – Parses and summarizes captured traffic (protocols, top talkers, etc.)
- **Detection** – Flags suspicious or anomalous traffic patterns
- **Report Generation** – Produces an HTML report of the analysis results

## Project Structure

```
Network-Traffic-Analysis/
├── main.py # Entry point
├── packet_capture.py # Packet capture module
├── traffic_analysis.py # Traffic parsing & analysis
├── detection.py # Anomaly / threat detection
├── reportGenerator.py # HTML report generator
├── README.md
└── images/ # Screenshots / assets
```


## Getting Started

### Prerequisites

- Python 3.8+
- `scapy` (for packet capture)
- Administrative / root privileges (required to capture packets)

### Installation

```bash
pip install scapy

Usage
python main.py

⚠️ Note: Packet capture requires elevated privileges. Run your terminal as Administrator (Windows) or with sudo (Linux).
