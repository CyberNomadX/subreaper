#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(
        description="SubReaper - Passive Subdomain Enumeration Tool"
    )
    parser.add_argument(
        "--domain",
        "-d",
        help="Target domain to enumerate subdomains for",
        required=True
    )

    args = parser.parse_args()
    domain = args.domain

    print(f"[+] Starting passive subdomain enumeration for: {domain}")
    print("[*] This is a placeholder – modules will be connected soon.")

if __name__ == "__main__":
    main()
