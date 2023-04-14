from scapy.all import *
import string

def read(packet):
	if packet.haslayer(ICMP):
		# print(packet.show())
		data = ''.join(filter(lambda x: x in string.printable, packet[ICMP].load.decode('ISO-8859-1')))
		print(data)

sniff(filter="icmp", prn=read)