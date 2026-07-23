import requests # In order to request for status_code

def http_collection(domain): # Stored in a function to simply return the dictionary
    http_results = { # Dictionary in order to store all http collected data and return in one variable
        "domain": domain,
        "https_status": "", 
        "http_status": "",
        "redirect": "",
    }

    try:
        response = requests.get(f"https://{domain}", timeout=15, allow_redirects=False)  # Make request to domain. Redirects false as we want to simply know about any redirects
        http_results["https_status"] = response.status_code # To keep updating the dictionary as data is gathered
        if response.status_code in [301, 302, 303, 307, 308]: # Check if the status code is a redirect
            http_results["redirect"] = response.headers.get("Location") # Get the redirect location if status code is a redirect
    except:
        pass

    if http_results["https_status"] == "": # Selection if https if empty, uses http as a fallback
        try:
            response = requests.get(f"http://{domain}", timeout=15, allow_redirects=False) # Same as https section, except with http
            http_results["http_status"] = response.status_code
            if response.status_code in [301, 302, 303, 307, 308]:
                http_results["redirect"] = response.headers.get("Location")
        except:
            pass

    return http_results # Return all gathered data 

