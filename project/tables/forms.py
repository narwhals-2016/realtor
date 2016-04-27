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


AGE_CHOICES = [('0_19','0_19'), ('20_24','20_24'), ('25_34','25_34'), ('35_54','35_54'), ('55_64','55_64'), ('65_plus','65_plus')]
GENDER_CHOICES = [('male','male'), ('female','female')]
NUMBER_OF_CHILDREN_CHOICES = [('0','0'), ('1_2','1_2'), ('3_plus','3_plus')]
CURRENT_EDU_LEVEL_CHOICES = [('hs','hs'), ('college','college')]
NUMBER_OF_UNITS_CHOICES = [('0_2','0_2'), ('3_10','3_10'), ('10_plus','10_plus')]
OWNERSHIP_TYPE_CHOICES = [('rent','rent'), ('purchase','purchase')]
NUMBER_OF_ROOMS_CHOICES = [('0_3','0_3'), ('4_plus','4_plus')]
BUILDING_AGE_CHOICES = [('pre 1970', 'pre 1970'), ('post 1970', 'post 1970')]
NIGHT_LIFE_CHOICES = [('not_high','not_high'), ('high','high'), ('very_high','very_high')]
SCHOOL_QUALITY_CHOICES = [('not_high','not_high'), ('high','high'), ('very_high','very_high')]


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
    number_of_units = forms.ChoiceField(
        choices = NUMBER_OF_UNITS_CHOICES,    
    )
    resident_type = forms.ChoiceField(
        choices = OWNERSHIP_TYPE_CHOICES,
    )
    rooms_per_unit = forms.ChoiceField(
        choices = NUMBER_OF_ROOMS_CHOICES,
    )
    building_age = forms.ChoiceField(
        choices = BUILDING_AGE_CHOICES,
    )
    night_life_importance = forms.ChoiceField(
        choices = NIGHT_LIFE_CHOICES,
    )
    school_quality_importance = forms.ChoiceField(
        choices = SCHOOL_QUALITY_CHOICES,
    )
    # Turn checkboxes into booleans, or use widgets checkboxinput?
    # currently_in_school = forms.BooleanField(label = 'currently in school')
    # marital_status_checkbox = forms.forms.BooleanField(label = 'marital_status_checkbox')
    # noise_level_checkbox= forms.forms.BooleanField(label = 'noise_level_checkbox')


    # def is_valid():
        # pass

    def execute_queries(self):
        pass



