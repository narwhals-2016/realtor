from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput, PasswordInput
from .models import Neighborhood, Ages, Economic, SchoolEducation, Building, Demographic, UnitValue, UnitDescription


# form used to register a user
class UserForm(UserCreationForm):
    "tried using the user creation form, didnt like it"
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
        widgets = {
            # this sets the input text area
            "password": PasswordInput(),
        }

# Layout
# CHOICES = [('Form name','Database name'),]

# in the form there are two choice that correspond to the same db input (35-64)
AGE_CHOICES = [('0_19',"age_0_19"), ('20_24',"age_20_24"), ('25_34',"age_25_34"), ('35_54',"age_35_64"), ('55_64',"age_35_64"), ('65+',"age_65_over")]
GENDER_CHOICES = [('male',"gender_m"), ('female', "gender_f")]
# there is no children field in the db 
NUMBER_OF_CHILDREN_CHOICES = [('none','0'), ('1_plus','1_2'), ('3_plus','3_plus')]
CURRENT_EDU_LEVEL_CHOICES = [('elementary','school_enrollment_pre_highschool'), ('hs','school_enrollment_highschool'), ('college','school_enrollment_college')]
HIGHEST_EDU_LEVEL_CHOICES = [('hs_plus','education_highschool_over'), ('college_plus','education_college_over')]
MARITAL_STATUS_CHOICES = [('on','married'), ('off','divorced')]
NUMBER_OF_UNITS_CHOICES = [('0_2','number_of_units_2_less'), ('3_10','number_of_units_3_10'), ('10_+','number_of_units_10_plus')]
OWNERSHIP_TYPE_CHOICES = [('rent','resident_type_renter'), ('purchase','resident_type_owner')]
NUMBER_OF_ROOMS_CHOICES = [('1_room','rooms_per_unit_1'), ('2_room','rooms_per_unit_2'),('3_5_room','rooms_per_unit_3_5'), ('6_plus','rooms_per_unit_6_plus')]
BUILDING_AGE_CHOICES = [('pre_1970','constucted_before_1970'), ('post_1970','constucted_1970_2000'), ('2000+','constucted_after_2000')]
NUMBER_OF_VEHICLES_CHOICES = [('off','vehicles_0'), ('on','vehicles_1'), ('on','vehicles_2_plus')]
# there is no commute types field in the db 
COMMUTE_TYPE_CHOICES = [('walk','walk'), ('transit','transit'), ('drive','drive')]
# these two feilds go into the school score table
SCHOOL_LEVEL_CHOICES = [('school_k-','k_school_score'), ('school_1-8','elem_school_score'), ('school_hs','hs_school_score'), ('school_none','none')]
SCHOOL_QUALITY_CHOICES = [('not_high','not_high'), ('high','high'), ('very_high','very_high')]
NIGHT_LIFE_CHOICES = [('not_high','night_life_score'), ('high','night_life_score'), ('very_high','night_life_score')]
NOISE_LEVEL_CHOICES = [('off','noise_score'), ('on','noise_score')]
CRIME_LEVEL_CHOICES = [('off','crime_score'), ('on','crime_score')]


class SearchForm(forms.Form):
    age = forms.ChoiceField(
        choices = AGE_CHOICES,
    )
    gender = forms.ChoiceField(
        choices = GENDER_CHOICES,
    )
    number_of_children = forms.ChoiceField(
        choices = NUMBER_OF_CHILDREN_CHOICES,
    )
    current_edu_level = forms.ChoiceField(
        choices = CURRENT_EDU_LEVEL_CHOICES,
    )
    highest_edu_level = forms.ChoiceField(
        choices = HIGHEST_EDU_LEVEL_CHOICES,
    )
    marital_status_checkbox = forms.ChoiceField(
        choices = MARITAL_STATUS_CHOICES,
    )
    income_level_range = forms.CharField() # get the input directly from the user
    number_of_units = forms.ChoiceField(
        choices = NUMBER_OF_UNITS_CHOICES,    
    )
    ownership_type = forms.ChoiceField(
        choices = OWNERSHIP_TYPE_CHOICES,
    )
    number_of_rooms = forms.ChoiceField(
        choices = NUMBER_OF_ROOMS_CHOICES,    
    )
    building_age = forms.ChoiceField(
        choices = BUILDING_AGE_CHOICES,
    )
    price_range = forms.CharField() # get the input directly from the user
    number_of_vehicles_checkbox = forms.ChoiceField(
        choices = NUMBER_OF_VEHICLES_CHOICES,
    )
    commute_address = forms.CharField() # get the input directly from the user
    commute_type = forms.ChoiceField(
        choices = COMMUTE_TYPE_CHOICES,
    )
    commute_time_range = forms.CharField() # get the input directly from the user
    school_level = forms.ChoiceField(
        choices = SCHOOL_LEVEL_CHOICES,
    )
    school_quality_importance = forms.ChoiceField(
        choices = SCHOOL_QUALITY_CHOICES,
    )
    night_life_importance = forms.ChoiceField(
        choices = NIGHT_LIFE_CHOICES,
    )
    noise_level_checkbox = forms.ChoiceField(
        choices = NOISE_LEVEL_CHOICES,
    )
    crime_level_checkbox = forms.ChoiceField(
        choices = CRIME_LEVEL_CHOICES,
    )


    # def is_valid():
    #     pass

    # def execute_queries(self):
    #     pass



