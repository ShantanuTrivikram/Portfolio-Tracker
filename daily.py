from mf_code import mf_code
import pandas as pd
import numpy as np
import requests
import json
from mf_code import search_string
from portfolio import *
from cosine import get_cosine

#Filtering only mfs whose last refreshed year is 2021
def relevant_mfs():
    lol = []
    df2 = pd.DataFrame()
    df = pd.read_csv("AMFI_metadata.csv")
    for c in range(len(df)):
        if(df.iloc[c][3][6:10] == "2021"):
            temp = list(df.iloc[c])
            lol.append(temp)
            # df.drop(c)
            # c = c - 1
    df2 = pd.DataFrame(lol, columns = ['id', 'name', 'des', 'last refreshed', 'from', 'to']) 
    df2.to_csv("Relevant_MF.csv")
    return (2)

#Removing similar funds
def filter_mfs():
    lol = []
    df = pd.read_csv("Relevant_MF.csv")
    for c in range(len(df)):
        if(c < (len(df) - 2)):
            if(get_cosine(df.iloc[c][2], df.iloc[c + 1][2]) > 0.90):
                temp = list(df.iloc[c])
                lol.append(temp)
    df2 = pd.DataFrame(lol, columns = ['label', 'id', 'name', 'des', 'last refreshed', 'from', 'to'])
    df2.to_csv("Filtered_Relevant_MF.csv")
    return 1

def rank_mf(q, period):
    mf_with_q = search_string(q)
    mf_list = []
    for mf_nav in mf_with_q:
        growth_stats = {"id": mf_nav["id"], "name": mf_nav["name"], "rate": 0}
        nav_data = mf(mf_nav["id"])
        growth_stats["rate"] = percent_growth(period, nav_data)
        mf_list.append(growth_stats)
    sorted_mf_list = sorted(mf_list, key = lambda i: i['rate'], reverse=True)
    with open('data/' + q + '_' + str(period) + 'days.json', 'w') as f:
        json.dump(sorted_mf_list, f)
    return (1)

rank_mf("ICICI", 30)
rank_mf("ICICI", 365)
rank_mf("ICICI", 730)
rank_mf("ICICI", 1095)
rank_mf("ICICI", 1835)

# relevant_mfs()
# filter_mfs()