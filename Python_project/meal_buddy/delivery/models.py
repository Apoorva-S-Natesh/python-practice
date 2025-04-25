from django.db import models

# Create your models here.
"""Extend to Model class inside models module or package"""

class Customer(models.Model): 
	username = models.CharField(max_length = 20) #Accepting data from frontend
	password = models.CharField(max_length = 20)
	email = models.CharField(max_length = 20)
	mobile = models.CharField(max_length = 10) #Taking mobile as string itself
	address = models.CharField(max_length = 50)

class Restaurant(models.Model):
	restaurantName = models.CharField(max_length = 20) #Accepting data from frontend
	picutreUrl = models.URLField(max_length = 200, default='https://img.freepik.com/freie-psd/restaurant-vintage-abzeichen-vorlagen-psd-set-remixed-aus-gemeinfreien-kunstwerken_53876-141767.jpg?t=st=1745589179~exp=1745592779~hmac=18565adbc457db41ae98630d4e960d602f2231fe3813bff947dd475a6f2ad99f&w=826')
	cuisine = models.CharField(max_length = 200)
	rating = models.FloatField()