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


AGE_CHOICES = ('0_19', '20_24', '25_34', '35_54', '55_64', '65_plus')
GENDER_CHOICES = ('male', 'female')
NUMBER_OF_CHILDREN_CHOICES = ('0', '1_2', '3_plus')
CURRENT_EDU_LEVEL_CHOICES = ('hs', 'college')
NUMBER_OF_UNITS_CHOICES = ('0_2', '3_10', '10_plus')
OWNERSHIP_TYPE_CHOICES = ('rent', 'purchase')
NUMBER_OF_ROOMS_CHOICES = ('0_3', '4_plus')
BUILDING_AGE_CHOICES = ('pre 1970', 'post 1970')

class QueryForm(forms.Form):
    age = forms.ChoiceField(
        label = 'your age',
        choices = AGE_CHOICES,
    )
    gender = forms.ChoiceField(
        label = 'your gender',
        choices = GENDER_CHOICES,
    )
    number_of_children = forms.ChoiceField(
        label = 'number of children',
        choices = NUMBER_OF_CHILDREN_CHOICES,
    )
    current_edu_level = forms.ChoiceField(
        label = 'education level',
        choices = CURRENT_EDU_LEVEL_CHOICES,
    )
    number_of_units = forms.ChoiceField(
        label = 'number_of_units',
        choices = NUMBER_OF_UNITS_CHOICES,    
    )
    resident_type = forms.ChoiceField(
        label = 'ownership type',
        choices = OWNERSHIP_TYPE_CHOICES,
    )
    rooms_per_unit = forms.ChoiceField(
        label = 'number of rooms',
        choices = NUMBER_OF_ROOMS_CHOICES,
    )
    building_age = forms.ChoiceField(
        label = 'building_age',
        choices = BUILDING_AGE_CHOICES,
    )

    # Turn checkboxes into booleans, or use widgets checkboxinput?
    currently_in_school = forms.BooleanField()
    marital_status_checkbox = forms.forms.BooleanField()


