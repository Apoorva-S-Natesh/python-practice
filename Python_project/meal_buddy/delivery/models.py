from django.db import models

# Create your models here.
"""Extend to Model class inside models module or package"""

class Customer(models.Model): 
	username = models.CharField(max_length = 20) #Accepting data from frontend
	password = models.CharField(max_length = 20)
	email = models.CharField(max_length = 20)
	mobile = models.CharField(max_length = 10) #Taking mobile as string itself
	address = models.CharField(max_length = 50)
