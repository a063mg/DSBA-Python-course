import os, time
import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mtime", help="Print the time of last file modification", action="store_true")

parser.add_argument("-s", "--size", help="Print the size of file in MB", action="store_true")

# parser.add_argument("--rename", help="Change file name to B", action="store", type=str, default="hw", nargs="=", metavar=None)

parser.add_argument("--rename", help="Something")

args = parser.parse_args()

file = input()

st = os.stat(file)

if args.mtime:
	print("last modified: %s" % time.ctime(st.st_mtime), args.mtime)
if args.size:
	print("the size of file is: %s" % (st.st_size/2**20),"MB")
if args.rename:
	os.rename(file, args.rename)
	print("Renamed successfully")
