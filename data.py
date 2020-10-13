import requests
import xml.etree.ElementTree as ET

baseURL = "https://demo.aeries.net/aeries/api/v5/schools/"
headers = {'content-type': 'application/json',
            "AERIES-CERT": "477abe9e7d27439681d62f4e0de1f5e1"
          }
        
def makeAPICall(url):
  return requests.get(url, headers=headers)

#Prints all school codes and school names
def getSchools():
  resp = makeAPICall(baseURL)
  data = resp.json()
  for entry in data:
    sc = entry["SchoolCode"]
    sn = entry["Name"]
    print(sc, ' - ', sn)

#def getSchools(schoolCode):

if __name__ == "__main__":
  getSchools()