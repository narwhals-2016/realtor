from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
# from django.db.models import Q

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import json
# import twython import Twython

# from .forms import UserForm, LoginForm, CreateForm
from .models import Neighborhood, Ages, Economic, SchoolEducation, Building, Demographic, UnitValue, UnitDescription

# Create your views here.
class Index(View):
    def get(self, request):

        return render(request, "form.html")
