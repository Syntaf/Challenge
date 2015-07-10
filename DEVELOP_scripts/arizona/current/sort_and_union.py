"""
    sort_and_union
    @author: Grant Mercer
    Opens all files in a given directory, sorts those
    files by they're LAST column. Prints those top 200
    values to a new csv file and unions
"""

import os
import sys
import csv
import operator

def files(path):
    """
    Yield function for listing only FILES in directories
    """
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

# Check, did the user specify a command line argument?
if len(sys.argv) != 2:
    # If the user did not (e.g. there are not two command line
    # arguments) , print the usage statement and end the
    # program
    print "Usage: python sort_and_union.py <folder>"
    sys.exit()

# Set the folder to the passed command line argument
folder = sys.argv[1]

# Create an 'out' dir if it does not currently exist
if not os.path.exists('out'):
    os.makedirs('out')

# For EACH file in the folder
for fname in files(folder):
    # Open the file
    with open('%s/%s' % (folder, fname)) as f:
        # Read and sort the file
        reader = csv.reader(f, delimiter=",")
        sortedlist = sorted(reader, key=operator.itemgetter(-1), 
                            reverse=True)
        # Write the first 200 values to a seperate CSV file
        with open('out/%s' % fname, 'w+') as of:
            writer = csv.writer(of, delimiter=",")
            # Loop 200 times, write 200 rows
            for r in range(0, 200):
                writer.writerow(sortedlist[r])

union_string = ''
# For EACH file in the generated folder
for out_fname in files('out'):
    union_string += out_fname + ' #;'

union_string = union_string[:-1]
print union_string
