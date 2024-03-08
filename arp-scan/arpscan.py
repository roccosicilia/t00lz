#!/usr/bin/python
 
# Sends an arp resolution request on broadcast for an IP address
# If reply is received within timeout the host is alive
# aviran.org

from scapy.all import *
import sys
 
Timeout=2
 
if len(sys.argv) != 2:
    print ("Usage: arp_ping.py IP")
    sys.exit(1)
    
    
answered,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]),timeout=Timeout,verbose=False)
 
 
if len(answered) > 0:
    print (answered[0][0].getlayer(ARP).pdst, "is up")
elif len(unanswered) > 0:
    print (unanswered[0].getlayer(ARP).pdst, " is down")