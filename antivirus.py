import requests
import time
import json
indicators = ["C:", "D:"]

url     =   "https://www.virustotal.com/api/v3/urls/id"
api_key =  "bcde9f92fc4138187ec2f952d129461663289ff65e53e555f2b41aedc32287dd"

for file in indicators:
   def get_channel(destination_file, api_key):
       response = requests.get(url, get_channel)
       response_json = json.loads(response.content)

       if response_json["positives"] <= 0:
        with open('results1.txt', 'a') as x:
             
               x.write(file) and x.write("-\t NOT MALICIOUS \n ")
       elif 1 >=  response_json["positives"] >= 3:
        with open('results2.txt', 'a') as x:
           
           x.write(file) and x.write("-\t MAYBE MALICIOUS \n ")
       elif response_json["positives"] >= 4:
        with open('results3.txt', 'a') as x:
           
             x.write(file) and x.write("-\t  MALICIOUS \n ")
       else: 
           print("Url not found")
           
       
       
time.sleep(10)
    
       
       
    
    
    
    
    
    




