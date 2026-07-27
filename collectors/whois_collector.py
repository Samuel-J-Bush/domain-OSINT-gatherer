import whois # Import whois to query domain registration info

def whois_collection(domain):
    whois_results = { # Dictionary to store all whois data in one variable
        "domain": domain,
        "registrar": "",
        "registrant": "",
        "creation_date": "",
        "expiration_date": "",
    }

    try:
        whois_data = whois.whois(domain) # Query whois for domain information

        if whois_data.registrar: # Check if registrar data exists before storing it in the dictionary
            whois_results["registrar"] = str(whois_data.registrar)

        if whois_data.registrant_name: # Check if registrant name exists 
            whois_results["registrant"] = str(whois_data.registrant_name)

        if whois_data.creation_date:
            creation_date_list = whois_data.creation_date # Get the list of dates
            if type(creation_date_list) == list: # Check if it's a list because it keeps returning a not human readable list
                whois_results["creation_date"] = str(creation_date_list[0]) # Take first date in the list and convert to string
            else: 
                whois_results["creation_date"] = str(creation_date_list) # Otherwise it is not a lsit and can just be added as a string

        if whois_data.expiration_date: 
            expiration_date_list = whois_data.expiration_date 
            if type(expiration_date_list) == list: 
                whois_results["expiration_date"] = str(expiration_date_list[0]) 
            else: 
                whois_results["expiration_date"] = str(expiration_date_list) 

    except: # Catch errors so it doesn't stop the whole collection if whois lookup fails
        pass

    return whois_results # Returns the results held in the dictionary
