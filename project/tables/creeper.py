
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

	for item in lis:
		for key,value in item.items():
			if key == 'type' and value == 'College':
				year_dic = item.get('year')
				year = year_dic.get('name')
				year = int(year)
				if year <= 2016:
					return True
				return False 

def genderfind(user_dic):
	if user_dic.get('gender') == "male":
		return "male" 
	if user_dic.get('gender') == "female":
		return "female"
	return False 

def agefind(user_dic):
	if user_dic.get('birthday'):
		print(user_dic.get('birthday'))
		return True 



