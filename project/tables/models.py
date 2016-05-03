from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    # id = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    name      = models.CharField(max_length=256)
    latitude  = models.CharField(max_length = 25, blank=True, default='') 
    longitude = models.CharField(max_length = 25, blank=True, default='')
    pic_link  = models.URLField(max_length=500, blank=True, default='')
    webdisplay = models.CharField(max_length=256, blank=True, default='')

    def __str__(self):
        return self.name

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "name": self.name,
        }

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # search = models.CharField(max_length=3000, default=None, Null=True)
    '''
    we can add aditional attributes but Included in the django user model are these attributes:
    Username, Password, Email address, firstname, lastname
    '''

    def to_json(self):
        return {
            "email": user.email,
            "username": user.username,
        }

class Ages(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    age_0_19 = models.DecimalField(max_digits=10, decimal_places=2)
    age_20_24 = models.DecimalField(max_digits=10, decimal_places=2)
    age_25_34 = models.DecimalField(max_digits=10, decimal_places=2)
    age_35_64 = models.DecimalField(max_digits=10, decimal_places=2)
    age_65_over = models.DecimalField(max_digits=10, decimal_places=2)
    age_median = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.neighborhood.name


    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
            "age_0_19": self.age_0_19,
            "age_20_24": self.age_20_24,
            "age_25_34": self.age_25_34,
            "age_35_64": self.age_35_64,
            "age_65_over": self.age_65_over,
            "age_median": self.age_median, 
        }

class Economic(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    laborforce = models.DecimalField(max_digits=10, decimal_places=2)
    unemployed = models.DecimalField(max_digits=10, decimal_places=2)
    below_poverty_level = models.DecimalField(max_digits=10, decimal_places=2)
    income_0_50 = models.DecimalField(max_digits=10, decimal_places=2)
    income_50_100 = models.DecimalField(max_digits=10, decimal_places=2)
    income_100_200 = models.DecimalField(max_digits=10, decimal_places=2)
    income_200_plus = models.DecimalField(max_digits=10, decimal_places=2)
    median_income = models.DecimalField(max_digits=10, decimal_places=2)
    mean_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.neighborhood.name


    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
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


# all other tables point here with FKs
class SchoolEducation(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    school_enrollment_pre_highschool = models.DecimalField(max_digits=10, decimal_places=2)
    school_enrollment_highschool = models.DecimalField(max_digits=10, decimal_places=2)
    school_enrollment_college = models.DecimalField(max_digits=10, decimal_places=2)
    education_highschool_over = models.DecimalField(max_digits=10, decimal_places=2)
    education_college_over = models.DecimalField(max_digits=10, decimal_places=2)
   
    def __str__(self):
        return self.neighborhood.name


    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
            "school_enrollment_pre_highschool": self.school_enrollment_pre_highschool,
            "school_enrollment_highschool": self.school_enrollment_highschool,
            "school_enrollment_college": self.school_enrollment_college,
            "education_highschool_over": self.education_highschool_over,
            "education_college_over": self.education_college_over, 
        }

class Building(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    number_of_units_2_less = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_units_3_10 = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_units_10_plus = models.DecimalField(max_digits=10, decimal_places=2)
    constucted_before_1970 = models.DecimalField(max_digits=10, decimal_places=2)
    constucted_1970_2000 = models.DecimalField(max_digits=10, decimal_places=2)
    constucted_after_2000 = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.neighborhood.name

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
            "number_of_units_2_less": self.number_of_units_2_less,
            "number_of_units_3_10": self.number_of_units_3_10,
            "number_of_units_10_plus": self.number_of_units_10_plus,
            "constucted_before_1970": self.constucted_before_1970,
            "constucted_1970_2000": self.constucted_1970_2000, 
            "constucted_after_2000": self.constucted_after_2000,
        }

class Demographic(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    # children_under_18 = models.DecimalField(max_digits=10, decimal_places=2)
    married = models.DecimalField(max_digits=10, decimal_places=2)
    # not_married = models.DecimalField(max_digits=10, decimal_places=2)
    divorced = models.DecimalField(max_digits=10, decimal_places=2)
    one_yr_turnover = models.DecimalField(max_digits=10, decimal_places=2)
    birth_native = models.DecimalField(max_digits=10, decimal_places=2)
    birth_foreign = models.DecimalField(max_digits=10, decimal_places=2)
    gender_m = models.DecimalField(max_digits=10, decimal_places=2)
    gender_f = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.neighborhood.name


    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
            "married": self.married,
            "divorced": self.divorced,
            "one_yr_turnover": self.one_yr_turnover,
            "birth_native": self.birth_native,
            "birth_foreign": self.birth_foreign, 
            "gender_m": self.gender_m,
            "gender_f": self.gender_f,
        } 

class UnitValue(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    value_of_unit_500_less = models.DecimalField(max_digits=10, decimal_places=2)
    value_of_unit_500_1M = models.DecimalField(max_digits=10, decimal_places=2)
    value_of_unit_1M_plus = models.DecimalField(max_digits=10, decimal_places=2)
    value_of_unit_median = models.DecimalField(max_digits=10, decimal_places=2)
    gross_rent_1000_less = models.DecimalField(max_digits=10, decimal_places=2)
    gross_rent_1000_1500 = models.DecimalField(max_digits=10, decimal_places=2)
    gross_rent_1500_plus = models.DecimalField(max_digits=10, decimal_places=2)
    gross_rent_median = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.neighborhood.name

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
            "value_of_unit_500_less": self.value_of_unit_500_less,
            "value_of_unit_500_1M": self.value_of_unit_500_1M,
            "value_of_unit_1M_plus": self.value_of_unit_1M_plus,
            "value_of_unit_median": self.value_of_unit_median,
            "gross_rent_1000_less": self.gross_rent_1000_less, 
            "gross_rent_1000_1500": self.gross_rent_1000_1500,
            "gross_rent_1500_plus": self.gross_rent_1500_plus,
            "gross_rent_median": self.gross_rent_median,
        }

class StreetEasy(models.Model):
    neighborhood = models.ForeignKey(Neighborhood)
    rent_median = models.DecimalField(max_digits=10, decimal_places=2)
    rent_average = models.DecimalField(max_digits=10, decimal_places=2)
    squarefeet_median = models.DecimalField(max_digits=10, decimal_places=2)
    squarefeet_average = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.neighborhood.name


    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
            "rent_median": self.rent_median,
            "rent_average": self.rent_average,
            "squarefeet_median": self.squarefeet_median,
            "squarefeet_average": self.squarefeet_average,
        }

