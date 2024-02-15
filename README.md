# python-security
Python scripts used for CTFs

# subdomenum.py
This script is designed to check for the existence of subdomains for a given domain name by making HTTP requests to each subdomain listed in a file named subdomains.txt. It works as follows:

Use with the file subdomains.txt

Example usage: python3 ./subdomenum.py tryhackme.com

The script imports necessary modules: requests for making HTTP requests and sys for accessing command-line arguments.
It reads a list of potential subdomains from a file called subdomains.txt, splitting the file content into individual subdomains based on new lines.
For each subdomain, the script constructs a URL by appending the subdomain to the user-provided domain name (accessed via sys.argv[1]), using the HTTP protocol.
It then attempts to make an HTTP GET request to each constructed URL.
If a connection error occurs (indicating the subdomain does not exist or is unreachable), the script silently ignores the error and continues to the next subdomain.
If the request is successful (indicating the subdomain likely exists), the script prints a message stating "Valid domain: " followed by the URL of the valid subdomain.
This script is useful for discovering active subdomains of a specific domain, which can be an important task in network administration, IT security assessments, or penetration testing.

# directoryenum.py
This script is designed to automate the process of directory enumeration on a given website by attempting to access a list of directories specified in a file named wordlist.txt. Here's a summary of its operation:

Example usage: python3 ./directoryenum.py tryhackme.com

The script begins by importing necessary modules: requests for making HTTP requests, and sys for accessing command-line arguments.
It reads a file named wordlist.txt, which contains a list of directory names (one per line), and splits this list into individual directory names.
For each directory name in the list, the script constructs a URL by appending the directory name (with an .html extension) to the base URL provided as a command-line argument (sys.argv[1]). It assumes the use of the HTTP protocol for the URL.
It makes an HTTP GET request to each constructed URL.
If the request returns a 404 status code, indicating that the directory does not exist on the server, the script ignores this and moves on to the next directory name in the list.
If the request returns any other status code, implying that the directory might exist (because it did not return a 404 error), the script prints a message stating "Valid directory:" followed by the URL of the directory.
This script is useful for web application testing, particularly for finding potentially accessible directories that are not directly linked from the site's main pages, which can be part of security assessments, penetration testing, or web scraping tasks.
