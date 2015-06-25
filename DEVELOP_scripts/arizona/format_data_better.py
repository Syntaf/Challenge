import json
import pprint

# load the file from dat.txt
json_data = open("dat.txt").read()

# using the jason parser to turn the list into a dictionary
data = json.loads(json_data)

# format.dat is used to format the output
with open("format.dat") as f:
    formatData = [x.strip('\n') for x in f.readlines()]

# for each station in the entire data set
for station in data["STATION"]:
    for opt in formatData:
        print opt,":",station[opt]
    print ""
