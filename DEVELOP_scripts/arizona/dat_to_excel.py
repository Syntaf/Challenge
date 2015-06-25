'''
    dat_to_excel.py
    @author: Grant Mercer
    Converts a data file passed with a specific format
    to an excel file
'''

import sys
import os
import csv
import pip
try:
    from xlsxwriter.workbook import Workbook
except ImportError, e:
    pip.main(['install', 'xlsxwriter'])

# If the user does not enter a command line argument after
# the program name, show usage and exit
if len(sys.argv) != 2:
    print "Usage: python dat_to_excel.py <folder>"
    sys.exit()

# Get command line argument passed by user
folder = sys.argv[1]

# For every file in the passed folder
for fname in os.listdir(folder):
    # Open a file
    with open('%s/%s' % (folder,fname)) as f:
        # Get every line that doesn't begin with a '#'
        data = [x.strip('\n') for x in f.readlines() if x[0] != '#']
    data = data[:1] + data[2:]                                  # skip a line
    workbook = Workbook('%s/%s.xlsx' % (folder,fname[:-4])      # open a workbook
    worksheet = workbook.add_worksheet()                        # create a work sheet
    reader = csv.reader(data)                                   # open our data object as a CSV
    for r, row, in enumerate(reader):                           # enumerate over csv
        for c, col in enumerate(row):
            worksheet.write(r, c, col)                          # write line to xlsx
    workbook.close()                                            # close and save xlsx file
