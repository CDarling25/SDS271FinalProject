import pandas as pd
import requests
from requests import get
import json
from ip2geotools.databases.noncommercial import DbIpCity
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
from IPython.display import display


class BLS():
    def __init__(self, interest):
        def get_api_key(self):
            load_dotenv()
            api_key = os.getenv("API_KEY")
            return api_key

        self.api_key = get_api_key(self)
        self.interest = interest
        self.interest_Series = None
        self.location = None
        self.data = None
        self.startyear = None
        self.endyear = None

    def set_interest_Series(self):
        codes = pd.read_csv("cpi_item_codes.csv")
        # item_name contains information on topic of series
        descriptions = codes['item_name'].tolist()
        series_codes = codes['item_code'].tolist()
        relevant_codes = []
        # store series codes with topics relevant to user interest into list
        for i in range(len(descriptions)):
            if self.interest in descriptions[i]:
                if "less" not in descriptions[i]:
                    series_code = "CUUR0000" + series_codes[i]
                    relevant_codes.append(series_code)
        self.interest_Series = relevant_codes

    def get_request(self, start_year, end_year, series_list = None):
        self.startyear = start_year
        self.endyear = end_year
        # if-else statement sets series list to relevant series of interest, or, if user specifies series manually, sets series list to specified series
        if series_list is None:
            series_list = self.interest_Series
        else:
            self.interest_Series = series_list
        headers = {
            'content-type': 'application/json',
        }
        payload = json.dumps({"seriesid": series_list,
                              "startyear": start_year,
                              "endyear": end_year,
                              "catalog": "false",
                              "registrationkey": self.api_key
                              })
        response_bls = requests.post("https://api.bls.gov/publicAPI/v2/timeseries/data", data=payload, headers=headers)
        json_data = response_bls.json()

        if 'Results' in json_data and 'series' in json_data['Results']:
            data_series = json_data['Results']['series']
            df_list = []
            # store each series as a dataframe in a master list
            for series in data_series:
                df = pd.DataFrame(series['data'])
                df=df.iloc[::-1].reset_index(drop=True)
                df = df.iloc[:, 0:4]
                df_list.append(df)
            self.data = df_list

    def error_handling(self, response):
        if response["status"] == "REQUEST_FAILED":
            print("Request failed.")
            return
        elif response["status"] == "REQUEST_NOT_PROCESSED":
            print("Request not processed. You may have reached your daily limit of requests for the day.")
            return
        elif response["status"] == "REQUEST_SUCCEEDED":
            print("Request succeeded.")
        return
        error_handling(self, response_bls)
        return response_bls

    def summary_stats(self):
        for index,df in enumerate(self.data):
            df["value"] = pd.to_numeric(df["value"])
            min_val = df["value"].min()
            max_val = df["value"].max()
            mean_val = df["value"].mean()
            std_dev = df["value"].std()
            summary_df = pd.DataFrame({'Series': [self.interest_Series[index]], 'Minimum': [min_val], 'Maximum': [max_val], 'Mean': [mean_val], 'Standard Deviation': [std_dev]})
            display(summary_df)

    def visualizer(self):
        for index,df in enumerate(self.data):
            df["value"] = pd.to_numeric(df["value"])
            plt.plot(df["value"])
            plt.xlabel(f"Month in Time Period {self.startyear} to {self.endyear}")
            plt.ylabel("Consumer Price Index")
            plt.title(f"Change in Consumer Price Index of Series {self.interest_Series[index]} Over {self.startyear} to {self.endyear}")
            plt.show()


