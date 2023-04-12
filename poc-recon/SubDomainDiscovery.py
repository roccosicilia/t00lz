'''
Usege:  SubDomainDiscovery --domain contoso.hack --mode amass
'''

import requests
import sys
import subprocess
import socket
import json
from shodan import Shodan

domain = sys.argv[1]
mode = sys.argv[2]
shodan_key = sys.argv[3]

### function def
def tabber50(string):
    string_len = len(string)
    empty = 50 - string_len
    tab = '-'*empty
    return tab

def tabber25(string):
    string_len = len(string)
    empty = 25 - string_len
    tab = '-'*empty
    return tab

### main program -- anass utility
if "amass" in mode:   # search subdomain via DuckDuckGo
    result = subprocess.check_output(["amass", "enum", "-passive", "-d", domain])
    #print(result.decode("utf-8"))
    subdomains = result.splitlines()

    content = {}
    i = 0
    for subdomain in subdomains:

        # gat domain info
        print("# Get domain info for {}".format(subdomain))
        try:

            subdomain_ip = socket.gethostbyname(subdomain)
            subdomain_str = subdomain.decode("utf-8")
            tab = tabber50(subdomain_str)
            # print("| {} {} | {}\t|".format(subdomain_str, tab, subdomain_ip))
            output = "| {} {} | {}\t|".format(subdomain_str, tab, subdomain_ip)

        except:

            subdomain_str = subdomain.decode("utf-8")
            tab = tabber50(subdomain_str)
            # print("| {} {} | n/a \t\t|".format(subdomain_str, tab))
            output = "| {} {} | n/a \t\t|".format(subdomain_str, tab)
        
        # get shodan info
        print("# Get Shodan info for {}".format(subdomain))
        #try:

        shodan_query = "https://api.shodan.io/shodan/host/{}?key={}".format(subdomain_ip, shodan_key)
        #print("### DEBUG ### {}".format(shodan_query))

        shodan_result = subprocess.check_output(["curl", "-X", "GET", shodan_query])
        #print("### DEBUG ### {}".format(shodan_result))

        shodan_json = json.loads(shodan_result.decode("utf-8"))

        org = shodan_json["org"]
        org_tab = tabber25(org)
        
        asn = shodan_json["asn"]
        asn_tab = tabber25(asn)

        shodan_ports = shodan_json["ports"]
        ports = ", ".join(shodan_ports[:5])
        ports_tab = tabber25(ports)

        output = output + " {} {} | {} {} | {} {} |".format(asn, asn_tab, org, org_tab, ports, ports_tab)
        
        content[i] = output
        i = i + 1
        
        #except:

            #content[i] = output
            #i = i + 1

### print the content ###
print("\n\n{}".format("#"*50))
for element in content.values():
    print(element)
