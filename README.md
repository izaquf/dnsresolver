# Dns resolver

#### **dnsresolver is a tool developed in Python3 for scanning and enumerating subdomains via DNS, using wordlists for automated discovery**
---

## 🚀 Installation

**To start using dnsresolver.py**

cd dnsresolver

---

**dependencies**

```bash
        pip install dnspython

```

---

<pre>
<b>
Dns Resolver

Commands:
    -d      Target domain
    -s      Single subdomain
    -t      DNS record type (A, AAAA, MX, TXT, NS, CNAME)
    -w      Wordlist file containing subdomains
    -v      Verbose mode (optional)

Examples:
    python3 dnsresolver.py -d google.com -t MX
    python3 dnsresolver.py -d google.com -t NS -v
    python3 dnsresolver.py -d google.com -t TXT
    python3 dnsresolver.py -d google.com -t CNAME -v
    python3 dnsresolver.py -s www -d google.com -t A
    python3 dnsresolver.py -s www -d google.com -t AAAA -v
    python3 dnsresolver.py -w subdomains.txt -d google.com -t A
    python3 dnsresolver.py -w subdomains.txt -d google.com -t AAAA -v
</b>
</pre>