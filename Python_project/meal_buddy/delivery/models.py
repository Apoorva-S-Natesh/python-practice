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
	name = models.CharField(max_length = 20)
	picture = models.URLField(max_length = 200, default='https://i.pinimg.com/' \
	'736x/19/b1/48/19b148ef0b3b6af0592f6bbb9a2fee68.jpg')
	cuisine = models.CharField(max_length = 200)
	rating = models.FloatField()

class Item(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name = "items") #CASCADE : If the Restaurant is deleted all the tables accessing it will be deleted, related_name = "items" to fetch all the data related to the item
	name = models.CharField(max_length=30)
	description = models.CharField(max_length = 200)
	price = models.FloatField()
	vegetarian = models.BooleanField(null=True, default=False)
	picture = models.URLField(max_length=200, default='https://i.pinimg.com/736x/' \
	'8b/f0/4f/8bf04f38445553c66196f423b74eab1d.jpg')

class Cart(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = "cart")
	items = models.ManyToManyField("Item", related_name = "carts") #To represent one cart can have many items

	def total_price(self):
		return sum(item.price for item in self.items.all())