'''
Usege:  SubDomainDiscovery --domain contoso.hack --mode amass
'''

import requests
import sys
import subprocess
import socket

domain =    sys.argv[1]
mode =      sys.argv[2]
#output =    sys.argv[3]

print

if "amass" in mode:   # search subdomain via DuckDuckGo
    result = subprocess.check_output(["amass", "enum", "-passive", "-d", domain])
    #print(result.decode("utf-8"))
    subdomains = result.splitlines()

    for subdomain in subdomains:
        subdomain_ip = socket.gethostbyname(subdomain)
        print("| {}\t| {}\t|".format(subdomain, subdomain_ip))
        