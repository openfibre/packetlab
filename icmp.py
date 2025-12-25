from scapy.all import *

packet = IP(dst="8.8.8.8") / ICMP(type="echo-request")

response = sr1(packet, timeout=2, verbose=False)

# if response and response.haslayer(ICMP):
#     icmp = response[ICMP]
#     if icmp.type == 0:  # Echo Reply
#         print("Received ICMP Echo Reply")
