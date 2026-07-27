import ssl
import socket # Necessary imports for ssl and socket connections

def cert_collection(domain):
    cert_results = {
        "domain": domain,
        "issuer": "",
        "valid_from":"",
        "valid_until":"",
    }

    try:
        context = ssl.create_default_context() # Create the secure connection context
        connection = socket.create_connection((domain, 443), timeout = 15) # Connect to domain on port 443 (HTTPS)
        wrapped_connection = context.wrap_socket(connection, server_hostname = domain) # Wrap the connection with SSL

        certificate = wrapped_connection.getpeercert()
        wrapped_connection.close() # Connection can now be closed as we have certificate so now pull data from that

        issuer_list = certificate["issuer"] # Extract the issuer list from cert
        for issuer in issuer_list:
            issuer_name = issuer[0][1] # Extracts the name of the organisation that issued the certificate
            cert_results["issuer"] = issuer_name # Feed back data to dictionary

        cert_results['valid_from'] = certificate['notBefore']  # Store valid from data in results, in the certificate it is called notBefore
        cert_results['valid_until'] = certificate['notAfter']  # Store valid until data in results, in the certificate it is called notAfter
    
    except: # Catch any errors so doesnt stop the whole collection if a certificate collection error
        pass

    return cert_results
