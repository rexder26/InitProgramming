import requests
from time import time
 
user = input("[+] Enter The Url You want to ping: ") 
while True :
    req = requests.get (f'https://{user}')
    begin_time = time ()
    if req.status_code != "410" and req.status_code != "503":
        print("[+] Site is Up!")
    else:
        print("[.] Site is #DOWN!")
     
