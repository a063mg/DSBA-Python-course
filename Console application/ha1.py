import os, time
import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mtime", help="Print the time of last file modification") # ha1.py -m a.txt

parser.add_argument("-s", "--size", help="Print the size of file in MB") # ha1.py -s a.txt

# parser.add_argument("--rename", help="Change file name to B", action="store", type=str, default="hw", nargs="=", metavar=None)

parser.add_argument("--rename", help="Something", nargs=2, metavar=None) # ha1.py --rename B a.txt

args = parser.parse_args()

if args.mtime:
	st = os.stat(args.mtime)
	print("last modified: %s" % time.ctime(st.st_mtime))
if args.size:
	st = os.stat(args.size)
	print("the size of file is: %s" % (st.st_size/2**20),"MB")
if args.rename:
	file = args.rename[1]
	name = args.rename[0]+"."+args.rename[1].split(".")[1]
	os.rename(file, name)
	print("Renamed successfully")
