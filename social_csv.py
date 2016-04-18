import csv
from pprint import pprint
import pandas as pd
import numpy as np
import datetime
import numpy as np
import pandas.io.data as web
import matplotlib.pyplot as plt
import tkinter

def get_percentage(var1, var2):
	aa = var1.replace(',','')
	bb = var2.replace(',','')
	c = round((int(aa)/int(bb))*100, 2)
	return(c)


def get_marital_state_percentage(var1, var2,var3,var4):
	aa = var1.replace(',','')
	bb = var2.replace(',','')
	dd = var3.replace(',','')
	ee = var4.replace(',','')
	numerator   = int(aa)+int(bb)
	denominator = int(dd)+int(ee)
	c = round((numerator/denominator)*100, 2)
	return(c)

def get_school_percentage(var1, var2,var3):
	aa = var1.replace(',','')
	bb = var2.replace(',','')
	dd = var3.replace(',','')
	numerator   = int(aa)+int(bb)
	c = round((numerator/int(dd))*100, 2)
	return(c)


#-----------------------------------
list_of_cols = ["Total households",
"Family households (families)",
"With own children under 18 years",
"Nonfamily households",
"Households with one or more people under 18 years",
"Households with one or more people 65 years and over",
"Average household size",
"Males 15 years and over",
"Now married, except separated",
"Females 15 years and over",
"Now married, except separated",
"Population 3 years and over enrolled in school",
"Nursery school, preschool",
"Kindergarten",
"Elementary school (grades 1-8)",
"High school (grades 9-12)",
"College or graduate school",
"Population 25 years and over",
"High school graduate or higher",
"Bachelor's degree or higher",
"Population 1 year and over",
"Same house",
"Total population",
"Native",
"Foreign born"]
#----------------------------------
dataa = {}
dataa = pd.read_csv("testdata.csv")[4:]

c = dataa['2009-2013 ACS Social Profile'].values
df = dataa.ix[:,dataa.columns!='2009-2013 ACS Social Profile']
df_trans = df.transpose()
df_trans.columns = c
df_trans.index = ['Estimate','MOE', 'CV','% Estimate', '% MOE']
d = df_trans[list_of_cols]

r = {}
r['FamilyHH_percentage'] = get_percentage(d['Family households (families)'][0],
						   d['Total households'][0])

d1 = d["With own children under 18 years"]
nd = np.array(d1)
r['Children_under_18_percentage'] = get_percentage(nd[0][0], d['Total households'][0])
# print('array n--',nd[0][0])
r['NonFamilyHH_percentage']= get_percentage(d['Nonfamily households'][0],
							 d['Total households'][0])

r['HH_with_under_18_percentage'] = get_percentage(d['Households with one or more people under 18 years'][0],
								   d['Total households'][0])

r['HH_with_over_65_percentage'] = get_percentage(d['Households with one or more people 65 years and over'][0],
								  d['Total households'][0])
 
r['HH_with_over_65_percentage']= get_percentage(d['Households with one or more people 65 years and over'][0], 
								 d['Total households'][0])

m = d["Now married, except separated"]
md = np.array(m)
r['Population_married_except_separated_percentage'] = get_marital_state_percentage(md[0][0], md[0][1],
													  d['Males 15 years and over'][0],
													  d['Females 15 years and over'][0])


r['Nursery_to_kindergarten_percentage'] = get_school_percentage(d['Nursery school, preschool'][0],
										  d['Kindergarten'][0],
										  d['Population 3 years and over enrolled in school'][0])


r['Elementary_Grades_1_18_percentage'] = get_percentage(d["Elementary school (grades 1-8)"][0],
											   d['Population 3 years and over enrolled in school'][0])

r['HS_Grades_9_12_percentage'] = get_percentage(d["High school (grades 9-12)"][0], 
									d['Population 3 years and over enrolled in school'][0])

r['College_or_graduate_percentage'] = get_percentage(d["College or graduate school"][0],
									 d['Population 3 years and over enrolled in school'][0])

r['HS_graduate_or_higher_percentage'] = get_percentage(d["High school graduate or higher"][0], 
										d['Population 25 years and over'][0])

r['Bachelor_degree_or_higher_percentage'] = get_percentage(d["Bachelor's degree or higher"][0], 
											d['Population 25 years and over'][0])
r['Same_house_percentage']= get_percentage(d["Same house"][0],
							 d['Population 1 year and over'][0])

t = d["Total population"]
td = np.array(t)
r['Native_population_percentage'] = get_percentage(d["Native"][0], td[0][0])
r['Foreign_born_percentage'] = get_percentage(d['Foreign born'][0], td[0][0])

print('dictionary---',r)
