import csv
import os
from pprint import pprint
import pandas as pd
import numpy as np
import datetime
import numpy as np
import pandas.io.data as web


# r (resultant dictionary) is the master dictionary with neighborhoods as keys and school(s) information/scores as the values
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


def get_HS_rating(r,c,df_trans):
    if c == 'New Visions Charter High School for Advanced Math':
        print('in function***',c,'***',df_trans['Unnamed: 3'])
    r['Number of students'] = df_trans[c]['Unnamed: 3']
    r['Instruction Rigor rating'] = df_trans[c]['Unnamed: 4']
    r['Student achievement rating'] = df_trans[c]['Unnamed: 10']
    return

#-----
def extract_transform_school_data(fname):

    list_of_cols = ["School Name","Enrollment",
    "Student Achievement Rating",'Rigorous Instruction Rating']

    dataa = {}
    dataa = pd.read_excel(fname, sheetname=0)
    index = dataa.iloc[0]
    school_type = fname.split('/')[4].split('_')[2]
    if school_type == "HS":
        c = dataa['2014-15 School Quality Report for High Schools'].values[1:]
    elif school_type == "EMS":
        c = dataa['2014-15 School Quality Report for Elementary, Middle, and K-8 Schools'].values[1:]
    #print(len(c))    
    df_trans = dataa[1:].transpose()    
    df_trans.columns = c
    df_trans.index = index.values           # assigning row labels

    # print(df_trans.loc['Enrollment'])
    # print(df_trans.loc['Rigorous Instruction Rating'])
    # print(df_trans.loc['Student Achievement Rating'])
    return(c)

    # r = {}
    #print('dt####',dt_index)
    #print('dt indexed**',dt_index)
    # for i in c:
    #   if i != 'School Name':
    #       try:
    #           print('SChool** ',df_trans[i]["Unnamed: 3"])
    #           r['Number of students'] = df_trans[i]['Unnamed: 3']
    #       except:
    #           print('school**',i,'  ratings not available')

    #       try:
    #           r['Instruction Rigor rating'] = df_trans[i]['Unnamed: 4']
    #       except:
    #           print('school**',i,'  ratings not available')

    #       try:
    #           r['Instruction Rigor rating'] = df_trans[i]['Unnamed: 10']
    #       except:
    #           print('school**',i,'  ratings not available')
        # print('for loop&&&',c[i],'vals&&&&&***',df_trans[c[i]['Unnamed: 3']])
        # get_HS_rating(r, c[i], df_trans)

    # r['Number of students'] = df_trans['Henry Street School for International Studies']['Unnamed: 3']
    # r['Instruction Rigor rating'] = df_trans['Henry Street School for International Studies']['Unnamed: 4']
    # r['Student achievement rating'] = df_trans['Henry Street School for International Studies']['Unnamed: 10']
    # print('dict****',r)
    
def extract_info_from_school_directory(fname):

    list_of_cols = ["school_name", 
    "boro","grade_span_min", "grade_span_max",
    "city","zip","total_students","Location 1"]
#----------------------------------
    dataa = {}
    dataa = pd.read_csv(fname)
    
    index = dataa.iloc[0]
    dataa.columns = index.index
    #print('index###',dataa["school_name"])
    # school_list = dataa[index.index[1]]
    school_list = dataa["school_name"]
    #print('schools****',school_list)
    # boro_list = dataa[index.index[2]]
    boro_list = dataa["boro"]
    city_list = dataa["city"]
    # total_no_of_students_list = dataa[index.index[17]]
    total_no_of_students_list = dataa["total_students"]
    zip_list = dataa["zip"]
    address_list = dataa["Location 1"]
    return(school_list)


def assign_PKschool_scores(dframe):
    pass

def initialize_dict():
    for key in best_matches:
        r[key] = []

