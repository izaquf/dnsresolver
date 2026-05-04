# Dns resolver

#### **O dnsresolver é uma ferramenta desenvolvida em Python 3 para varredura e enumeração de subdomínios via DNS, utilizando listas de palavras (wordlists) para descoberta automatizada.**
---

## 🚀 Instalação

**Para começar a usar o dnsresolver.py**

cd dnsresolver

---

**dependências**

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