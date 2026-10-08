# Python Torrent Downloader with SOCKS5

A lightweight Python script (compatible with **Python 3.12**) built with `libtorrent` designed to download torrent files safely, handle network restrictions, and tunnel traffic through local SOCKS5 proxies (such as v2rayN) using a **TCP-only** configuration to successfully bypass strict firewalls and blocked P2P ports.

## Features

* **Python 3.12 Compatible:** Tested and optimized for modern Python environments.
* **TCP-Only Proxy Tunneling:** Enforces strict TCP routing for trackers and peer handshakes, bypassing UDP blocks and restrictive network firewalls completely.
* **SOCKS5 Proxy Integration:** Seamlessly routes peer connections and HTTP/HTTPS tracker requests through local proxies (e.g., v2rayN).
* **Network Restriction Bypassing:** Dynamically binds to open ports, strips blocked UDP trackers, and injects HTTP tracker fallbacks.
* **Real-time Monitoring:** Tracks progress, active peers, seeders, and connection states cleanly in the console.

## Prerequisites

* Python 3.12 (or compatible 3.x)
* `libtorrent` python package

## Installation & Setup

1. Clone or download this repository.
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r req.txt
   ```

3. Download your torrent file.
4. Replace your file path and anme in ```ti``` variable.

5. Run the code
   ```bash
   python main.py
   ```