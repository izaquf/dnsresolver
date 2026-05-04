"""
	@uthor izaquf
	Python3
"""

import os
import sys
import argparse
import dns.resolver

# pip install dnspython
resolver = dns.resolver.Resolver()

def dnsIPv(subdomain, target, type, verbose=False):
	try:
		result = resolver.resolve(f"{subdomain}.{target}", ("%s"%(type)))
		for line in result:
			print(f"{subdomain} -> {line}")

	except dns.resolver.NXDOMAIN:
		if verbose:
			if type == "A" or type == "a":
				print(f"{subdomain} -> Record A not found")
			else:
				print(f"{subdomain} -> Record AAAA not found")
		else:
			# Doesn't appear on the screen
			pass

def dnsOthers(target, type, verbose=False):
	try:
		result = resolver.resolve(target, type)
		print(f"Record {type}")
		for data in result:
			print(data.to_text())
	except dns.resolver.NoAnswer:
		print(f"The domain {target} doesn't have any records of type {type}")


def main():
	parser = argparse.ArgumentParser(
		description="Dns resolver",
		epilog="Example: python script.py -d google.com -t A -s www -v"
	)

	parser.add_argument("-d", "--domain", required=True, help="Target domain")
	parser.add_argument(
		"-t", "--type",
		required=True,
		choices=["A", "AAAA", "MX", "TXT", "NS", "CNAME"],
		help="DNS record type"
	)
	parser.add_argument("-s", "--subdomain", help="Single subdomain")
	parser.add_argument("-w", "--wordlist", help="File with subdomains")
	parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")

	args = parser.parse_args()

	if args.subdomain:
		dnsIPv(args.subdomain, args.domain, args.type, args.verbose)

	elif args.wordlist:
		try:
			with open(args.wordlist, "r") as file:
				for line in file:
					l = line.strip()
					if l: # Avoid empty lines
						dnsIPv(l, args.domain, args.type, args.verbose)
		except FileNotFoundError:
			print("Wordlist file not found")
		except KeyboardInterrupt:
			pass

	else:
		dnsOthers(args.domain, args.type)

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		os.system("clear")
		print(" ___            ___             _             ")
		print("|   \\ _ _  ___ | _ \\___ ___ ___| |_ _____ _ _ ")
		print("| |) | ' \\(_-< |   / -_|_-</ _ \\ \\ V / -_) '_|")
		print("|___/|_||_/__/ |_|_\\___/__/\\___/_|\\_/\\___|_|  \n\n")
		print("Commands:")
		print("\t-d\tTarget domain")
		print("\t-s\tSingle subdomain")
		print("\t-t\tDNS record type (A, AAAA, MX, TXT, NS, CNAME)")
		print("\t-w\tWordlist file containing subdomains")
		print("\t-v\tVerbose mode (optional)")
		print("Examples:")
		print(f"\tpython3 {sys.argv[0]} -d google.com -t MX")
		print(f"\tpython3 {sys.argv[0]} -d google.com -t NS -v")
		print(f"\tpython3 {sys.argv[0]} -d google.com -t TXT")
		print(f"\tpython3 {sys.argv[0]} -d google.com -t CNAME -v")
		print(f"\tpython3 {sys.argv[0]} -s www -d google.com -t A")
		print(f"\tpython3 {sys.argv[0]} -s www -d google.com -t AAAA -v")
		print(f"\tpython3 {sys.argv[0]} -w subdomains.txt -d google.com -t A")
		print(f"\tpython3 {sys.argv[0]} -w subdomains.txt -d google.com -t AAAA -v\n\n")
		sys.exit(1)
	else:
		main()