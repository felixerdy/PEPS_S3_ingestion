import os
from extend import *

print "Starting downloading images for bbox:", lonmin, lonmax, latmin, latmax

runString = "./peps_download.py -c S1 --lonmin %s --lonmax %s --latmin %s --latmax %s -d %s -f %s" % (lonmin, lonmax, latmin, latmax, start_date, end_date)

os.system(runString)
