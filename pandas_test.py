import csv
import pandas as pd
import numpy as np

exl = pd.ExcelFile('practice.xlsx')
# gets the first sheet name in the excel 
test = exl.parse(exl.sheet_names[0])

print(test[4:])
