import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="SubReaper - Passive Subdomain Enumeration Tool"
    )

    parser.add_argument(
        "--domain",
        "-d",
        help="Target domain to enumerate subdomains for",
        required=True
    )

    return parser.parse_args()
