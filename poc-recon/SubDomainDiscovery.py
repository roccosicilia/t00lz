'''
Usege:  SubDomainDiscovery --domain contoso.hack --mode amass
'''

import requests
import sys
import subprocess

domain =    sys.argv[1]
mode =      sys.argv[2]
#output =    sys.argv[3]

if "amass" in mode:   # search subdomain via DuckDuckGo
    result = subprocess.check_output(["amass", "-passive", "enum", "-d", domain])
    print(result)
