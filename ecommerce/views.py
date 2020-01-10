
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm, LoginForm
import random

def home_page(request):
	context ={
	"title": "THE OFFICIAL HUMBLE HOTHEADS WEBSITE",
	"content": "Welcome to the home page",
	"premium_content": "YEEAAAHH",
	'n': random.random()

		}
	return render(request, 'home_page.html' , context)



def exclusive_page(request):
	context = {
	"title": "Exclusive Items",
	"content": "Check out the latest exclusive items",
	}
	return render(request, 'home_page.html' , context)
    



def tracksuits_page(request):
	context = {
	"title": "Tracksuits",
	"content": "Tracksuits",
	}

	return render(request, 'home_page.html', context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
	"form": form
	}
	return render(request, "auth/login.html", context)

def register_page(request):
	form = loginForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
	context = {
	"form": form,
	}

	return render(request, "auth/login.html", {context})

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
	"title": "Welcome to our contact page",
	"content": "Please fill in your details to get our latest drops",
	"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data )
	#if request.method == "POST" :
		# print (request.POST) 
		# print (request.POST.get('fullname'))
		# print (request.POST.get('email'))
		# print (request.POST.get('content'))
	return render(request, 'contact/view.html', context)






    





