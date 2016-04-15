# from django.db import models
# from django.contrib.auth.models import User
# from django.utils.text import slugify
# from django.utils import timezone #make sure to set the timezone 

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def to_json(self):
        return {
            "email": user.email,
            "username": user.username,
        }
    '''
    we can add aditional attributes but Included in the django user model are these attributes:
    Username, Password, Email address, firstname, lastname
    '''

class Ages(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    age_0_19 = models.IntegerField(default=0)
    age_20_24 = models.IntegerField(default=0)
    age_25_34 = models.IntegerField(default=0)
    age_35_64 = models.IntegerField(default=0)
    age_65_over = models.IntegerField(default=0)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "age_0_19": self.age_0_19,
            "age_20_24": self.age_20_24,
            "age_25_34": self.age_25_34,
            "age_35_64": self.age_35_64,
            "age_65_over": self.age_65_over, 
        }


class School_education(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    school_enrollment_pre_highschool = models.IntegerField(default=0)
    school_enrollment_highschool = models.IntegerField(default=0)
    school_enrollment_college = models.IntegerField(default=0)
    education_highschool_over = models.IntegerField(default=0)
    education_college_over = models.IntegerField(default=0)
   
    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "school_enrollment_pre_highschool": self.school_enrollment_pre_highschool,
            "school_enrollment_highschool": self.school_enrollment_highschool,
            "school_enrollment_college": self.school_enrollment_college,
            "education_highschool_over": self.education_highschool_over,
            "education_college_over": self.education_college_over, 
        }


class Demographic(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    married = models.IntegerField(default=0)
    divorced = models.IntegerField(default=0)
    one_yr_turnover = models.IntegerField(default=0)
    birth_native = models.IntegerField(default=0)
    birth_foreign = models.IntegerField(default=0)
    gender_m = models.IntegerField(default=0)
    gender_f = models.IntegerField(default=0)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "married": self.married,
            "divorced": self.divorced,
            "one_yr_turnover": self.one_yr_turnover,
            "birth_native": self.birth_native,
            "birth_foreign": self.birth_foreign, 
            "gender_m": self.gender_m,
            "gender_f": self.gender_f,
        }


class Economic(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    laborforce = models.IntegerField(default=0)
    unemployed = models.IntegerField(default=0)
    below_poverty_level = models.IntegerField(default=0)
    income_0_50 = models.IntegerField(default=0)
    income_50_100 = models.IntegerField(default=0)
    income_100_200 = models.IntegerField(default=0)
    income_200_plus = models.IntegerField(default=0)
    median_income = models.IntegerField(default=0)
    mean_income = models.IntegerField(default=0)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "laborforce": self.laborforce,
            "unemployed": self.unemployed,
            "below_poverty_level": self.below_poverty_level,
            "income_0_50": self.income_0_50,
            "income_50_100": self.income_50_100, 
            "income_100_200": self.income_100_200,
            "income_200_plus": self.income_200_plus,
            "median_income": self.median_income,
            "mean_income": self.mean_income,
        }


class Building(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    number_of_units_2_less = models.IntegerField(default=0)
    number_of_units_3_10 = models.IntegerField(default=0)
    number_of_units_10_plus = models.IntegerField(default=0)
    constucted_before_1970 = models.IntegerField(default=0)
    constucted_1970_2000 = models.IntegerField(default=0)
    constucted_after_2000 = models.IntegerField(default=0)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "number_of_units_2_less": self.number_of_units_2_less,
            "number_of_units_3_10": self.number_of_units_3_10,
            "number_of_units_10_plus": self.number_of_units_10_plus,
            "constucted_before_1970": self.constucted_before_1970,
            "constucted_1970_2000": self.constucted_1970_2000, 
            "constucted_after_2000": self.constucted_after_2000,
        }


class Unit(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    units_occupied = models.IntegerField(default=0)
    units_vacant = models.IntegerField(default=0)
    rooms_per_unit_under_3 = models.IntegerField(default=0)
    rooms_per_unit_over_4 = models.IntegerField(default=0)
    resident_type_owner = models.IntegerField(default=0)
    resident_type_renter = models.IntegerField(default=0)
    length_residence_before_2000 = models.IntegerField(default=0)
    length_residence_2000_2009 = models.IntegerField(default=0)
    length_residence_after_2010 = models.IntegerField(default=0)
    vehicles_0 = models.IntegerField(default=0)
    vehicles_1 = models.IntegerField(default=0)
    vehicles_2_plus = models.IntegerField(default=0)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "units_occupied": self.units_occupied,
            "units_vacant": self.units_vacant,
            "rooms_per_unit_under_3": self.rooms_per_unit_under_3,
            "rooms_per_unit_over_4": self.rooms_per_unit_over_4,
            "resident_type_owner": self.resident_type_owner, 
            "resident_type_renter": self.resident_type_renter,
            "length_residence_before_2000": self.length_residence_before_2000,
            "length_residence_2000_2009": self.length_residence_2000_2009,
            "length_residence_after_2010": self.length_residence_after_2010,
            "vehicles_0": self.vehicles_0,
            "vehicles_1": self.vehicles_1,
            "vehicles_2_plus": self.vehicles_2_plus,
        }


class Value(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    value_of_unit_500_less = models.IntegerField(default=0)
    value_of_unit_500_1M = models.IntegerField(default=0)
    value_of_unit_1M_plus = models.IntegerField(default=0)
    value_of_unit_median = models.IntegerField(default=0)
    gross_rent_1000_less = models.IntegerField(default=0)
    gross_rent_1000_1500 = models.IntegerField(default=0)
    gross_rent_1500_plus = models.IntegerField(default=0)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "value_of_unit_500_less": self.value_of_unit_500_less,
            "value_of_unit_500_1M": self.value_of_unit_500_1M,
            "value_of_unit_1M_plus": self.value_of_unit_1M_plus,
            "value_of_unit_median": self.value_of_unit_median,
            "gross_rent_1000_less": self.gross_rent_1000_less, 
            "gross_rent_1000_1500": self.gross_rent_1000_1500,
            "gross_rent_1500_plus": self.gross_rent_1500_plus,
        }


class Commute(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    communte_score = models.IntegerField(default=0)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "communte_score": self.communte_score,
        }


class Features(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    night_life_score = models.IntegerField(default=0)
    number_of_parks = models.IntegerField(default=0)
    shopping_score = models.IntegerField(default=0)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "night_life_score": self.night_life_score,
            "number_of_parks": self.number_of_parks,
            "shopping_score": self.shopping_score,
        }


class Grade(models.Model):
    neighborhood_id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    borough_id = models.ForeignKey(Borough)
    crime_score = models.IntegerField(default=0)
    school_score = models.IntegerField(default=0)
    noise_score = models.IntegerField(default=0)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood_id": self.neighborhood_id,
            "borough_id": self.borough_id,
            "crime_score": self.crime_score,
            "school_score": self.school_score,
            "noise_score": self.noise_score,
        }


# all other tables point here with FKs
class Neighborhoods(models.Model):
    # id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    name = models.CharField()
    borough = models.CharField()

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "name": self.name,
            "borough": self.borough_id,
        }


# all other tables point here with FKs
class Borough(models.Model):
    # id = models.ForeignKey(Neighborhoods) # FK to the neighborhoods table
    name = models.CharField()

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "name": self.name,
        }

