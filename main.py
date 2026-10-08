import time
import libtorrent as lt

ses = lt.session({
    'listen_interfaces': '0.0.0.0:0',
    
    # --- PROXY CONFIGURATION ---
    'proxy_type': 2,                 # 2 = SOCKS5 Proxy
    'proxy_hostname': '127.0.0.1',   # Your local v2rayN SOCKS5 IP
    'proxy_port': 10808,            # Your local v2rayN SOCKS5 port
    'proxy_peer_connections': True,
    'proxy_tracker_connections': True,
    # ---------------------------

    # Disable UDP-dependent features since proxying uTP fails
    'enable_dht': False,
    'enable_lsd': False,
    'enable_upnp': False,
    'enable_natpmp': False,
    
    # Force TCP preference over uTP
    'enable_outgoing_utp': False,
    'enable_incoming_utp': False,
    
    # Protocol Encryption & Safety
    'out_enc_policy': 1,
    'in_enc_policy': 1,
    'allowed_enc_level': 3,
    'validate_https_trackers': False,
    
    'alert_mask': (lt.alert_category.error | lt.alert_category.status
                   | lt.alert_category.tracker | lt.alert_category.connect 
                   | lt.alert_category.peer),
})

ti = lt.torrent_info("YOUR-TORRENT-FILE.torrent")
atp = lt.add_torrent_params()
atp.ti = ti
atp.save_path = "./downloads"
h = ses.add_torrent(atp)

# Keep the HTTP tracker fallback list
current_trackers = h.trackers()
safe_trackers = [t for t in current_trackers if not t['url'].startswith('udp://')]

http_fallbacks = [
    "http://tracker.openbittorrent.com:80/announce",
    "http://opentrackr.org:1337/announce",
    "http://tracker.internetwarriors.net:1337/announce"
]

for url in http_fallbacks:
    safe_trackers.append({'url': url, 'tier': 1})

h.replace_trackers(safe_trackers)
h.scrape_tracker()

interesting = (lt.tracker_reply_alert, lt.scrape_reply_alert, lt.scrape_failed_alert,
               lt.peer_connect_alert, lt.peer_disconnected_alert,
               lt.peer_error_alert, lt.listen_failed_alert)

try:
    while not h.status().is_seeding:
        for a in ses.pop_alerts():
            msg = a.message()
            if "127.0.0.1" in msg or "::1" in msg or "No such host" in msg:
                continue
            if isinstance(a, interesting):
                print(f"[ALERT] {msg}")
        s = h.status()
        print(f"{s.state} | {s.progress*100:.1f}% | connected {s.num_peers} "
              f"| seeds {s.num_seeds} | list_peers {s.list_peers} "
              f"| candidates {s.connect_candidates}")
        time.sleep(3)
except KeyboardInterrupt:
    pass