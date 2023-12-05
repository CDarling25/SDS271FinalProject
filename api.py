import pandas as pd 
import requests
from requests import get
import json
from ip2geotools.databases.noncommercial import DbIpCity
from dotenv import load_dotenv
import os

class BLS():
    def __init__(self, interest):
        self.interest = interest
        self.interest_Series = None
        self.ip = None
        self.location = None

    def set_location(self):
        self.ip = get('https://api.ipify.org').content.decode('utf8')
        self.location = DbIpCity.get(ip, api_key="free")
        # this method will get the user’s location

    def get_api_key(self):
        # instruct user to make .env file to store in format API_KEY=29374af23 first. Then run this function automatically upon instantiation of class
        load_dotenv()
        api_key = os.getenv("API_KEY")
        return api_key

  # this will set the api key for the user
    def set_interest_Series(self):
        codes = pd.read_csv("cpi_item_codes.csv")
        print(codes.head())
        # for i in range(len(codes)):
        #   if



def main():
    test = BLS("food")
    api_key = test.get_api_key()
    test.set_interest_Series()
    payload = {"seriesid": ["CUUR0000SA0", "SUUR0000SA0"],
            "startyear": "2013",
            "endyear": "2014",
            "catalog":"false",
            "registrationkey": f"{api_key}"
            }

    response = requests.post("https://api.bls.gov/publicAPI/v2/timeseries/data", data = payload)

    print(response.text)

    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip))
    res = DbIpCity.get(ip, api_key="free")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(pd.read_csv("cpi_item_codes.csv"))
if __name__=="__main__":
  main()