def extract_Pre_K_school_directory(fname):

    list_of_cols = ["LocName","PreK_Type", 
    "Borough","address", "zip",
    "Seats","EXTENDED_DAY"]

    dataa = {}
    dataa = pd.read_csv(fname)
    
    index = dataa.iloc[0]
    c = dataa['LocName'].values[1:]
    dataa.columns = index.index
    
    PreK_school_list = dataa["LocName"].values
    PreK_school_type = dataa["PreK_Type"].values
    Borough_list = dataa["Borough"].values
    address_list = dataa["address"].values
    seats_list = dataa["Seats"].values
    extended_day_list = dataa["EXTENDED_DAY"].values
    zip_list = list(dataa["zip"].values)

    
    initialize_dict()
    # print('LIST**',zip_list)
    #print('zip: ',zip_list)
    # z_list = ['11692','10472']
    #print('whole dataset:', dataa[dataa["11692"]])
    for zipcode in zip_list:

        for nb, vals in best_matches.items():
            if str(zipcode) in vals:
                #print(zipcode,'****', nb, 'list  :',vals)
                ix = zip_list.index(int(zipcode))
                #print('index of the zipcode: ',ix,  seats_list[ix])

                temp = ["Kindergarten :", "School :"+PreK_school_list[ix],
                        "Type of school :"+PreK_school_type[ix],
                        "Number of students: "+str(seats_list[ix])]

                r[nb].append(temp)

    # print('r   :',len(r['Upper West Side']))
    #assign_PKschool_scores(dataa, zip_list)

def get_zip_codes_from_all_schools_directory(fname1,lst):
 
    
    dataa = pd.read_excel(fname1, sheetname=0)
    index = dataa.iloc[0]
    dataa.columns = index.index

    all_schools_from_directory_list = list(dataa["LEGAL NAME"].values)
    all_schools_addresses = list(dataa["MAILING ADDRESS"].values)
    all_schools_zips = list(dataa["ZIP"].values)    
    
    count = 0
    ncount = 0
    print('no of schools  ',len(lst), 'number of schools in directory :',len(all_schools_from_directory_list))
    for school in lst:
        school_uppercase = school.upper()
        if school_uppercase in all_schools_from_directory_list:
            ix = all_schools_from_directory_list.index(school_uppercase)
            count += 1
            # get address and zip
        else:
            ncount =+ 0
            #print(school,' is not in the list')
    print('COUNT   :',count,'not counted  :',ncount)

def compare_schools(c,c1):
    HS_list_from_directory = c1.values
    HS_list_from_reports = c
    matched_list = [school for school in HS_list_from_reports if school in HS_list_from_directory]
    #print('lst**', len(matched_list))
    unmatched_list = [school for school in HS_list_from_reports if school not in HS_list_from_directory]
    specialized_schools = unmatched_list
    #print('unmatched schools list **',len(unmatched_list))
    #print('unmatched schools: ',unmatched_list)

 

#----------------------------491 High Schools---------------------------------------------
# HighSchool_file = '/home/sulekha/SCHOOLS/2014_2015_HS_SQR_Results_2016_01_07.xlsx'
# school_count1 = extract_transform_school_data(HighSchool_file)   # 491 high schools
# #print('COUNT  ',len(school_count1))  

# HS_directory = '/home/sulekha/SCHOOLS/DOE_High_School_Directory_2014-2015.csv'
# school_count2 = extract_info_from_school_directory(HS_directory)    # 435 high schools (rest are special schools)
# #print('# of schhols from quality report:',len(school_count1),'# of schools from DOE:',len(school_count2))
# compare_schools(school_count1, school_count2)

#----------------------------1254 elementary thru middle Schools---------------------------------------------

# ELMSchool_file = '/home/sulekha/SCHOOLS/2014_2015_EMS_SQR_Results_2016_01_07.xlsx'
# ELMschool_count1 = extract_transform_school_data(ELMSchool_file)   
# print('Elementary-thru-Middleschools  ',len(ELMschool_count1))

Pre_Kschool_file =  '/home/sulekha/SCHOOLS/Universal_Pre-K__UPK__School_Locations.csv' 
Pre_Kschool_count1 = extract_Pre_K_school_directory(Pre_Kschool_file)   # 1885 schools  

# all_schools_directory =  '/home/sulekha/SCHOOLS/15-16SchoolDirectory.xlsx' 
# ELMschools_with_zip_code = get_zip_codes_from_all_schools_directory(all_schools_directory, ELMschool_count1)   # 1885 schools 








