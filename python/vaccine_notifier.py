import time
import requests
from playsound import playsound

print("Select mode: 1 - Pincode, 2 - District: ",end="")
mode = int(input())
pincode = ""
district = ""
district_code = ""

if(mode == 1):
    print("Input Pincode: ",end="")
    pincode = input()
elif(mode == 2):
    print("Enter District Name: ",end="")
    district = input()
    # Todo district mapping
    district_code = "307"
else:
    print("Invalid choice!")
print("Enter date in DD-MM-YYYY format: ",end="")
date = input()

print("Enter Age: ",end="")
age = int(input())

urls = [
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+district_code+"&date="+date, 
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+pincode+"&date="+date 
]

header = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Origin": "https://www.cowin.gov.in",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.cowin.gov.in/",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

print("Checking for open slots. Will noitfy when available...")
def makeRequest():
    response = requests.get(urls[0], headers = header)
    centers = response.json()["centers"]
    for center in centers:
        sessions = center["sessions"]
        checkEachSession(sessions)

def checkEachSession(sessions):
    for session in sessions:
        if(session["min_age_limit"] <= age):
            if(session["available_capacity"] > 0):
                print("We have a vaccine slot available!")
                playsound('./alert.mp3')

while(True):
    makeRequest()
    time.sleep(5)