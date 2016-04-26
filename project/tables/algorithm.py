from tables.models import Ages, Economic


def age_match(age):
	if age <= 19:
		return sort_by(table=Ages, field='age_0_19')
	elif 20 <= age <= 24:
		return sort_by(table=Ages, field='age_20_24')
	elif 25 <= age <= 34:
		return sort_by(table=Ages, field='age_25_34')
	elif 35 <= age <= 64:
		return sort_by(table=Ages, field='age_35_64')
	elif age >= 65:
		return sort_by(table=Ages, field='age_65_over')

def sort_by(table, field):
	# - is supposed to order by descending
	return table.objects.order_by('-' + field)[:10]

def income_match(income):
	if income < 50000:
		return sort_by(table=Economic, field='income_0_50')
	elif 50000 <= income < 100000:
		return sort_by(table=Economic, field='income_50_100')
	elif 100000 <= income < 200000:
		return sort_by(table=Economic, field='income_100_200')
	elif income >= 200000:
		return sort_by(table=Economic, field='income_200_plus')

