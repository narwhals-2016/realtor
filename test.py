import pandas as pd
import decimal
D = decimal.Decimal
housing_csv = pd.read_csv(
	'housing-middle-village.csv', 
	skiprows=[1,2,3,4], 
	converters={'Unnamed: 1': lambda x: x.replace(',','')}
)

print(housing_csv)
