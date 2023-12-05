import pandas as pd 
import requests
from requests import get
import json
from ip2geotools.databases.noncommercial import DbIpCity
from dotenv import load_dotenv
import os
import matplotlib as plt

class BLS():
    def __init__(self, interest):
        self.interest = interest
        self.interest_Series = None
        self.ip = None
        self.location = None
        self.data = None

    def set_location(self):
        self.ip = get('https://api.ipify.org').content.decode('utf8')
        self.location = DbIpCity.get(ip, api_key="free")
        # this method will get the user’s location
    
    def set_interest_Series(self):
        codes = pd.read_csv("cpi_item_codes.csv")
        descriptions = codes['item_name'].tolist()
        series_codes = codes['item_code'].tolist()
        relevant_codes = []
        for i in range(len(descriptions)):
        if self.interest in descriptions[i]:
            if "less" not in descriptions[i]:
                relevant_codes.append(series_codes[i])
        self.interest_Series = relevant_codes

    def get_api_key(self):
        # instruct user to make .env file to store in format API_KEY=29374af23 first. Then run this function automatically upon instantiation of class
        load_dotenv()
        api_key = os.getenv("API_KEY")
        return api_key

    def get_request(self, api_key, start_year, end_year, series_list):
        headers = {
            'content-type': 'application/json',
        }
        payload = json.dumps({"seriesid": series_list,
                    "startyear": start_year,
                    "endyear": end_year,
                    "catalog": "false",
                    "registrationkey": api_key
                    })
        response_bls = requests.post("https://api.bls.gov/publicAPI/v2/timeseries/data", data=payload, headers=headers)
        print(response_bls.text)

    def error_handling(self, response):
        if response["status"] == "REQUEST_FAILED":
            print("Request failed.")
            return
        elif response["status"] == "REQUEST_SUCCEEDED":
            print("Request succeeded.")
        return
        error_handling(self, response_bls)
        return response_bls

    def summary_stats(self, col_name):
        min_val = self.data[col_name].min
        max_val = self.data[col_name].max
        mean_val = self.data[col_name].mean()
        std_dev = self.data[col_name].std()

        print("Minimum Value:", min_val)
        print("Maximum Value:", max_val)
        print("Mean Value:", mean_val)
        print("Standard Deviation:", std_dev)
  
    def visualizer(self, x_var, y_var):
        plt.plot(x_var, y_var)
        plt.show()

def main():
    test = BLS("food")
    api_key = test.get_api_key()
    test.set_interest_Series()
    print(test.interest_Series)
    test.get_request(api_key, 2013, 2014, ['CUUR0000SA0','SUUR0000SA0'])


if __name__=="__main__":
  main()