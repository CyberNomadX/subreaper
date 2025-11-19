import aiohttp
import asyncio

async def fetch_certspotter(domain):
    url = f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names"
    subdomains = set()

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    print(f"[!] CertSpotter error: HTTP {response.status}")
                    return subdomains

                data = await response.json()
                for cert in data:
                    for name in cert.get("dns_names", []):
                        if domain in name:
                            subdomains.add(name.lower())
    except Exception as e:
        print(f"[!] CertSpotter exception: {e}")

    return subdomains
