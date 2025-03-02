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

# ICMPScan.py
This script utilizes the Scapy library, a powerful packet manipulation tool for Python, to perform a network discovery task specifically an ARP (Address Resolution Protocol) scan within a specified IP range on a given network interface. Here's a breakdown of its functionality:

Note: Change the interface= and ip_range= to your specific requiremet.

Import Scapy Library: The script starts by importing all functions from the scapy.all module, which provides the necessary tools for crafting and transmitting packets.

Configuration Variables: It sets up three key variables:

interface: Specifies the network interface (e.g., "eth0") to be used for sending packets.
ip_range: Defines the target IP range (e.g., "10.0.0.0/24") for the ARP scan, indicating the script will scan all IPs within this subnet.
broadcastMac: The destination MAC address is set to the broadcast MAC address ("ff:ff:ff:ff:ff:ff"), meaning the ARP request will be sent to all devices in the subnet.
Crafting the ARP Request Packet: The script creates an ARP request packet (packet) by combining an Ethernet frame (Ether) destined for the broadcast MAC address with an ARP request (ARP) for the specified IP range (pdst=ip_range).

Sending the Packet and Receiving Responses: It then sends the crafted packet (srp(packet, timeout=2, iface=interface, inter=0.1)) on the specified interface with a timeout of 2 seconds between receiving the ARP reply. The inter=0.1 parameter specifies the interval between sending each packet. The srp function sends the packet at layer 2 and returns two lists: ans (answered), containing pairs of request and response packets, and unans (unanswered).

Processing Received Packets: For each pair of sent and received packets in the ans list, the script extracts and prints the source MAC address (%Ether.src%) and the source IP address (%ARP.psrc%) of the responding device.

This script is effectively used for network scanning or mapping, identifying all active devices within the specified IP range by sending ARP requests and listening for replies, which helps in understanding the network's structure or for security analysis.

# portscan.py
This script is a straightforward tool that leverages Python to conduct a port scanning operation. It's aimed at identifying open ports on a specific IP address, using fundamental network programming concepts. Here's how it breaks down:

Script Overview
Purpose: To scan for open ports on a predetermined IP address (10.10.68.76), effectively determining which ports are accepting connections. This can be useful for network security analysis or educational purposes in penetration testing scenarios.
Key Components of the Script
Initial Setup:

Imports necessary Python modules: sys for system-specific parameters, socket for network interface, and pyfiglet for generating ASCII art headers.
Prepares a target IP address and a range of ports (1 through 65534) for scanning.
ASCII Art Banner:

Generates and displays a stylized banner using pyfiglet to make the script's output more engaging.
Scanning Mechanism:

Defines a function probe_port to attempt connections to each port on the target IP address. It uses the socket module to handle network communications.
Iterates through all possible port numbers, using probe_port to check if each port is open (able to establish a TCP connection).
Collects and lists any open ports found during the scan.
Output:

Concludes by printing out all discovered open ports, providing a concise overview of accessible services on the target machine.
Example Usage
Scenario: You're conducting a security audit on a networked device with IP 10.10.68.76, aiming to identify potentially vulnerable open ports.
Action: Run this script as is, assuming Python and pyfiglet are installed on your system.
Outcome: Receive a list of open ports, which can then be analyzed for security implications or further penetration testing tasks.
This script serves as a basic yet practical example of how to implement port scanning with Python, emphasizing core programming techniques in network security.

Requires: pyfiglet (pip install pyfiglet)

# filedownloader.py
In essence, this script downloads the PSTools.zip file from the Sysinternals website and saves it to the local filesystem. This is a straightforward way to programmatically download files from the internet using Python.

# hashcrack.py
This script is a basic MD5 hash cracker designed for educational purposes, likely aimed at individuals learning about cybersecurity, particularly in penetration testing scenarios like those found on TryHackMe. The script attempts to crack an MD5 hash by comparing it against a list of potential plaintext passwords (a wordlist). Here's how it breaks down:

How It Works:
Display an ASCII Art Banner: It uses the pyfiglet library to generate and print an ASCII art banner titled "TryHackMe \n Python 4 Pentesters \n HASH CRACKER for MD5", creating a visually appealing introduction.

Input from User:

Wordlist Location: The script prompts the user to input the location of a wordlist file. This file should contain a list of potential plaintext passwords, one per line.
Hash to Be Cracked: The user is also prompted to enter the MD5 hash that they wish to crack.
Cracking Process:

