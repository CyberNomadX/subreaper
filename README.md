# SubReaper

**SubReaper** is a Python-based subdomain enumeration tool focused on passive discovery. It queries public data sources to uncover subdomains associated with a target domain.

This project is part of my public cybersecurity portfolio, showcasing Python scripting, API integration, and modular tool development.

## 🚧 Intended Features

> These features are planned and will be implemented as development progresses.

- [ ] Passive subdomain enumeration from public APIs (e.g., crt.sh, CertSpotter, ThreatCrowd)
- [ ] Modular design with pluggable data sources
- [ ] DNS resolution to verify live subdomains
- [ ] Brute-force subdomain discovery using wordlists
- [ ] Async or multi-threaded execution for speed
- [ ] Output to console and file (`.txt`, `.json`)
- [ ] CLI support for single domain or domain list input
- [ ] Clean and well-documented codebase
- [ ] Tests and validation for each module


## 📦 Installation

SubReaper requires **Python 3.8+** and `pip`.

1. Clone the repository:

```bash
git clone https://github.com/yourusername/SubReaper.git
cd SubReaper
```

2. (Optional) Create a virtual enviroment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Usage instructions will be added once core functionality is implemented.

Stay tuned as the project develops.

## 🧱 Project Structure (Planned)
```
SubReaper/
├── main.py # Entry point of the tool
├── input_handler.py # CLI argument parsing and input validation
├── output.py # Handles formatting and writing results
├── resolver.py # Optional: resolves DNS for discovered subdomains
├── bruteforcer.py # Optional: brute-force discovery using wordlists
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── sources/ # Passive data source integrations
│ ├── init.py
│ ├── certspotter.py
│ ├── crtsh.py
│ └── threatcrowd.py
├── wordlists/ # Subdomain wordlists (for brute-force)
│ └── common.txt
└── utils/ # (Optional) shared utilities/helpers
└── logger.py
```
> Note: This layout is subject to change as features are added.
