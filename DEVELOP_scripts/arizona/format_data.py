"""
    @author: Grant Mercer
    gmercer015@gmail.com

    Script designed to read in a data file of a specific format as
    dat.txt shows, and display information on each station formatted
    according to format.dat . 
"""
import re
import string
from itertools import groupby

bad_chars = '(){}"<>[] '     # characers we want to strip from the string
key_map = []

# parse file
with open("dat.txt") as f:
    data = f.read()
    data = data.strip('\n')
    data = re.split('}|\[{', data)

# format file
with open("format.dat") as f:
    formatData = [x.strip('\n') for x in f.readlines()]

data = filter(len, data)

# strip and split each station
for k in range(1, len(data)-1):
    # perform black magic, don't even try to understand this
    dat = filter(None, data[k].translate(string.maketrans("", "", ), bad_chars).split(','))
    key_map.append(dict(x.split(':') for x in dat if ':' in x))
    if ':' not in dat[4] : key_map[k-1]['NAME']+=str(", " + dat[4])


for station in range(0, len(key_map)):
    for opt in formatData:
        print opt,":",key_map[station][opt]
    print ""



