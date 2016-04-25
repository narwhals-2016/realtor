import csv
import os
from pprint import pprint
import pandas as pd
import numpy as np
import numpy as np
from tables.models import SchoolEducation, School, Neighborhood


def extract_transform_school_data(fname, best_matches, r):


    list_of_cols = ["School Name","Enrollment",
                    "Student Achievement Rating",
                    "Rigorous Instruction Rating"]
    dataa = {}
    dataa = pd.read_excel(fname, sheetname=0)
    index = dataa.iloc[0]



    school_type = fname.split('/')[3].split('_')[2]
    if school_type == "HS":
        c = dataa['2014-15 School Quality Report for High Schools'].values[1:]
    elif school_type == "EMS":
        c = dataa['2014-15 School Quality Report for Elementary, Middle, and K-8 Schools'].values[1:]
        
    df_trans = dataa[1:].transpose()   
    df_trans.columns = c
    df_trans.index = index.values 

    all_schools_directory =  'tables/datasets/schools/15-16SchoolDirectory.xlsx' 
    # for every school get the typr, addr and zipcode from all schools directory(master directory)
    addr_zip_dictionary = get_zip_codes_from_all_schools_directory(all_schools_directory, c) 
                
    for school, addr_and_zip in addr_zip_dictionary.items():     
        temp=[]

        zipcode = addr_and_zip[2] 
        obj = df_trans[school]
        en = 'Enrollment'
        try:
            enrol = obj[en]
        except:
            f = 0
        rt = "Rigorous Instruction Rating"
        try:
            rigor = obj[rt]
        except:
            f = 0            
        sa = 'Student Achievement Rating'
        try:
            student_achievemet = obj[sa]
        except:
            f = 0                        

        score =  calculate_score(enrol, rigor, student_achievemet)                        
        for nb, vals in best_matches.items():
            if str(zipcode) in vals:
                temp = [school,
                        addr_and_zip[0],
                        score,
                        addr_and_zip[1],
                        str(zipcode)]
                r[nb].append(temp)
    return(c)
    
#-----
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



def initialize_dict(best_matches, r):
# initialize the dictionary r with keys from best_matches(list of neighborhoods) 
    for key in best_matches:
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
            print('school_uppercase: ',school_uppercase)
    return(elm_addr_zip_dict)


def get_3_scores(detail_list, neighborhood):
# schoolType : Pre-K Only,Elementary,Middle School,Junior High School,Junior Senior School,
#              Senior High,Special School, K-12 School,NA, Other
# each item(list) in detail_list has school, schoolType, score, address and zip
    lst = []
    k_school_score = ms_school_score = hs_school_score = 0

    if len(detail_list) > 0:
        for i in range(0, len(detail_list)):
            if (detail_list[i][1] in ('Pre-K Only', 'DOE', 'CHARTER','NYCEEC','K-12 School')):
                k_school_score =+ 1
            elif (detail_list[i][1]  in ('Elementary','Middle School')):
                ms_school_score = ms_school_score + detail_list[i][2]
            elif (detail_list[i][1] in  ('K-12 School', 'Junior High School', 
                                         'Junior Senior School','Senior High')):
                hs_school_score = hs_school_score + detail_list[i][2]  
        lst = [k_school_score, ms_school_score, hs_school_score]       
    return(lst)

def insert_into_db(r):
    for neighborhood, school_scores in r.items():
        score_list = get_3_scores(school_scores, neighborhood)
       try:
           item =  Neighborhood.objects.get(name=neighborhood)
           School.objects.create(neighborhood=item,
                                 k_school_score = score_list[0],
                                 elem_school_score = score_list[1],
                                 hs_school_score = scoer_list[2])
       except:
           print(neighborhood, 'not found for School model')

def extract_Pre_K_school_directory(fname, best_matches, r):
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
        for nb, vals in best_matches.items():
            if str(zipcode) in vals:
                temp = [obj["PreK_Type"],
                        obj["Seats"],
                        obj["zip"]]
                r[nb].append(temp)
#    print('universal preK: ',r)


def run():
    #---------------------------------Main pgm -----------------------------------------------
# r-(resultant dictionary) master dictionary with neighborhoods as keys and school(s) information/scores as values
    r = {} 
