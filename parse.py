# coding: utf-8
'''
Script to read and parse numbers of babies born with different names
'''
import xlrd
book = xlrd.open_workbook('babynamesallyears_tcm77-374773.xls',on_demand=True)

maleData=book.sheet_by_name('Boys')

for v in maleData.row_values(6)[::2]:
    print v
# First entry is the name
# Other entries are numbers born with that name
# in years 2013-1996
