import os
import sys
import csv
import operator

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

if len(sys.argv) != 2:
    print "Usage: python sort_and_union.py <folder>"
    sys.exit()

folder = sys.argv[1]
if not os.path.exists('out'):
    os.makedirs('out')

for fname in files(folder):
    with open('%s/%s' % (folder, fname)) as f:
        reader = csv.reader(f, delimiter=",")
        sortedlist = sorted(reader, key=operator.itemgetter(-1), 
                            reverse=True)
        with open('out/%s' % fname, 'w+') as of:
            writer = csv.writer(of, delimiter=",")
            for r in range(0, 200):
                writer.writerow(sortedlist[r])
        break;
