from scapy.all import *
import string
import sys
import time

# var
# packets_seen = set()
source_os = sys.argv[1]
message = []

def read(packet):
    filenale = time.strftime("%Y%m%d-%H%M")
    if packet.haslayer(ICMP):
        # check OS
        if source_os == 'unix':
            data = ''.join(filter(lambda x: x in string.printable, packet[ICMP].load.decode('ISO-8859-1')))
            print(data)
        elif source_os == 'win':
            data = packet[ICMP].load
            #if data not in packets_seen:
            #packets_seen.add(data)
            # print("Size: {}".format(len(data)))
            if (len(data) == 1):
                message.clear()
                file = open("./stream.txt", "a")
                # file.write("\n-----\n")
                file.close()
            else:
                message.append(len(data))
                file = open("./stream.txt", "a")
                file.write("{}, ".format(len(data)))
                file.close()
    else:
        print("No ICMP packets")
    
    # debug message
    print(message)

sniff(filter="icmp", prn=read)