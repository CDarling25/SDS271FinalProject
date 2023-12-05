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

    def get_request(self, api_key, start_year, end_year, series_list):
        payload = {"seriesid": series_list,
                   "startyear": start_year,
                   "endyear": end_year,
                   "catalog": "false",
                   "registrationkey": f"{api_key}"
                   }
        response = requests.post("https://api.bls.gov/publicAPI/v2/timeseries/data", data=payload)
        def error_handling(self, response):
            if "Series does not exist" in response:
                print("Error")
            elif "REQUEST_FAILED" in response:
                print("Request failed, error 404")
                return
        error_handling(response)
        return

def main():
    test = BLS("food")
    api_key = test.get_api_key()
    test.set_interest_Series()
    # can't figure out why it's only returning one series' data
    payload = {"seriesid":["CUUR0000SA0", "SUUR0000SA0"],

"startyear":"2018",   "endyear":"2018",  "catalog":True,

"calculations":True,  "annualaverage":True, "aspects":True,

"registrationkey":f"{api_key}"}


    response = requests.post("https://api.bls.gov/publicAPI/v2/timeseries/data", data = payload)

    print(response.text)

    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip))
    res = DbIpCity.get(ip, api_key="free")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(pd.read_csv("cpi_item_codes.csv"))
if __name__=="__main__":
  main()