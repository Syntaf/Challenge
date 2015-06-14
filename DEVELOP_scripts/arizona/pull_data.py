"""
    @author: Grant Mercer
    gmercer015@gmail.com

    This script will connent to the site:
    http://api.mesowest.net/v2/stations/timeseries?token=0b1943fb6da945328d161ea6b64459ce&start
    =200505010000&end=200510310000&vars=air_temp_high_24_hour,air_temp_low_24_hour,relative
    _humidity,sea_level_pressure&units=english&output=csv&obtime=local&STID=____

    and download the data from each station (denoted by STID), the output will be written back
    as YEAR_STID
"""
import os
import re
import string
import shutil
import subprocess
import time
import json
from datetime import datetime, timedelta

# The web address is split up into 3 seperate parts, we'll be injecting the start date, end date
# and station ID to the address api/v2/stations/token&START=...&END=...&vars&STID= 
static_path_start = "http://api.mesowest.net/v2/stations/timeseries?token=f11c52999e0144dcb4461f4fb3ef2b53&start="
static_path_end = "05010000&end="
static_path_STID = "10310000&vars=air_temp_high_24_hour,air_temp_low_24_hour,relative_humidity,sea_level_pressure&units=english&output=csv&obtime=local&STID="

# function to grab all station names from a text file, each appears on one line
def getSTIDS(filename):
    with open(filename) as f:
        # strip each line of any spaces or '\n' so we can directly append the element onto
        # the web address
        stids = [x.translate(string.maketrans("", "", ), " \n") for x in f.readlines()]
    return stids

# if the directory does not exist, create it
stids = getSTIDS("stids.txt")

# create the raw directory if it does not already exist
if not os.path.exists("raw") : os.makedirs("raw")

# for each STATION in our STATIONS list
for stid in stids:
    # append the station name onto the "STID=" portion of the web address
    path_STID = static_path_STID + stid
    # for each year we need data
    for date in range(2005,2015):
        # wget <do not create directories> <output file=raw/date_stationName.dat>
        # website address, with start and end date injected into the address
        proc_wget = "wget -nd -O " + \
                "raw/" + str(date) + "_" + stid + ".dat " + "\"" + \
                static_path_start + str(date) + \
                static_path_end + str(date) + \
                path_STID + "\""
        
        # call wget using os.system()
        os.system(proc_wget)
