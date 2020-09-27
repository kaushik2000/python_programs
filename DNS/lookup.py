def parse_dns(dns_raw):
    for line in dns_raw :
        if line.startswith("#") or line == "\n" : continue
        line = line.strip()
        all_records = line.split(", ")
        about_domain = {"type" : all_records[0], "alias" : all_records[2]}
        dns_records[all_records[1]] =  about_domain
    return dns_records

def resolve(dns_records, lookup_chain, domain):
    lookup_domain = lookup_chain[-1]
    try:
        dns_records[lookup_domain]
    except:
        print("Error: record not found for domain:", domain)
        return

    if (dns_records[lookup_domain]["type"] == "A"):
        lookup_chain.append(dns_records[lookup_domain]["alias"]) 
        return lookup_chain
    else:
        lookup_chain.append(dns_records[lookup_domain]["alias"]) 
        return resolve(dns_records,lookup_chain,domain)  
    
while True:
        
    # File-handle for DNS zone file
    dns_raw = open("zone")
    
    # Getting Domain name fro client
    domain = input("Enter domain name for lookup: ")
    if len(domain) < 1: 
        print("No domain found!")
        continue
    
    dns_records = dict()
    dns_records = parse_dns(dns_raw)
    lookup_chain = [domain]
    lookup_chain = resolve(dns_records, lookup_chain, domain)
    if lookup_chain is not None:
        for record in lookup_chain:
            print(" => ", record, end="")
        print("\n")
    else:
        continue