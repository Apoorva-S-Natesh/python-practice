from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def index(request):
	return render(request, 'delivery/index.html')

def open_signin(request):
	return render(request, 'delivery/signin.html')

def open_signup(request):
	return render(request, 'delivery/signup.html')

def signup(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		address = request.POST.get('address')

		Customer.objects.create(
			username = username, 
			password = password,
			email = email,
			mobile = mobile,
			address = address,
		)

	#return HttpResponse("Request for signup received")
	return render(request, 'delivery/signin.html')

def signin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

	#Need to check if this username and password exits in database
	#if get() works then it returns the CUstomer object if the user does not exits the we get an Exception
	try:
		Customer.objects.get(username = username, password = password) # instance variable usrename = fetched data username
		return render(request, 'delivery/success.html')
	
	except Customer.DoesNotExist:
		return render(request, 'delivery/fail.html')