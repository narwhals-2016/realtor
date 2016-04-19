# import csv
import xlrd
import os
# from pprint import pprint
import pandas as pd
import numpy as np
import datetime
import numpy as np
import pandas.io.data as web
# import matplotlib.pyplot as plt
# import tkinter
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from tables.models import SchoolEducation, Demographic, Neighborhood

def get_percentage(var1, var2):
    c = round((int(var1)/int(var2))*100, 2)
    return(c)


def get_marital_state_percentage(var1, var2,var3,var4):
    numerator   = int(var1)+int(var2)
    denominator = int(var3)+int(var4)
    c = round((numerator/denominator)*100, 2)
    return(c)


def get_school_percentage(var1,var2,var3,var4):
    numerator   = int(var1)+int(var2)+int(var3)
    c = round((numerator/int(var4))*100, 2)
    return(c)

def insert_row_in_education_table(r):

    try:
        item =  Neighborhood.objects.get(name=r['neighborhood'])
        SchoolEducation.objects.create(neighborhood=item,
                   school_enrollment_pre_highschool = r['school_enrollment_pre_highschool'],
                   school_enrollment_highschool = r['HS_Grades_9_12_percentage'],
                   school_enrollment_college = r['College_or_graduate_percentage'],
                   education_highschool_over = r['HS_graduate_or_higher_percentage'],
                   education_college_over = r['Bachelor_degree_or_higher_percentage'])
    except:
        print('item not found+++++',r['neighborhood'])


def insert_row_in_demographic(r):

    try:
        item =  Neighborhood.objects.get(name=r['neighborhood'])
        Demographic.objects.create(neighborhood=item,
                   married = r['Married_percentage'],
                   divorced= r['Divorced_percentage'],
                   one_yr_turnover = r['Same_house_percentage'],
                   birth_native = r['Native_population_percentage'],
                   birth_foreign = r['Foreign_born_percentage'],
                   gender_m = 58.00,
                   gender_f = 42.00)
    except:
        print('item not found+++++',r['neighborhood'])


def insert_into_db(r):
    insert_row_in_education_table(r)
    insert_row_in_demographic(r)



#-----------------------------------
def CalculateValues(r, dataa, c):
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
    df = dataa.ix[:,dataa.columns!='2009-2013 ACS Social Profile']
    df_trans = df.transpose()
    df_trans.columns = c
    df_trans.index = ['Estimate','MOE', 'CV','% Estimate', '% MOE']
    d = df_trans[list_of_cols]

  
    r['FamilyHH_percentage'] = get_percentage(d['Family households (families)'][0],
                               d['Total households'][0])

    d1 = d["With own children under 18 years"]
    nd = np.array(d1)
    r['Children_under_18_percentage'] = get_percentage(nd[0][0], d['Total households'][0])

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
    r['Married_percentage'] = get_marital_state_percentage(md[0][0], md[0][1],
                                                          d['Males 15 years and over'][0],
                                                          d['Females 15 years and over'][0])
    r['Divorced_percentage'] = 100 - int(r['Married_percentage'])


    r['school_enrollment_pre_highschool'] = get_school_percentage(d['Nursery school, preschool'][0],
                                              d['Kindergarten'][0],
                                              d["Elementary school (grades 1-8)"][0],
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

    insert_into_db(r)


def extract_transform_social_data(folder, fname):

    dataa = {}
    r = {}
    file_path = 'tables/datasets/' + folder + '/' + fname
    dataa = pd.read_excel(file_path, sheetname=0)
    c = dataa['2009-2013 ACS Social Profile'].values
    r['neighborhood'] = c[0][23:]
    if (r['neighborhood'] != "Rikers Island"):
        CalculateValues(r, dataa, c)
    else:
        print('****Rikers ****')
    
def run(folder):

    list_of_files = os.listdir('tables/datasets/' + folder)
    for f in list_of_files:
        extract_transform_social_data(folder, f)

