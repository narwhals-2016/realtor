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

import requests 
from allauth.socialaccount.models import SocialToken
from .creeper import hasGraduated, genderfind, agefind

from .algorithm import get_results


class Index(View):
	def get(self, request):
		if request.user.is_authenticated() and not request.session.get('access_token'):
			request.session['access_token'] = str(SocialToken.objects.get(account__user=request.user, account__provider='facebook'))
			r = requests.get('https://graph.facebook.com/me?access_token='+request.session['access_token']+'&fields=education,birthday,gender')
			print(r.json())
			gender = genderfind(r.json())
			isgraduated = hasGraduated(r.json())
			age = agefind(r.json())
			print(age)


			context = {}
			username = request.user.username
			context['username']= username
	
			user_form = UserForm()
			login_form = LoginForm()

			context ["user_form"] = user_form
			context ["login_form"] = login_form
			context["isgraduated"] = isgraduated
			context["gender"] = gender
			context["age"]= age 

			return render(request, "index.html", context)

		context = {}
		# check to see if someone is already logged in
		if request.user.is_authenticated(): 
			# get their username  
			username = request.user.username

			context['username']= username
	

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
		body = request.body.decode()
		if not body: 
			return JsonResponse ({"response":"Missing Body"})
		data = json.loads(body)

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
		field_mappings = self.map_table_fields(form.fields, cd)
		nb_list = get_results(field_mappings)
		print(nb_list)
		return JsonResponse({"success": True})

	def map_table_fields(self, form_fields, cleaned_data):
		field_values_list = [
			'income_level_range',
			'price_range',
			'commute_address',
			'commute_time_range',
			'night_life_importance',
		]
		field_choice_dict = {}
		for field in form_fields:
			if field in field_values_list:
				print('FVL - field', field)
				# the forms' choices don't match the table's fields, we want the raw form submission
				field_choice_dict[field] = self.map_values(field, cleaned_data)
				print('FVL - val', field_choice_dict[field])
			else:
				# get field name, not html form input name
				field_choices = dict(form_fields[field].choices)
				cleaned_choice = cleaned_data.get(field, 'empty')
				choice = field_choices.get(cleaned_choice, 'empty')
				field_choice_dict[field] = choice
		return field_choice_dict
	
	def map_values(self, field, cleaned_data):
		return cleaned_data.get(field, 'empty')

class Results(View):
	def post(self,request):
		pass










