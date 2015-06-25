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

if len(sys.argv) != 2:
    print "Usage: python dat_to_excel.py <folder>"
    sys.exit()

folder = sys.argv[1]

for fname in os.listdir(folder):
    with open('%s/%s' % (folder,fname)) as f:
        data = [x.strip('\n') for x in f.readlines() if x[0] != '#']
    data = data[:1] + data[2:]
    csvfile = '%s/%s' % (folder,fname[:-4])
    workbook = Workbook(csvfile + '.xlsx')
    worksheet = workbook.add_worksheet()
    reader = csv.reader(data)
    for r, row, in enumerate(reader):
        for c, col in enumerate(row):
            worksheet.write(r, c, col)
    workbook.close()
