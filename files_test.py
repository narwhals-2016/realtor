import os
import pandas as pd



def demo(filename):
	demo_csv = pd.read_csv(filename, skiprows=[2,3], converters={'Unnamed: 1': lambda x: x.replace(',','')})
	indexed = demo_csv.set_index('2009-2013 ACS Demographic Profile')
	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = indexed.index[0]
	neighborhood = neighborhood_string[23:]
	under_nineteen = sum([
		int(indexed.loc['Under 5 years'][0]),
		int(indexed.loc['5 to 9 years'][0]),
		int(indexed.loc['10 to 14 years'][0]),
		int(indexed.loc['15 to 19 years'][0])
	])
	print(neighborhood, under_nineteen)

file_list = os.listdir('demo_csv_files/')
for file in file_list:
	demo('demo_csv_files/' + file)