class UnitDescription(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    units_occupied = models.DecimalField(max_digits=10, decimal_places=2)
    units_vacant = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_per_unit_1 = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_per_unit_2 = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_per_unit_3_5 = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_per_unit_6_plus = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_median = models.DecimalField(max_digits=10, decimal_places=2)
    resident_type_owner = models.DecimalField(max_digits=10, decimal_places=2)
    resident_type_renter = models.DecimalField(max_digits=10, decimal_places=2)
    length_residence_before_2000 = models.DecimalField(max_digits=10, decimal_places=2)
    length_residence_2000_2009 = models.DecimalField(max_digits=10, decimal_places=2)
    length_residence_after_2010 = models.DecimalField(max_digits=10, decimal_places=2)
    vehicles_0 = models.DecimalField(max_digits=10, decimal_places=2)
    vehicles_1_plus = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.neighborhood.name

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
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

class Score(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    night_life_score = models.DecimalField(max_digits=10, decimal_places=2)
    commute_score = models.DecimalField(max_digits=10, decimal_places=2)
    crime_score = models.DecimalField(max_digits=10, decimal_places=2)
    noise_score = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.neighborhood.name

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
            "night_life_score": self.night_life_score,
            "communte_score": self.communte_score,
            "crime_score": self.crime_score,
            "noise_score": self.noise_score,
        }

class School(models.Model):
    neighborhood = models.ForeignKey(Neighborhood) # FK to the neighborhood table
    k_school_score = models.DecimalField(max_digits=10, decimal_places=2)
    elem_school_score = models.DecimalField(max_digits=10, decimal_places=2)
    hs_school_score = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.neighborhood.name

    # this create a dictionary from an object to use with ajax
    def to_json(self):
        return {
            "neighborhood": self.neighborhood.name,
            "k_school_score": self.k_school_score,
            "elem_school_score": self.elem_school_score,
            "hs_school_score": self.hs_school_score,
        }


        
