from scapy.all import *

packet = IP(dst="104.18.26.120") / TCP(sport=RandShort(), dport=80, flags="S", seq=1000)

response = sr1(packet, timeout=2, verbose=False)

# if response and response.haslayer(TCP):
#     tcp = response[TCP]
#     if tcp.flags & 0x12:  # SYN-ACK
#         print("Received SYN-ACK")
#     elif tcp.flags & 0x14:  # RST-ACK
#         print("Received RST")
