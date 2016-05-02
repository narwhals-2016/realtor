from datetime import date,datetime

def hasGraduated(user_dic):
	lis_of_dics = []
	if not user_dic.get('education'):
		return False

	ed_dic = user_dic.get('education')
	length = len(ed_dic)
	for i in range(0,length):
		s = ed_dic[i]
		lis_of_dics.append(s)


	return parse_schools(lis_of_dics)


def parse_schools(lis):
	# for key,value in ed_dic.items():
	# 	if key == 'type' and value == 'High School':
	# 		year_dic= ed_dic.get('year')
	# 		year = year_dic.get('name')
	# 		year = int(year)
	##############################################
	'''
	Return True if Graduated or Graduating this year.
	'''
	if len(lis) < 1:
		return False 

	school_type = [value for item in lis for key,value in item.items() if value == 'College' or value == 'High School'] 
	
	for item in lis:
		for key,value in item.items():
			if value == 'College':
				year_dic = item.get('year')
				year = year_dic.get('name')
				year = int(year)
				if year <= 2016:
					return "True"
				if year > 2016:
					return "college_student"
			if value == 'High School' and 'College' not in school_type:
				year_dic = item.get('year')
				year = year_dic.get('name')
				year = int(year)
				if year > 2016:
					return "hs_student"
				elif year < 2016:
					return "hs_grad"
		
def genderfind(user_dic):
	if user_dic.get('gender') == "male":
		return "male" 
	if user_dic.get('gender') == "female":
		return "female"
	return False 

def agefind(user_dic):
	if user_dic.get('birthday'):
		my_date = user_dic.get('birthday')
		b_date = datetime.strptime(my_date, '%m/%d/%Y')
		age = ((datetime.today() - b_date).days/365)
		age = int(age)
		if age >= 0 and age <= 19:
			return"0_19"
		if age >= 20 and age <= 24:
			return"20_24"
		if age >= 25 and age <= 34:
			return"25_34"
		if age >= 35 and age <= 54:
			return"35_54"
		if age >= 55 and age <= 64:
			return"55_64"
		if age >= 65:
			return"65+"
		

		

			




