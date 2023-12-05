import pandas as pd 
import requests
from requests import get
import json
from ip2geotools.databases.noncommercial import DbIpCity
#from dotenv import load_dotenv
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
          if "Series does not exist" in response:
              print("Error")
          elif "REQUEST_FAILED" in response:
              print("Request failed, error 404")
          else:
              print("worked")
      error_handling(self, response_bls)
      return

def main():
    test = BLS("food")
    #api_key = test.get_api_key()
    test.set_interest_Series()
    print(test.interest_Series)
    #test.get_request(api_key, 2013, 2014, ['CUUR0000SA0','SUUR0000SA0'])


if __name__=="__main__":
  main()