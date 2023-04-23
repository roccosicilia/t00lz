from scapy.all import *
import string
import sys

# var
packets_seen = set()
source_os = sys.argv[1]
message = []

def read(packet):
    if packet.haslayer(ICMP):
        # check OS
        if source_os == 'unix':
            data = ''.join(filter(lambda x: x in string.printable, packet[ICMP].load.decode('ISO-8859-1')))
            print(data)
        elif source_os == 'win':
            data = packet[ICMP].load
            #if data not in packets_seen:
            packets_seen.add(data)
            # print("Size: {}".format(len(data)))
            if (len(data) == 1):
                message.clear()
            else:
                message.append(len(data))
    else:
        print("No ICMP packets")
    
    print(message)

sniff(filter="icmp", prn=read)