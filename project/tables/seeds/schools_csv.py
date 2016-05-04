import csv
import os
from decimal import Decimal
from pprint import pprint
import pandas as pd
import numpy as np
from tables.seeds.mappings.mappings import nb_zip
from tables.models import School, Neighborhood
 

def extract_transform_school_data(folder_path, fname, nb_zip, r):

    list_of_cols = ["School Name","Enrollment",
                    "Student Achievement Rating",
                    "Rigorous Instruction Rating"]
    dataa = {}
    dataa = pd.read_excel(fname, sheetname=0)
    index = dataa.iloc[0]

    school_type = fname.split('/')[-1].split('_')[2]
    if school_type == "HS":
        c = dataa['2014-15 School Quality Report for High Schools'].values[1:]
    elif school_type == "EMS":
        c = dataa['2014-15 School Quality Report for Elementary, Middle, and K-8 Schools'].values[1:]
        
    df_trans = dataa[1:].transpose()   
    df_trans.columns = c
    df_trans.index = index.values 

    all_schools_directory =  folder_path + '15-16SchoolDirectory.xlsx' 
    # for every school get the typr, addr and zipcode from all schools directory(master directory)
    addr_zip_dictionary = get_zip_codes_from_all_schools_directory(all_schools_directory, c) 
     
    number_success=0
    unsuccess = 0           
    for school, addr_and_zip in addr_zip_dictionary.items():     
        temp=[]

        zipcode = addr_and_zip[2] 
        obj = df_trans[school]
        en = 'Enrollment'
        try:
            number_success = number_success +1
            enrol = obj[en]
        except:
            enrol = 0
            unsuccess + unsuccess + 1
            # print('obj:', obj[school])
            print('***********&&&&&&&&&**************************')
        rt = "Rigorous Instruction Rating"
        try:
            rigor = obj[rt]
        except:
            rigor = 0            
        sa = 'Student Achievement Rating'
        try:
            student_achievemet = obj[sa]
        except:
            student_achievemet = 0                        

        score =  calculate_score(enrol, rigor, student_achievemet)                        
        for nb, vals in nb_zip.items():
            if str(zipcode) in vals:
                temp = [school,
                        addr_and_zip[0],
                        score,
                        # addr_and_zip[1],
                        str(zipcode)]
                r[nb].append(temp)

    # print('success: ', number_success, 'unsuccess: ',unsuccess)
    return(c)
    
def calculate_score(n1, n2, n3):
#  n1 = enrollment, n2 = Rigorous Instruction Rating,  n3 = Student Achievement Rating    
    score = 0
# if  enrollment is < 250 score =5, between 250 and 500 score =4 ...
    if (int(n1) < 250):
        score =+ 5
    elif ((int(n1) > 250) and (int(n1) < 500 )):
        score =+ 4
    elif ((int(n1) > 500) and (int(n1) < 750 )):
        score =+ 3
    elif ((int(n1) > 750) and (int(n1) < 1000 )):
        score =+ 2
    else: 
        score =+ 1
# if instruction rigor rating is exceeding target then score =5 ... 

    if (n2 == 'Exceeding Target'):
        score =+ 5
    elif (n2 == 'Meeting Target'):
        score =+ 4
    elif (n2 == 'Approaching Target'):
        score =+ 3
    elif (n2 == 'Not Meeting Target'):
        score =+ 2
    else: 
        score =+ 1
# if student achievementrating is exceeding target then score =5 ... 
    if (n3 == 'Exceeding Target'):
        score =+ 5
    elif (n3 == 'Meeting Target'):
        score =+ 4
    elif (n3 == 'Approaching Target'):
        score =+ 3
    elif (n3 == 'Not Meeting Target'):
        score =+ 2
    else: 
        score =+ 1

    return(score)

def initialize_dict(nb_zip, r):
# initialize the dictionary r with keys from nb_zip(list of neighborhoods) 
    for key in nb_zip:
        r[key] = []

def change_format_of_name(school):
# this is to take care of different format of chool-names between two files  
    s1 = school     
    if school[4:4] == ' ':  
        if school[:3] == 'P.S':
            num = int(school[5:].split(' ')[0])
            s1 = 'PS '+str(num)+school[8:]
    return(s1) 


def get_zip_codes_from_all_schools_directory(fname1,lst):
 # fname1 is the DOE directory with 7000+ school names and addresses, lst is list of elementary and middle schools 
    dataa = pd.read_excel(fname1, sheetname=0)
    index = dataa.iloc[0]
    dataa.columns = index.index

    lst1 = pd.Series(lst)    
    zip_df = dataa[["LEGAL NAME","GRADE ORGANIZATION DESCRIPTION","MAILING ADDRESS","ZIP"]]
    rows = zip_df["LEGAL NAME"].values
    zip_df.index = rows    

    not_found_count = 0
    elm_addr_zip_dict = {}
    for school in lst:
        name = change_format_of_name(school)
        school_uppercase = name.upper()       
        if school_uppercase in zip_df.index:
            elm_addr_zip_dict[school] = [zip_df.loc[school_uppercase]["GRADE ORGANIZATION DESCRIPTION"],
                                         zip_df.loc[school_uppercase]["MAILING ADDRESS"], 
                                         zip_df.loc[school_uppercase]["ZIP"].astype(int)]
        else:
            not_found_count += 1
            elm_addr_zip_dict[school] = ['Type not found','Addr not found', 'Zip not found']

    return(elm_addr_zip_dict)


