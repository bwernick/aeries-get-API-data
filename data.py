import requests
import lxml.etree as etree

url = "https://demo.aeries.net/aeries/api/v5/schools/"
headers = {'content-type': 'application/xml',
            "AERIES-CERT": "477abe9e7d27439681d62f4e0de1f5e1"
          }
          
r = requests.get(url, headers=headers)
#print (r.content)
x = etree.parse(r.content)
print(etree.tostring(x, pretty_print=True))