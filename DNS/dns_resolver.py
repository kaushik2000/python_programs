import dns.resolver 

while True:
    record_type = input(">>>> Enter the record type required(A/CNAME/MX): ").strip().upper()
    if record_type != "A" and record_type != "CNAME" and record_type != "MX" : 
        print(">>>> The entered record doen't exist. Please select the record")
        continue
    domain = input(">>>> Enter the domain name: ")
    try:
        result = dns.resolver.query(domain, record_type)
    except Exception as e:
        print(">>>> Error", type(e))
        print()
        continue
    
    if record_type == "A" :
        for ipval in result:
            print('>>>> IP', ipval.to_text())
    elif record_type == "CNAME" :
        for cname_value in result:
            print('>>>> Canonical Name: ', cname_value.target)
    elif record_type == "MX" :
        for exchange_data in result:
            print('>>>> MX Record', exchange_data.exchange.to_text())
    print()