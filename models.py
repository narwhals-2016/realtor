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
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    borough = models.ForeignKey(Borough)
    age_0_19 = models.DecimalField(max_digits=None, decimal_places=5)
    age_20_24 = models.DecimalField(max_digits=None, decimal_places=5)
    age_25_34 = models.DecimalField(max_digits=None, decimal_places=5)
    age_35_64 = models.DecimalField(max_digits=None, decimal_places=5)
    age_65_over = models.DecimalField(max_digits=None, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            "borough": self.borough,
            "age_0_19": self.age_0_19,
            "age_20_24": self.age_20_24,
            "age_25_34": self.age_25_34,
            "age_35_64": self.age_35_64,
            "age_65_over": self.age_65_over, 
        }


class SchoolEducation(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    borough = models.ForeignKey(Borough)
    school_enrollment_pre_highschool = models.DecimalField(max_digits=None, decimal_places=5)
    school_enrollment_highschool = models.DecimalField(max_digits=None, decimal_places=5)
    school_enrollment_college = models.DecimalField(max_digits=None, decimal_places=5)
    education_highschool_over = models.DecimalField(max_digits=None, decimal_places=5)
    education_college_over = models.DecimalField(max_digits=None, decimal_places=5)
   
    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            "borough": self.borough,
            "school_enrollment_pre_highschool": self.school_enrollment_pre_highschool,
            "school_enrollment_highschool": self.school_enrollment_highschool,
            "school_enrollment_college": self.school_enrollment_college,
            "education_highschool_over": self.education_highschool_over,
            "education_college_over": self.education_college_over, 
        }


