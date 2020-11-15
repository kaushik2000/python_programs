import dns.resolver
from scapy.all import *
while True:
    while True:
        hostname = input("Enter a domain name: ").lower()
        if len(hostname) < 1 :
            print("<-- Invalid domain name -->")
            continue
        else:
            break

    # Resolving the given hostname # DNS is set to operate on UDP port 53
    record_type = "A"
    domain = hostname
    try :
        result = dns.resolver.query(domain, record_type)
    except :
        print("<-- Invalid domain name -->")
        continue
    for ipval in result:
        print('<<-- Resolving domain:', hostname, ' -->\n>>>> IP', ipval.to_text(), ' <<<<\n')
    resolved_hostname = ipval.to_text()

    print("<<-- Forming a packet with IPv4 Protocol -->>")
    ans,unans = traceroute(resolved_hostname,l4=UDP(sport=RandShort(), dport=53)/DNS(qd=DNSQR(qname=hostname)))
    print("Answered packets: ", ans)
    print("Unanswered packets", unans, "\n----------")

    #res,unans = sr(IP(dst=resolved_hostname, ttl=(5,10), flags="MF")/UDP(sport=RandShort(), dport=53), timeout=125)

    # Tracing the route of the sent packet
    traceroute(resolved_hostname)
    print("<--- Trace Complete --->\n")
