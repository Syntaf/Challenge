import json
import pprint

json_data = open("dat.txt").read()

data = json.loads(json_data)

with open("format.dat") as f:
    formatData = [x.strip('\n') for x in f.readlines()]

for station in data["STATION"]:
    for opt in formatData:
        print opt,":",station[opt]
    print ""
