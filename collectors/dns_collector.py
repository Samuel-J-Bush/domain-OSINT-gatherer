import dns.resolver # Import necessary to peform dns.resolver.resolve for each record

def dns_collection(domain):
    dns_results = { # In order to keep all dns records in one variable to be easily returned together
        "domain": [],
        "A": [],
        "AAAA": [],
        "MX": [],
        "NS": [],
    }
    
    for record in ["A","AAAA","MX","NS"]: # So the record itself iterates but all use the same dns.resolve process
        try:
            answers = dns.resolver.resolve(domain, record) # Queries the DNS for the record type on the domain
            records_as_strings = []
            for rdata in answers: # In order to have each individual answer returned from DNS put in one list
                record_string = str(rdata) # Allows data to be readable as sstring
                records_as_strings.append(record_string)
            dns_results[record] = records_as_strings # Stores the list of records back in the appropriate place in the dictionary
        except:
            pass

    return dns_results # Returns the results held in the dictionary in the single variable
