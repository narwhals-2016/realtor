import csv
from pprint import pprint
import pandas as pd
import numpy as np
import datetime
import numpy as np
import pandas.io.data as web
import matplotlib.pyplot as plt
import tkinter
# from matplotlib import style
# price <- read.csv("test.csv")
# print('dataframe--',price)

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
	numerator   = round(int(aa)+int(bb))
	denominator = round(int(cc)+int(dd))
	c = round((nunerator/denominator)*100, 2)
	return(c)

# c = get_marital_state_percentage(df_trans["Now married, except separated"],)
#-----------------------------------
list_of_cols = ["Total households",
"Family households (families)",
"With own children under 18 years",
"Nonfamily households",
"Households with one or more people under 18 years",
"Households with one or more people 65 years and over",
"Average household size","Now married, except separated",
"Now married, except separated",
"Nursery school, preschool",
"Elementary school (grades 1-8)",
"High school (grades 9-12)",
"College or graduate school",
"High school graduate or higher",
"Bachelor's degree or higher",
"Native",
"Foreign born"]
#----------------------------------
dataa = {}
dataa = pd.read_csv("testdata.csv")
dataa = dataa[4:]
print('total data--',dataa)

c = dataa['2009-2013 ACS Social Profile'].values
# print('column names--',c)
df = dataa.ix[:,dataa.columns!='2009-2013 ACS Social Profile']
df_trans = df.transpose()
df_trans.columns = c
df_trans.index = ['Estimate','MOE', 'CV','% Estimate', '% MOE']
d = df_trans[list_of_cols]
print('FINAL RESULT---',df_trans)
print('*********************************************************************')
r = {}
c = get_percentage(d['Family households (families)'][0], d['Total households'][0])
r['FamilyHH_percentage'] = c
# print('second item--',d['With own children under 18 years'])
c = get_percentage(d['Nonfamily households'][0], d['Total households'][0])
r['NonFamilyHH_percentage'] = c
c = get_percentage(d['Households with one or more people under 18 years'][0], d['Total households'][0])
r['HH_with_under_18_percentage'] = c
c = get_percentage(d['Households with one or more people 65 years and over'][0], d['Total households'][0])
r['HH_with_over_65_percentage'] = c
c = get_percentage(d['Households with one or more people 65 years and over'][0], d['Total households'][0])
r['HH_with_over_65_percentage'] = c





c = get_percentage(df_trans['Nursery school, preschool'][0], df_trans['Population 3 years and over enrolled in school'][0])
r['Nursery_school_percentage'] = c
c = get_percentage(df_trans["Elementary school (grades 1-8)"][0], df_trans['Population 3 years and over enrolled in school'][0])
r['Elementary_schoolGrades_1_18_percentage'] = c
c = get_percentage(df_trans["High school (grades 9-12)"][0], df_trans['Population 3 years and over enrolled in school'][0])
r['High_school_Grades_9_12_percentage'] = c
c = get_percentage(df_trans["College or graduate school"][0], df_trans['Population 3 years and over enrolled in school'][0])
r['College_or_graduate_school_percentage'] = c
c = get_percentage(df_trans["High school graduate or higher"][0], df_trans['Population 25 years and over'][0])
r['HS_graduate_or_higher_percentage'] = c
c = get_percentage(df_trans["Bachelor's degree or higher"][0], df_trans['Population 25 years and over'][0])
r['Bachelor_degree_or_higher_percentage'] = c
c = get_percentage(df_trans["Same house"][0], df_trans['Population 1 year and over'][0])
r['Same_house_percentage'] = c
print('indexes--', df_trans["Total population"][1,0])
# print('Native--',df_trans["Native"][0],'**',grep("Total population", colnames(df_trans)))
# c = get_percentage(df_trans["Native"][0], df_trans['Total population'][0,0])
# r['Total_population_percentage'] = c
# c = get_percentage(df_trans["Foreign born"][0], df_trans['Total population'][0])
# r['Foriegn_born_percentage'] = c
print('dictionary---',r)
