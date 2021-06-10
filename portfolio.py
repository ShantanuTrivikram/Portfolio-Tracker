from mf_code import mf_code
import pandas as pd
import nltk
import numpy as np
import requests
import json
from mf_code import search_string

def real_time_data():
    URL = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=BSE:SBIN&interval=5min&apikey=L4YTVMNNUIQHZ0W1"
    response = requests.get(URL, timeout=3)
    data = json.loads(response.text)
    print("data", data)

def quandl():
    URL = "https://www.quandl.com/api/v3/datasets/BSE/BOM533171.json?api_key=xQrMh6FgVCzY92DxbG3x"
    response = requests.get(URL)
    data = json.loads(response.text)
    print("data", data)

def mf(mfcode):
    
    URL = "https://api.mfapi.in/mf/" + mfcode
    response = requests.get(URL)
    data = json.loads(response.text)
    return data

def plot_stockdata_mf(data):
    nav_values = []
    for i in range(30):
        nav_values.append(data["data"][i]["nav"])
    return (nav_values)

# returns nav of mf x days
def nav_x_days_ago(x, mf_data):
    if(len(mf_data["data"]) > x):
        return float(mf_data["data"][x]["nav"])   
    else:
        return float(0)

def percent_growth(days, mf_data):
    if(nav_x_days_ago(days, mf_data) == float(0)):
        rate = 0
    else:
        rate = (nav_x_days_ago(0, mf_data) - nav_x_days_ago(days, mf_data)) * 100/ nav_x_days_ago(days, mf_data)
    return rate

def rank_mf_categories(q):
    mf_with_q = search_string(q)
    mf_list = []
    for mf_nav in mf_with_q:
        growth_stats = {"id": mf_nav["id"], "name": mf_nav["name"], "rate": 0}
        nav_data = mf(mf_nav["id"])
        growth_stats["rate"] = percent_growth(30, nav_data)
        mf_list.append(growth_stats)
    sorted_mf_list = sorted(mf_list, key = lambda i: i['rate'], reverse=True)
    return (sorted_mf_list)


mfcode = "108466"
# print(nav_x_days_ago(30, mf(mfcode)))
# print(nav_x_days_ago(0, mf(mfcode)))
# print(percent_growth(30, mf(mfcode)))
# q = "Bluechip"
# rank_mf_categories(q)
# real_time_data()
# quandl()
# plot_stockdata_mf(mf())