# our neighborhood names
    best_matches = {
        'Allerton-Pelham Gardens': ['10312'],
        "Annadale-Huguenot-Prince's Bay-Eltingville": ['10312'],
        'Arden Heights': ['MISSING'],
        'Astoria': ['11103'],
        'Auburndale': ['11358'],
        'Baisley Park': ['11434'],
        'Bath Beach': ['11214'],
        'Battery Park City-Lower Manhattan': ['10280','10038','10004', '10006', '10005'],
        'Bay Ridge': ['11209'],
        'Bayside-Bayside Hills': ['11361'],
        'Bedford Park-Fordham North': ['10458'],
        'Bedford brooklyn': ['11216'],
        'Bellerose': ['11426'],
        'Belmont bronx': ['10458'],
        'Bensonhurst East': ['11204'],
        'Bensonhurst West': ['11214'],
        'Borough Park': ['11219'],
        'Breezy Point-Belle Harbor-Rockaway Park-Broad': ['11697'],
        'Briarwood-Jamaica Hills': ['11435'],
        'Brighton Beach': ['11235'],
        'Bronxdale': ['10462'],
        'Brooklyn Heights-Cobble Hill': ['11201'],
        'Brownsville': ['11212'],
        'Bushwick North': ['11237'],
        'Bushwick South': ['11237'],
        'Cambria Heights': ['11411'],
        'Canarsie': ['11236'],
        'Carroll Gardens-Columbia Street-Red Hook': ['11231'],
        'Central Harlem North-Polo Grounds': ['10039'],
        'Central Harlem South': ['10026'],
        'Charleston-Richmond Valley-Tottenville': ['10307'],
        'Chinatown': ['10013'],
        'Claremont-Bathgate': ['10457'],
        'Clinton Hill': ['11205'],
        'Co-Op City': ['10475'],
        'College Point': ['11356'],
        'Corona': ['11368'],
        'Crotona Park East': ['10460'],
        'Crown Heights North': ['11225'],
        'Crown Heights South': ['11225'],
        'Cypress Hills-City Line': ['11208'],
        'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': ['11201',"11217"],
        'Douglas Manor-Douglaston-Little Neck': ['11362'],
        'Dyker Heights': ['11228'],
        'East Concourse-Concourse Village': ['10451'],
        'East Elmhurst': ['11369'],
        'East Flatbush-Farragut': ['11203'],
        'East Flushing': ['11354'],
        'East Harlem North': ['10037'],
        'East Harlem South': ['10029'],
        'East New York': ['11207'],
        'East New York (Pennsylvania Ave)': ['11207'],
        'East Tremont': ['10457'],
        'East Village': ['10009'],
        'East Williamsburg': ['11211'],
        'Eastchester-Edenwald-Baychester': ['10475'],
        'Elmhurst': ['11373'],
        'Elmhurst-Maspeth': ['11373'],
        'Erasmus': ['11226'],
        'Far Rockaway-Bayswater': ['11691'],
        'Flatbush': ['11226'],
        'Flatlands': ['11234'],
        'Flushing': ['11354'],
        'Fordham South': ['10458'],
        'Forest Hills': ['11375'],
        'Fort Greene': ['11205'],
        'Fresh Meadows-Utopia': ['11365'],
        'Ft. Totten-Bay Terrace-Clearview': ['11360'],
        'Georgetown-Marine Park-Bergen Beach-Mill Basi': ['11234'],
        'Glen Oaks-Floral Park-New Hyde Park': ['11040'],
        'Glendale': ['11385'],
        'Gramercy': ['10003'],
        'Grasmere-Arrochar-Ft. Wadsworth': ['10304'],
        'Gravesend': ['11223'],
        'Great Kills': ['10308'],
        'Greenpoint': ['11222'],
        'Grymes Hill-Clifton-Fox Hills': ['10301'],
        'Hamilton Heights': ['10031'],
        'Hammels-Arverne-Edgemere': ['11692'],
        'Highbridge': ['10452'],
        'Hollis': ['11423'],
        'Homecrest': ['11223'],
        'Hudson Yards-Chelsea-Flat Iron-Union Square': ['10011',"10001"],
        'Hunters Point-Sunnyside-West Maspeth': ['11104'],
        'Hunts Point': ['10474'],
        'Jackson Heights': ['11372'],
        'Jamaica': ['11432'],
        'Jamaica Estates-Holliswood': ['11423'],
        'Kensington-Ocean Parkway': ['11218'],
        'Kew Gardens': ['11415'],
        'Kew Gardens Hills': ['11415'],
        'Kingsbridge Heights': ['10463'],
        'Laurelton': ['11413'],
        'Lenox Hill-Roosevelt Island': ['10065'],
        'Lincoln Square': ['10023'],
        'Lindenwood-Howard Beach': ['11414'],
        'Longwood': ['10455'],
        'Lower East Side': ['10002'],
        'Madison brookl': ['11229'],
        'Manhattanville': ['10027'],
        'Marble Hill-Inwood': ['10034'],
        "Mariner's Harbor-Arlington-Port Ivory-Granite": ['10303'],
        'Maspeth': ['11378'],
        'Melrose South-Mott Haven North': ['10451'],
        'Middle Village': ['11379'],
        'Midtown-Midtown South': ['10019'],
        'Midwood': ['11230'],
        'Morningside Heights': ['10027'],
        'Morrisania-Melrose': ['10456'],
        'Mott Haven-Port Morris': ['10454'],
        'Mount Hope': ['10003'],
        'Murray Hill': ['10016'],
        'Murray Hill-Kips Bay': ['10016'],
        'New Brighton-Silver Lake': ['10301'],
        'New Dorp-Midland Beach': ['10306'],
        'New Springville-Bloomfield-Travis': ['10314'],
        'North Corona': ['11368'],
        'North Riverdale-Fieldston-Riverdale': ['10471'],
        'North Side-South Side': ['MISSING'],
        'Norwood': ['10467'],
        'Oakland Gardens': ['11364'],
        'Oakwood-Oakwood Beach': ['10306'],
        'Ocean Hill': ['11233'],
        'Ocean Parkway South': ['11230'],
        'Old Astoria': ['11102'],
        'Old Town-Dongan Hills-South Beach': ['10305'],
        'Ozone Park': ['11417'],
        'Parkchester': ['10462'],
        'Pelham Bay-Country Club-City Island': ['10464'],
        'Pelham Parkway': ['10062'],
        'Pomonok-Flushing Heights-Hillcrest': ['11354','11206'],
        'Port Richmond': ['10302'],
        'Prospect Heights': ['11238'],
        'Prospect Lefferts Gardens-Wingate': ['11225'],
        'Queens Village': ['11428'],
        'Queensboro Hill queens': ['11355'],
        'Queensbridge-Ravenswood-Long Island City': ['11106','11101'],
        'Rego Park': ['11374'],
        'Richmond Hill': ['11418'],
        'Ridgewood': ['11385'],
        'Rikers Island': ['MISSING'],
        'Rosedale': ['11422'],
        'Rossville-Woodrow': ['10309'],
        'Clinton' : ['10036','10019','10018'],
        'Rugby-Remsen Village': ['11203'],
        'Schuylerville-Throgs Neck-Edgewater Park': ['10465'],
        'Seagate-Coney Island': ['11224'],
        'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': ['11235'],
        'SoHo-TriBeCa-Civic Center-Little Italy': ['10013','10007'],
        'Soundview-Bruckner': ['10472'],
        'Soundview-Castle Hill-Clason Point-Harding Pa': ['10472'],
        'South Jamaica': ['11433'],
        'South Ozone Park': ['11436'],
        'Springfield Gardens North': ['11413'],
        'Springfield Gardens South-Brookville': ['11413'],
        'Spuyten Duyvil-Kingsbridge': ['10463'],
        'St. Albans': ['11412'],
        'Stapleton-Rosebank': ['10305'],
        'Starrett City': ['11239'],
        'Steinway': ['11105'],
        'Stuyvesant Heights nyc': ['11233'],
        'Stuyvesant Town-Cooper Village': ['10009','10010'],
        'Sunset Park East': ['11220'],
        'Sunset Park West': ['11220'],
        'Todt Hill-Emerson Hill-Heartland Village-Ligh': ['10304'],
        'Turtle Bay-East Midtown': ['10022'],
        'University Heights-Morris Heights': ['10453'],
        'Upper East Side-Carnegie Hill': ['10128','10028','10075', '10021'],
        'Upper West Side': ['10024','10025'],
        'Van Cortlandt Village': ['10468'],
        'Van Nest-Morris Park-Westchester Square': ['10462'],
        'Washington Heights North': ['10040','10032','10033'],
        'Washington Heights South': ['10033'],
        'West Brighton': ['10310'],
        'West Concourse': ['10451'],
        'West Farms-Bronx River': ['10460'],
        'West New Brighton-New Brighton-St. George': ['10310'],
        'West Village': ['10014','10012'],
        'Westchester-Unionport': ['10461'],
        'Westerleigh': ['10314'],
        'Whitestone': ['11357'],
        'Williamsbridge-Olinville': ['10467','11249'],
        'Williamsburg': ['11211'],
        'Windsor Terrace': ['11215'],
        'Woodhaven': ['11421'],
        'Woodlawn-Wakefield': ['10466'],
        'Woodside': ['11377'],
        'Yorkville nyc': ['10128'],
        "hell's kitchen": ['10019'],
    }


    initialize_dict(best_matches, r)
#----------------------------491 High Schools---------------------------------------------
    HighSchool_file = 'tables/datasets/schools/2014_2015_HS_SQR_Results_2016_01_07.xlsx'
    HSschool_list = extract_transform_school_data(HighSchool_file, best_matches, r)   # 491 high schools
    # print('High school count: ',len(HSschool_list))  

# #----------------------------1254 elementary thru middle Schools-------------------------
    ELMSchool_file = 'tables/datasets/schools/2014_2015_EMS_SQR_Results_2016_01_07.xlsx'
    ELMschool_list = extract_transform_school_data(ELMSchool_file, best_matches, r)   
    # print('Elementary-thru-Middleschools  ',len(ELMschool_list))

#----------------------------1885 preK Schools---------------------------------------------
    Pre_Kschool_file =  'tables/datasets/schools/Universal_Pre-K__UPK__School_Locations.csv' 
    extract_Pre_K_school_directory(Pre_Kschool_file, best_matches, r)
#----------create Schools table-----------------------------------------------------------
    insert_into_db(r)











