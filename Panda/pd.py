import pandas as pd
import argparse

split_parameter = ","

parser = argparse.ArgumentParser()

# parser.add_argument("-m", "--mtime", help="Print the time of last file modification") # ha1.py -m a.txt

# parser.add_argument("-s", "--size", help="Print the size of file in MB") # ha1.py -s a.txt

# # parser.add_argument("--rename", help="Change file name to B", action="store", type=str, default="hw", nargs="=", metavar=None)

parser.add_argument("--input", help="Something") # ha1.py --rename B a.txt

parser.add_argument("--columns", help="Something") # ha1.py --rename B a.txt

parser.add_argument("--query", help="Something") # ha1.py --rename B a.txt

parser.add_argument("--output", help="Something") # ha1.py --rename B a.txt

args = parser.parse_args()

if args.input:
	data = pd.read_csv(args.input)
if args.columns:
	args.columns = args.columns.replace(" ", "")
	columns = args.columns.split(split_parameter)
if args.query:
	try:
		query = data.query(args.query)
		rows = query.shape[0]
		df = query.loc[0:rows, columns]
		pass
	except Exception as e:
		print (e)
if args.output:
	f = open(args.output, "w+")
	content = df.to_csv(index=False)
	f.write(content)
	f.close()


