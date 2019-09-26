import pandas as pd
import argparse

split_parameter = ","

parser = argparse.ArgumentParser()

#python3.7 -i pd.py --input="train.csv" --output="output.csv" --query='Sex == "female" & Survived == 1' --columns="Survived, Sex"

parser.add_argument("--input", help="--input_file input csv file name") 

parser.add_argument("--columns", help="--columns list of columns to select from input csv file") 

parser.add_argument("--query", help="--query query string to apply") 

parser.add_argument("--output", help="--output_file output csv file name") 

args = parser.parse_args()

pas = True

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
		pas = False
if args.output:
	if pas:
		f = open(args.output, "w+")
		content = df.to_csv(index=False)
		f.write(content)
		f.close()


