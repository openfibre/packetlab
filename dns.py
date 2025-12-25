from scapy.all import *

packet = IP(dst="164.100.3.1") / UDP(sport=RandShort(), dport=53) / \
         DNS(rd=1, qd=DNSQR(qname="example.com"))

response = sr1(packet, timeout=2, verbose=False)

# if response and response.haslayer(DNS):
#     dns = response[DNS]
#     for i in range(dns.ancount):
#         print(dns.an[i].rdata)
