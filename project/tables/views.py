from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
# from django.db.models import Q

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

import json
import pprint


from .forms import UserForm, LoginForm, SearchForm
from .models import Neighborhood, Ages, Economic, SchoolEducation, Building, Demographic, UnitValue, UnitDescription
from .algorithm import get_results

class Index(View):
    def get(self, request):
        context = {}
        # check to see if someone is already logged in
        if request.user.is_authenticated(): 
            # get their username  
            username = request.user.username
            context = {
                'username': username,
            }
        user_form = UserForm()
        login_form = AuthenticationForm()
        context ["user_form"] = user_form
        context ["login_form"] = login_form
        return render(request, "index.html", context)


class Register(View):
    def post(self, request):
        data = request.POST
        user_form = UserForm(data)
        if user_form.is_valid():
            user = user_form.save()
            return JsonResponse({"Message": "Register succesfull", "success": True})
        else:
            return JsonResponse ({"response":"Invalid information", 'success' : False, 'errors': user_form.errors })


class Login(View):
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session.set_expiry(30000)
            return JsonResponse({"username":username, "success": True})
        else:
            return JsonResponse({'errors': form.errors})


class Logout(View):
    def post(self, request):
        print(request)
        logout(request) # django built in logout 
        return JsonResponse ({"Message":"Logout Successful"})


class Search(View):
	def post(self,request):
		form = SearchForm(request.POST)
		form.is_valid()
		cd = form.cleaned_data
		f = self.get_table_fields(form.fields, cd)
		nb_list = get_results(f)
		print(nb_list)
		return JsonResponse({"success": True})

	def get_table_fields(self, form_fields, cleaned_data):
		field_choice_dict = {}
		for field in form_fields:
			# charfields, not choicefields
			if field == 'income_level_range':
				field_choice_dict[field] = cleaned_data.get(field, 'empty')
			elif field == 'price_range': 
				field_choice_dict[field] = cleaned_data.get(field, 'empty')
			elif field == 'commute_address':
				field_choice_dict[field] = cleaned_data.get(field, 'empty')
			elif field == 'commute_time_range':
				field_choice_dict[field] = cleaned_data.get(field, 'empty')
			# get field name, not html form input name
			else:
				# print('1: ', field)
				field_choices = dict(form_fields[field].choices)
				# print('2: ', field_choices)
				cleaned_choice = cleaned_data.get(field, 'empty')
				choice = field_choices.get(cleaned_choice, 'empty')
				# choice = field_choices[cleaned_data[field]]
				# print('3: ', choice)
				field_choice_dict[field] = choice
		return field_choice_dict

class Results(View):
    def post(self,request):
        pass










