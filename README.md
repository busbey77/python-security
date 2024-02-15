# python-security
Python scripts used for CTFs

# subdomenum.py
This script is designed to check for the existence of subdomains for a given domain name by making HTTP requests to each subdomain listed in a file named subdomains.txt. It works as follows:

Use with the file subdomains.txt

The script imports necessary modules: requests for making HTTP requests and sys for accessing command-line arguments.
It reads a list of potential subdomains from a file called subdomains.txt, splitting the file content into individual subdomains based on new lines.
For each subdomain, the script constructs a URL by appending the subdomain to the user-provided domain name (accessed via sys.argv[1]), using the HTTP protocol.
It then attempts to make an HTTP GET request to each constructed URL.
If a connection error occurs (indicating the subdomain does not exist or is unreachable), the script silently ignores the error and continues to the next subdomain.
If the request is successful (indicating the subdomain likely exists), the script prints a message stating "Valid domain: " followed by the URL of the valid subdomain.
This script is useful for discovering active subdomains of a specific domain, which can be an important task in network administration, IT security assessments, or penetration testing.

