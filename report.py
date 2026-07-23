def report_generator(dns_results, http_results, cert_results, file_results, domain): # Takes the parameters of the data in the poorly formatted dictionaries
    report_text = ""
    report_text = report_text +  f"Gathered information for {domain} \n" # To clearly state the domain once at the top

    for results_type in [dns_results, http_results, cert_results, file_results]: # For each of the types of results, iterates through the four result dictionaries.
        for rtype, record in results_type.items(): # Loops through each key value pair in the dictionary

            if rtype == "domain": # Domain is in all dictionaries, this ensures the domain isnt repeated as it is already put in by line 3
                continue

            if type(record) == list: # If the value is a list then change formatting
                report_text = report_text + f"{rtype}\n" # So user can see what record type the outputted list consists of
                for item in record: # For iterating each item in the list 
                    report_text = report_text + f"- {item} \n" # Bulletpoint each value in the list
            else:
                report_text = report_text + f"{rtype}: {record}\n" # For one value, this formating seperated with a colon, as it is easier to read

    return report_text
    
    
