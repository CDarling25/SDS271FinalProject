import pandas as pd 
import requests
from requests import get
import json
from ip2geotools.databases.noncommercial import DbIpCity

def main():
    payload = {"seriesid": ["CUUR0000SA0", "SUUR0000SA0"],
            "startyear": "2013",
            "endyear": "2014",
            "catalog":"false",
            "registrationkey": "99c5831b88614d4285efc658f040b2b6"
            }

    response = requests.post("https://api.bls.gov/publicAPI/v2/timeseries/data", data = payload)

    print(response.text)

    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip))
    res = DbIpCity.get(ip, api_key="free")
    print(f"Location: {res.city}, {res.region}, {res.country}")

if __name__=="__main__":
  main()