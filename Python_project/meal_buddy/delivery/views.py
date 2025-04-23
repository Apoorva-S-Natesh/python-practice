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