import pandas as pd
import os
import sys
import asyncio
ROT_DIR= os.path.abspath(os.curdir)
sys.path.append(ROT_DIR)
from Pheonix.client_api import clientAPI  
import json
from collections import deque

print(ROT_DIR)
var=json.loads(open(ROT_DIR+"\meteo\settings\\api_info.json",'r').read())
var=var["vars"]

if __name__ == "__main__":
    api=clientAPI("https://archive-api.open-meteo.com/v1/archive")
    
    result=asyncio.get_event_loop().run_until_complete(api.fetch_all(variables=var,horizon=10,model="gfs",start_date="2025-01-25",end_date="2025-02-08",longtitude=0,latitude=0)) 
    hourly = pd.DataFrame(result["hourly"])
    hourly_unit = pd.DataFrame.from_dict(result["hourly_units"], orient="index", columns=["Unit"])
    print(hourly_unit)
    hourly["latitude"]=result["latitude"]
    hourly["longitude"]=result["longitude"]
    hourly["elevation"]=result["elevation"]
    hourly["timezone"]=result["timezone"]
    column_list=hourly.columns.tolist()
    column_list= [column_list[0]] + column_list[-4:] + column_list[1:-4]
    hourly=hourly[column_list]
    print(hourly)