class Demographic(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    borough = models.ForeignKey(Borough)
    married = models.DecimalField(max_digits=None, decimal_places=5)
    divorced = models.DecimalField(max_digits=None, decimal_places=5)
    one_yr_turnover = models.DecimalField(max_digits=None, decimal_places=5)
    birth_native = models.DecimalField(max_digits=None, decimal_places=5)
    birth_foreign = models.DecimalField(max_digits=None, decimal_places=5)
    gender_m = models.DecimalField(max_digits=None, decimal_places=5)
    gender_f = models.DecimalField(max_digits=None, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            "borough": self.borough,
            "married": self.married,
            "divorced": self.divorced,
            "one_yr_turnover": self.one_yr_turnover,
            "birth_native": self.birth_native,
            "birth_foreign": self.birth_foreign, 
            "gender_m": self.gender_m,
            "gender_f": self.gender_f,
        }


class Economic(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    # borough = models.ForeignKey(Borough)
    laborforce = models.DecimalField(max_digits=None, decimal_places=5)
    unemployed = models.DecimalField(max_digits=None, decimal_places=5)
    below_poverty_level = models.DecimalField(max_digits=None, decimal_places=5)
    income_0_50 = models.DecimalField(max_digits=None, decimal_places=5)
    income_50_100 = models.DecimalField(max_digits=None, decimal_places=5)
    income_100_200 = models.DecimalField(max_digits=None, decimal_places=5)
    income_200_plus = models.DecimalField(max_digits=None, decimal_places=5)
    median_income = models.DecimalField(max_digits=None, decimal_places=5)
    mean_income = models.DecimalField(max_digits=None, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            # "borough": self.borough,
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
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    number_of_units_2_less = models.DecimalField(max_digits=None, decimal_places=5)
    number_of_units_3_10 = models.DecimalField(max_digits=None, decimal_places=5)
    number_of_units_10_plus = models.DecimalField(max_digits=None, decimal_places=5)
    constucted_before_1970 = models.DecimalField(max_digits=None, decimal_places=5)
    constucted_1970_2000 = models.DecimalField(max_digits=None, decimal_places=5)
    constucted_after_2000 = models.DecimalField(max_digits=None, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            "number_of_units_2_less": self.number_of_units_2_less,
            "number_of_units_3_10": self.number_of_units_3_10,
            "number_of_units_10_plus": self.number_of_units_10_plus,
            "constucted_before_1970": self.constucted_before_1970,
            "constucted_1970_2000": self.constucted_1970_2000, 
            "constucted_after_2000": self.constucted_after_2000,
        }


class UnitDescription(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    borough = models.ForeignKey(Borough)
    units_occupied = models.DecimalField(max_digits=None, decimal_places=5)
    units_vacant = models.DecimalField(max_digits=None, decimal_places=5)
    rooms_per_unit_under_3 = models.DecimalField(max_digits=None, decimal_places=5)
    rooms_per_unit_over_4 = models.DecimalField(max_digits=None, decimal_places=5)
    resident_type_owner = models.DecimalField(max_digits=None, decimal_places=5)
    resident_type_renter = models.DecimalField(max_digits=None, decimal_places=5)
    length_residence_before_2000 = models.DecimalField(max_digits=None, decimal_places=5)
    length_residence_2000_2009 = models.DecimalField(max_digits=None, decimal_places=5)
    length_residence_after_2010 = models.DecimalField(max_digits=None, decimal_places=5)
    vehicles_0 = models.DecimalField(max_digits=None, decimal_places=5)
    vehicles_1 = models.DecimalField(max_digits=None, decimal_places=5)
    vehicles_2_plus = models.DecimalField(max_digits=None, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            "borough": self.borough,
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


class UnitValue(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    borough = models.ForeignKey(Borough)
    value_of_unit_500_less = models.DecimalField(max_digits=None, decimal_places=5)
    value_of_unit_500_1M = models.DecimalField(max_digits=None, decimal_places=5)
    value_of_unit_1M_plus = models.DecimalField(max_digits=None, decimal_places=5)
    value_of_unit_median = models.DecimalField(max_digits=None, decimal_places=5)
    gross_rent_1000_less = models.DecimalField(max_digits=None, decimal_places=5)
    gross_rent_1000_1500 = models.DecimalField(max_digits=None, decimal_places=5)
    gross_rent_1500_plus = models.DecimalField(max_digits=None, decimal_places=5)
    gross_rent_median = models.DecimalField(max_digits=None, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            "borough": self.borough,
            "value_of_unit_500_less": self.value_of_unit_500_less,
            "value_of_unit_500_1M": self.value_of_unit_500_1M,
            "value_of_unit_1M_plus": self.value_of_unit_1M_plus,
            "value_of_unit_median": self.value_of_unit_median,
            "gross_rent_1000_less": self.gross_rent_1000_less, 
            "gross_rent_1000_1500": self.gross_rent_1000_1500,
            "gross_rent_1500_plus": self.gross_rent_1500_plus,
            "gross_rent_median": self.gross_rent_median,
        }


class Commute(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    borough = models.ForeignKey(Borough)
    communte_score = models.DecimalField(max_digits=None, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            "borough": self.borough,
            "communte_score": self.communte_score,
        }


class Features(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    borough = models.ForeignKey(Borough)
    night_life_score = models.DecimalField(max_digits=None, decimal_places=5)
    number_of_parks = models.DecimalField(max_digits=None, decimal_places=5)
    shopping_score = models.DecimalField(max_digits=None, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            "borough": self.borough,
            "night_life_score": self.night_life_score,
            "number_of_parks": self.number_of_parks,
            "shopping_score": self.shopping_score,
        }


class Grade(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    borough = models.ForeignKey(Borough)
    crime_score = models.DecimalField(max_digits=None, decimal_places=5)
    school_score = models.DecimalField(max_digits=None, decimal_places=5)
    noise_score = models.DecimalField(max_digits=None, decimal_places=5)

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood,
            "borough": self.borough,
            "crime_score": self.crime_score,
            "school_score": self.school_score,
            "noise_score": self.noise_score,
        }


# all other tables point here with FKs
class Neighborhood(models.Model):
    # id = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    name = models.CharField()
    # borough = models.CharField()

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "name": self.name,
            # "borough": self.borough,
        }


# all other tables point here with FKs
class Borough(models.Model):
    # id = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    name = models.CharField()

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "name": self.name,
        }

