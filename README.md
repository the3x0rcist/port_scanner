# Port Scanner

A **lightweight, powerful TCP Port Scanner** built with Python's `socket` module. Perfect for network diagnostics, security assessments, and understanding your local or remote host’s exposed services.

> ⚠️ **Disclaimer:** Use responsibly. Unauthorized scanning of networks is illegal in many jurisdictions.

---

## Overview

This simple yet effective tool performs a **TCP handshake** to check whether a port on a target IP address is **open** or **closed**. It’s an excellent utility for:

-  Security Auditing  
- 🛠 Network Troubleshooting  
-  Learning about TCP/IP and Port Communication  

---

##  Features

-  Scans any IPv4 address  
-  Customizable port ranges (e.g., `1-1000`, `20-80`, etc.)  
-  Clear and informative output  
-  Lightweight and dependency-free  
-  Easily customizable Python script  

---

## Usage

### Prerequisites:
- Python 3.x

### Run the scanner:
```bash
python3 portscanner.py <target-ip> <port-range>
