'''
Usege amass mode:  SubDomainDiscovery.py amass ShodanKey 
'''

import requests
import sys
import subprocess
import socket
import json

### mode and flag management
if len(sys.argv) < 4:
    print("Usage: python ./{} DomainName Mode ShodanKey [flags]".format(sys.argv[0]))
    print("Available Mode: amass")
    print("Flags:\n \
          \t -b: brute forcing domain\n \
          \t -i: check for alive hosts (ICMP)\n")
    sys.exit()

domain = sys.argv[1]
mode = sys.argv[2]
shodan_key = sys.argv[3]
try:
    option = sys.argv[4]
except:
    option = None

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

def tabber15(string):
    string_len = len(string)
    empty = 15 - string_len
    tab = '-'*empty
    return tab

### main program -- anass utility
if "amass" in mode:   # search subdomain via DuckDuckGo
    result = subprocess.check_output(["amass", "enum", "-passive", "-d", domain])
    #print(result.decode("utf-8"))
    subdomains = result.splitlines()

    content = {}
    i = 0
    iplist = []
    domainlist = []
    for subdomain in subdomains:

        # preset
        output = ''

        # gat domain info
        print("# Get domain info for {}".format(subdomain))
        try:

            # get IP from subdomain
            subdomain_ip = socket.gethostbyname(subdomain)
            subdomain_str = subdomain.decode("utf-8")
            tab = tabber50(subdomain_str)

            # print("| {} {} | {}\t|".format(subdomain_str, tab, subdomain_ip))
            output = "| {} {} | {}\t|".format(subdomain_str, tab, subdomain_ip)
            iplist.append(subdomain_ip)
            domainlist.append(subdomain_str)

        except:

            subdomain_str = subdomain.decode("utf-8")
            tab = tabber50(subdomain_str)
            # print("| {} {} | n/a \t\t|".format(subdomain_str, tab))
            output = "| {} {} | n/a \t\t|".format(subdomain_str, tab)
        
        # get shodan info
        print("# Get Shodan info for {}".format(subdomain))
        try:

            shodan_query = "https://api.shodan.io/shodan/host/{}?key={}".format(subdomain_ip, shodan_key)
            #print("### DEBUG ### {}".format(shodan_query))

            shodan_result = subprocess.check_output(["curl", "-X", "GET", shodan_query])
            #print("### DEBUG ### {}".format(shodan_result))

            shodan_json = json.loads(shodan_result.decode("utf-8"))

            org = shodan_json["org"]
            org = org[:15]
            org_tab = tabber15(org)
            
            asn = shodan_json["asn"]
            asn_tab = tabber15(asn)

            shodan_ports = shodan_json["ports"]
            ports = shodan_ports[:5]
            portlist = ''
            for port in ports:
                portlist += "{} ".format(port)
            ports_tab = tabber25(portlist)

            output = output + " {} {} | {} {} | {} {} |".format(asn, asn_tab, org, org_tab, portlist, ports_tab)
            
            content[i] = output
            i = i + 1
        
        except:

            content[i] = output
            i = i + 1

### print the content ###
print("\n\n{}".format("#"*150))
for element in content.values():
    print(element)
print("{}".format("#"*150))

### print the content ###
if option != None:
    print("\n\n{}\n".format("#"*150))
    print(" -- Details for alive host\n")

    # check for ICMP response
    if 'i' in option:
        hostalive = []
        for host in iplist:
            r_ping = subprocess.run(['ping', '-c', '4', host], capture_output=True)
            if r_ping.returncode == 0:
                hostalive.append(host)
        print("List of alive host: {}".format(hostalive))

else:
    print("\n\n{}".format("#"*150))