The script reads the wordlist file line by line.
Each line (presumed to be a potential password) is stripped of leading and trailing whitespace and then encoded into bytes.
The script uses the hashlib.md5() function to compute the MD5 hash of each potential password.
It compares the computed hash with the input hash. If a match is found, it indicates that the plaintext version of the hashed password has been identified.
Output: If a matching hash is found, the script prints the message "Found cleartext password!" followed by the plaintext password. It then exits.

How to Use It:
Prepare Your Environment:

Ensure Python is installed on your system.
Install the pyfiglet module if it's not already installed, using the command: pip install pyfiglet.
Prepare a Wordlist:

You need a wordlist file (a text file with potential passwords, one per line). The effectiveness of the script depends on the quality and comprehensiveness of the wordlist.
Run the Script:

Execute the script by running it in your terminal or command prompt.
When prompted, enter the full path to your wordlist file.
Enter the MD5 hash you want to crack when prompted.
Example Usage:
Imagine you want to crack the MD5 hash 5f4dcc3b5aa765d61d8327deb882cf99 (which is the hash for the password "password").

You run the script.
Enter the path to your wordlist when prompted (e.g., /path/to/wordlist.txt).
Enter 5f4dcc3b5aa765d61d8327deb882cf99 as the hash to be cracked.
If "password" is in your wordlist, the script will output: Found cleartext password! password.

# keylogger.py
This script is a simple Python program that utilizes the keyboard library to record and then replay keystrokes made by the user until the ENTER key is pressed. Here's a breakdown of its functionality and usage:

What the Script Does:
Record Keystrokes: The script starts recording keystrokes as soon as it is run. Every key press, including special keys and combinations, is logged until the ENTER key is pressed.

Replay Keystrokes: After the ENTER key is pressed, the script stops recording and immediately replays all the recorded keystrokes in the same order and timing as they were originally made.

Components of the Script:
import keyboard: This imports the keyboard module, which allows Python scripts to control and interact with the keyboard directly.

keys = keyboard.record(until ='ENTER'): This line starts the recording process. It keeps recording all keystrokes until the ENTER key is pressed. The recorded sequence of keystrokes is stored in the keys variable.

keyboard.play(keys): This line replays the recorded keystrokes stored in keys.

How to Use the Script:
Install the keyboard Module: First, you need to have the keyboard library installed. If you haven't installed it yet, you can do so by running pip install keyboard in your terminal or command prompt. Note that you might need administrative privileges to install this library or run scripts that use it, due to the need for low-level keyboard access.

Run the Script: Execute the script by running it with Python from your terminal or command prompt. You might need to run your terminal as an administrator or use sudo on Linux/Mac due to the library's requirement for elevated permissions.

Record and Replay Keystrokes: After starting the script, begin typing anything you want. The script will record all your keystrokes, including letters, numbers, and special keys, until you press ENTER. Once ENTER is pressed, the script will automatically replay all the keystrokes you made.

# sshbrute.py
This Python script is designed to perform a brute-force attack on an SSH server using a specified username and a list of potential passwords. It utilizes the Paramiko library to establish SSH connections and systematically tests each password from the provided list against the server. Here's a basic overview of its operation:

Collects Input from the User: The script prompts the user to enter three pieces of information: the target IP address of the SSH server, the username to attempt the brute-force attack on, and the location of a text file containing a list of potential passwords.

Defines a Function for SSH Connection Attempts: It contains a function, ssh_connect, which attempts to connect to the SSH server using the provided username and one of the passwords from the list. This function tracks whether the connection attempt was successful or failed due to authentication errors.

Iterates Through the Password List: The script reads the password file line by line, stripping any extra whitespace from each password. It then uses the ssh_connect function to test each password.

Determines and Reports Outcome: For each password attempt, the script checks the connection outcome. If a password is successfully used to connect (authentication succeeds), the script prints the password, indicating it has been "found", and then exits. If the attempt fails, it prints "no luck" and continues to the next password in the list.

Error Handling: The script includes basic error handling to catch and report exceptions that may occur during the SSH connection attempt.

Closes Resources: The script incorrectly attempts to close a file (input_file.close()), which is a mistake since the file object is not defined as input_file and because the file is automatically closed by the with statement.

Usage: To use this script, ensure you have Python and the Paramiko library installed. Run the script and follow the prompts to input the target IP address, username, and password file location.
