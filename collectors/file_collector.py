import requests # Necessary to check for public files on the domain

def file_collection(domain):
    file_results = {
        "domain": domain,
        "robots.txt": "",
        "sitemap.xml": "",
        "security.txt": "",
    }

    try:
        response = requests.get(f"https://{domain}/robots.txt", timeout = 15) # Requests the entire response regarding the robots.txt file
        if response.status_code == 200: # Uses .status_code to extract only status code, with 200 being file found and accessable.
            file_results["robots.txt"] = f"https://{domain}/robots.txt" 
    except:
        pass

    try:
        response = requests.get(f"https://{domain}/sitemap.xml", timeout = 15) # Identical logic as above, substituting robots.txt for sitemap.xml
        if response.status_code == 200: 
            file_results["sitemap.xml"] = f"https://{domain}/sitemap.xml" 
    except:
        pass

    try:
        response = requests.get(f"https://{domain}/.well-known/security.txt", timeout = 15) # Identical logic as above, substituting sitemap.xml for .well-known/security.txt
        if response.status_code == 200: 
            file_results["security.txt"] = f"https://{domain}/.well-known/security.txt" 
    except:
        pass

    return file_results
