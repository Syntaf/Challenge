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
from datetime import datetime, timedelta

static_path_start = "http://api.mesowest.net/v2/stations/timeseries?token=0b1943fb6da945328d161ea6b64459ce&start="
static_path_end = "05010000&end="
static_path_STID = "10310000&vars=air_temp_high_24_hour,air_temp_low_24_hour,relative_humidity,sea_level_pressure&units=english&output=csv&obtime=local&STID="

bad_chars = '(){}"<>[] '     # characers we want to strip from the string
key_map = []

def getSTIDS(filename):
    with open(filename) as f:
        stids = [x.translate(string.maketrans("", "", ), " \n") for x in f.readlines()]
    return stids

# if the directory does not exist, create it
stids = getSTIDS("stids.txt")

if not os.path.exists("raw") : os.makedirs("raw")
if not os.path.exists("formatted") : os.makedirs("formatted")

# format file
with open("format.dat") as f:
    formatData = [x.strip('\n') for x in f.readlines()]

for stid in stids:
    path_STID = static_path_STID + stid
    # grab data for each day
    for date in range(2005,2015):
        proc_wget = "wget -nd -O " + \
                "raw/" + str(date) + "_" + stid + ".dat " + \
                static_path_start + str(date) + \
                static_path_end + str(date) + \
                path_STID
        
        print proc_wget
        """
        p = subprocess.Popen(proc_wget, shell=True)
        p.wait()
        #os.system(proc_wget)
        """
        #time.sleep(.25)

        """
        # parse file
        with open(os.path.join("raw", str(date) + "_" + stid + ".dat")) as f:
            data = f.read()
            data = data.strip('\n')
            data = re.split('}|\[{', data)


        data = filter(len, data)

        # strip and split each station
        for dat in data[1:-1]:
            # perform black magic, don't even try to understand this
            dat = dat.translate(string.maketrans("", "", ), bad_chars).split(',')
            key_map.append(dict(x.split(':') for x in dat if ':' in x ))
            if ':' not in dat[1]:key_map['NAME']+=dat[1]

        print key_map
        with open(os.path.join("formatted", str(date) + "_" + stid + ".dat"), 'w+') as of:
            for station in range(0, len(key_map)):
                for opt in formatData:
                    of.write(opt + ":" + key_map[station][opt] + "\n")
        """






