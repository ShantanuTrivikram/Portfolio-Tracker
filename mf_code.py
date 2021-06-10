import pandas as pd
codes = {}
codes_list = []
def mf_code():  
    df = pd.read_csv("Filtered_Relevant_MF.csv")
    for c in range(len(df)):
        temp_dict = {"id": "", "name": ""}
        codes[df.iloc[c][1]] = str(df.iloc[c][0])
        temp_dict["id"] = str(df.iloc[c][1])
        temp_dict["name"] = df.iloc[c][2]
        codes_list.append(temp_dict)
    # print("MF_code")
    return codes_list





def ret_codes(mf_name):
    if(not bool(codes)):
        mf_code()
    return codes[mf_name]

def search_string(q):
    codes_with_searchstring = []
    for mf in codes_list:
        if(q.lower() in mf["name"].lower()):
            codes_with_searchstring.append(mf)

    return codes_with_searchstring

#Initialize the dict so that the readExcel code doesnt run always
if(not bool(codes)):
    mf_code()

mf_name = "ICICI Prudential Mutual Fund - ICICI Prudential Bluechip Fund - Growth"
# print(ret_codes(mf_name))

# q = "Bluechip"
# list1 = search_string(q)
# print(len(list1))




