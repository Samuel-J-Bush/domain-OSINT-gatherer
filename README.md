# Domain OSINT gatherer
This project is a tool that collects publically accessable information about a domain and summarises it into a file or terminal output.

## What it does
- Allows user to input name of target domain
- Allows user to choose whether new file or terminal output
- Collects information from the following fields:
    - DNS information
    - HTTP information
    - Certificate information
    - File information
- Outputs in terminal or creates a new text document (in newly created folder if first run of tool) with information

## Collections
### DNS
1. A, AAAA records
2 MX records (mail servers)
3. NS rcords (nameservers)
### HTTP
1. HTTPS status
2. HTTP status (as a fallback for HTTPS)
3. Redirects
### Certificate
1. Certificate issuer
2. Valid from date
3. Valid untill date
### File
1. robots.txt
2. sitemap.xml
3. security.txt
### Whois
1. registrar
2. registrant (if available)
3. creation and expiration date

## Output
When inputting the domain, the user has the option of two output types.
1. Terminal output - Output in the terminal with the data for quick access and use.
2. File creation - Creates a folder called reports if it has not already been created.
    - File with the data saved in the reports folder and referred back to in future.
    - If tool is ran again then the new file will be added to same reports folder.

## Example
### For example, to gather information on google.com.

![Input in terminal](/screenshots/input.png)

### And to be put into a file.

![Output in a file](/screenshots/output.png)

### If it was not in a file, the output is identical - just in the terminal.
