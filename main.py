import os # Import for folder generation feature
from collectors.dns_collector import dns_collection # So the functions that collect the data in their section are callable
from collectors.http_collector import http_collection
from collectors.certificate_collector import cert_collection
from collectors.file_collector import file_collection 
from report import report_generator # So the report_generator function can imporve formatting of the dictionaries to be outputted

domain = input("Enter domain name: ") # User can select the domain to gather info about
option = input("Do you want output in terminal or output in a file. Enter t or f: ").lower() # So user can choose between terminal output or file creation

dns_results = dns_collection(domain) # Contains the data in the results variables so they can be put as arguments for report_generator
print("DNS collection complete")
http_results = http_collection(domain)
print("http collection complete")
cert_results = cert_collection(domain)
print("Certificate collection complete")
file_results = file_collection(domain)
print("File collection complete")
total_report = report_generator(dns_results, http_results, cert_results, file_results, domain) # In order to have a better formatted, easier to read output.
print("Report generation complete")

if os.path.exists("reports") == False: # To only make a new folder if the reports folder doesnt exist 
    os.mkdir("reports")

if option == "f":
    filename = f"reports/{domain}_information.txt" # So the filename is recognisable as info on the domain and saved into the reports folder
    with open(filename, "w", encoding = "utf-8") as newfile: # Opening file in "write" makes a new file or overwrites if report for domain already exists
        newfile.write(total_report)

elif option == "t":
    print(total_report) # So user can see results in terminal

else: 
    print("Input error, please run again and enter t or f")
