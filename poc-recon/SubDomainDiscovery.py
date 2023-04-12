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
          \t -i: check ICMP response for the host\n \
          \t -w: check web content for the host\n")
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

            # check ICMP
            r_ping = subprocess.run(['ping', '-c', '1', subdomain_ip], capture_output=True)
            if result.returncode == 0:
                color = '31m'
            else:
                color = '32m'

            # print("| {} {} | {}\t|".format(subdomain_str, tab, subdomain_ip))
            output = "| {} {} | " + '\033[{}' + "{}" + '\033[0m' + "\t|".format(subdomain_str, tab, color, subdomain_ip)

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
    print("\n\n{}".format("#"*150))
    print(option)
else:
    print("\n\n{}".format("#"*150))