#!/usr/bin/env python3
"""Rebuilds ru-bypass.json (an Incy routing profile) from the community-curated
Re-filter-lists domain/IP lists. Source project:
https://github.com/1andrevich/Re-filter-lists
"""
import json
import time
import urllib.request

DOMAINS_URL = "https://raw.githubusercontent.com/1andrevich/Re-filter-lists/main/community.lst"
IPS_URL = "https://raw.githubusercontent.com/1andrevich/Re-filter-lists/main/community_ips.lst"


def fetch_lines(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        text = r.read().decode()
    return sorted({line.strip() for line in text.splitlines() if line.strip()})


def main():
    domains = fetch_lines(DOMAINS_URL)
    ips = fetch_lines(IPS_URL)

    profile = {
        "Name": "RU Bypass",
        "GlobalProxy": "false",
        "RemoteDNSType": "DoH",
        "RemoteDNSDomain": "https://cloudflare-dns.com/dns-query",
        "DomesticDNSType": "DoU",
        "DomesticDNSIP": "77.88.8.8",
        "ProxySites": domains,
        "ProxyIp": ips,
        "DirectSites": [],
        "DirectIp": [],
        "BlockSites": [],
        "BlockIp": [],
        "DomainStrategy": "AsIs",
        "FakeDNS": "false",
        "LastUpdated": int(time.time()),
    }

    with open("ru-bypass.json", "w") as f:
        json.dump(profile, f, separators=(",", ":"))

    print(f"domains={len(domains)} ips={len(ips)}")


if __name__ == "__main__":
    main()
