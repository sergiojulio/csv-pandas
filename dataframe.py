import sys
import pandas as pd
"""Pandas con Unit Testing"""


def main(file: str) -> str:
    	
	print(file)

	df = pd.read_csv(file)
	limit = 1000
	pd.set_option("display.max_rows",limit)
	
	print(df)


if __name__ == "__main__":
	main(sys.argv[1])

	#print('Number of arguments:', len(sys.argv), 'arguments.')
	#print('Argument List:', str(sys.argv))