def get_3_scores(detail_list, neighborhood):
# schoolType : Pre-K Only,Elementary,Middle School,Junior High School,Junior Senior School,
#              Senior High,Special School, K-12 School,NA, Other
# each item(list) in detail_list has school, schoolType, score, address and zip
    lst = []
    k_school_score = ms_school_score = hs_school_score = 0
    ms_school_count = hs_school_count = 0
    if len(detail_list) > 0:
        for i in range(0, len(detail_list)):
            if (detail_list[i][1] in ('Pre-K Only', 'DOE', 'CHARTER','NYCEEC')):
                k_school_score = k_school_score + 1
            elif (detail_list[i][1]  in ('Elementary','Middle School')):
                ms_school_score = ms_school_score + detail_list[i][2]
                ms_school_count += 1
            elif (detail_list[i][1] in  ('K-12 School', 'Junior High School', 
                                         'Junior Senior School','Senior High')):
                hs_school_score = hs_school_score + detail_list[i][2]
                hs_school_count += 1
        
        if ms_school_count == 0:
            final_ms_school_score = ms_school_score
        else:
            final_ms_school_score = round(ms_school_score/ms_school_count, 2)      
        
        if hs_school_count == 0:
            final_hs_school_score = hs_school_score
        else:
            final_hs_school_score = round(hs_school_score/hs_school_count, 2)      

        lst = [k_school_score, final_ms_school_score, 
            final_hs_school_score
            ]       
    return(lst)

def insert_into_db(r):
    for neighborhood, school_scores in r.items():
        score_list = get_3_scores(school_scores, neighborhood)  
        if len(score_list) > 0:                  
            try:
                item = Neighborhood.objects.get(name=neighborhood)
                School.objects.create(neighborhood=item,
                                      k_school_score = score_list[0],
                                      elem_school_score = score_list[1],
                                      hs_school_score = score_list[2])
            except Exception as e:
                print("*"*100)
                print(neighborhood)
                print(score_list)
                print(school_scores)
                print(type(e),e.args)
        else:
            print('!!!NO SCHOOLS!!!', neighborhood)
            item = Neighborhood.objects.get(name=neighborhood)
            School.objects.create(neighborhood=item,
                                  k_school_score = 1,
                                  elem_school_score = 1,
                                  hs_school_score = 1)

def extract_Pre_K_school_directory(fname, nb_zip, r):
# fname is the file with preK schools(public,private etc)
    list_of_cols = ["LocName","PreK_Type", 
    "Borough","address", "zip",
    "Seats","EXTENDED_DAY"]
    dataa = pd.read_csv(fname)
    index = dataa.iloc[0]
    dataa.columns = index.index
    
    df_info = dataa[["LocName", "PreK_Type", 
                    "Borough", "address",
                    "zip", "Seats", "EXTENDED_DAY"]]
    rows = df_info["LocName"].values
    
    df_info.index = rows
    scls = df_info.index
    for scl in range(0, len(scls)):
        obj = df_info.loc[scls[scl]]
        zipcode = obj["zip"].astype(int)
        for nb, vals in nb_zip.items():
            if str(zipcode) in vals:
                temp = [obj["LocName"],
                        obj["PreK_Type"],
                        obj["Seats"],
                        obj["zip"]]
                r[nb].append(temp)
#    print('universal preK: ',r)


# def load():
#         try:
#             item =  Neighborhood.objects.get(name=neighborhood)
#             School.objects.create(
#                 neighborhood=item,
#                 k_school_score = score_list[0],
#                 elem_school_score = score_list[1],
#                 hs_school_score = score_list[2]
#             )
#         except Exception as e:
#             print("*"*100)
#             print(neighborhood)
#             print(score_list)
#             print(school_scores)
#             print(type(e),e.args)

def run(folder_path):

    #---------------------------------Main pgm -----------------------------------------------
# r-(resultant dictionary) master dictionary with neighborhoods as keys and school(s) information/scores as values
    r = {} 
# our neighborhood names
 
    initialize_dict(nb_zip, r)
#----------------------------491 High Schools---------------------------------------------
    HighSchool_file = folder_path + '2014_2015_HS_SQR_Results_2016_01_07.xlsx'
    HSschool_list = extract_transform_school_data(folder_path, HighSchool_file, nb_zip, r)   # 491 high schools
    # print('High school count: ',len(HSschool_list))  

#----------------------------1254 elementary thru middle Schools---------------------------------------------
    ELMSchool_file = folder_path + '2014_2015_EMS_SQR_Results_2016_01_07.xlsx'
    ELMschool_list = extract_transform_school_data(folder_path, ELMSchool_file, nb_zip, r)   
    # print('Elementary-thru-Middleschools  ',len(ELMschool_list))

#----------------------------1885 preK Schools---------------------------------------------
    Pre_Kschool_file =  folder_path + 'Universal_Pre-K__UPK__School_Locations.csv' 
    extract_Pre_K_school_directory(Pre_Kschool_file, nb_zip, r)
#----------create Schools table-----------------------------------------------------------
    insert_into_db(r)











