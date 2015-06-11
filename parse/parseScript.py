import re
import string

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
for dat in data[1:-1]:
    # perform black magic, don't even try to understand this
    dat = dat.translate(string.maketrans("", "", ), bad_chars).split(',')
    key_map.append(dict(x.split(':') for x in dat if ':' in x ))
    if ':' not in dat[1]:key_map['NAME']+=dat[k][1]


for station in range(0, len(key_map)):
    for opt in formatData:
        print opt,":",key_map[station][opt]
    print ""



