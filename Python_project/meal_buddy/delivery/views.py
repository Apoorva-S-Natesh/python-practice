from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from .models import Customer,Restaurant,Item,Cart, Cart_Item
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

import razorpay
from django.conf import settings

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

		#If a user already exists then new oobject is not created
		try:
			Customer.objects.get(username = username)
			return HttpResponse("User exists! Try Signing In!")
		except:
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
		if username == 'admin':
			return render(request, 'delivery/admin_home.html') # Only one user redirected to admin page (username: admin, password: 123)
		else:
			restaurantList = Restaurant.objects.all()
			return render(request, 'delivery/customer_home.html', {"restaurantList" : restaurantList, "username" : username})
	
	except Customer.DoesNotExist:
		return render(request, 'delivery/fail.html')
	
def open_add_restaurant(request):
	return render(request, 'delivery/add_restaurant.html')

def add_restaurant(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		picture = request.POST.get('picture')
		cuisine = request.POST.get('cuisine')
		rating = request.POST.get('rating')

	try:
		Restaurant.objects.get(name = name)
		return HttpResponse("Restaurant Exists")
	except: 
		Restaurant.objects.create(
			name = name,
			picture = picture,
			cuisine = cuisine,
			rating = rating,
		)
	return render(request, 'delivery/admin_home.html')

def open_show_restaurant(request):
	restaurantList = Restaurant.objects.all() #Fetching all the restuarant objects
	return render(request, 'delivery/show_restaurants.html', {"restaurantList" : restaurantList})

def open_update_restaurant(request, restaurant_id):
	restaurant = Restaurant.objects.get(id = restaurant_id)
	return render(request, 'delivery/update_restaurant.html', {"restaurant" : restaurant})

def update_restaurant(request, restaurant_id):
	restaurant = Restaurant.objects.get(id = restaurant_id)
	if request.method == 'POST':
		name = request.POST.get('name')
		picture = request.POST.get('picture')
		cuisine = request.POST.get('cuisine')
		rating = request.POST.get('rating')

		restaurant.name = name
		restaurant.picture = picture
		restaurant.cuisine = cuisine
		restaurant.rating = rating

		restaurant.save()

	restaurantList = Restaurant.objects.all()
	return render(request, 'delivery/show_restaurants.html', {"restaurantList" : restaurantList})

def delete_restaurant(request, restaurant_id):
	restaurant = Restaurant.objects.get(id = restaurant_id)
	restaurant.delete()

	restaurantList = Restaurant.objects.all()
	return render(request, 'delivery/show_restaurants.html', {"restaurantList" : restaurantList})

def open_update_menu(request, restaurant_id):
	restaurant = Restaurant.objects.get(id = restaurant_id)

	return render(request, 'delivery/update_menu.html', {"restaurant" : restaurant})

def open_update_menu(request, restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	itemList = Item.objects.filter(restaurant=restaurant)
	return render(request, 'delivery/update_menu.html', {"itemList" : itemList, "restaurant" : restaurant})


def update_menu(request, restaurant_id):
	restaurant = Restaurant.objects.get(id=restaurant_id)
	
	if request.method == 'POST':
		name = request.POST.get('name')
		description = request.POST.get('description')
		price = request.POST.get('price')
		vegetarian = request.POST.get('is_veg') == 'on'
		picture = request.POST.get('picture')

	try:
		Item.objects.get(name = name, restaurant=restaurant)
		return HttpResponse("Duplicate Item")
	except Item.DoesNotExist: 
		Item.objects.create(
			restaurant = restaurant,
			name = name,
			description = description,
			price = price,
			vegetarian = vegetarian,
			picture = picture,
		)

	#itemList = Item.objects.all()
	itemList = restaurant.items.all()
	#itemList = Item.objects.filter(restaurant=restaurant)
	return render(request, 'delivery/update_menu.html', {"itemList": itemList, "restaurant": restaurant})
	
	#return HttpResponse("Received")

def open_update_item(request, item_id):
	item = Item.objects.get(id = item_id)
	return render(request, 'delivery/upadate_item.html', {"item" : item})

def update_item(request, item_id):
	item = Item.objects.get(id = item_id)
	if request.method == 'POST':
		name = request.POST.get('name')
		description = request.POST.get('description')
		price = request.POST.get('price')
		vegetarian = request.POST.get('is_veg') == 'on'
		picture = request.POST.get('picture')

		item.name = name
		item.description = description
		item.price = price
		item.vegetarian = vegetarian
		item.picture = picture

		item.save()

	restaurant = item.restaurant
	itemList = Item.objects.filter(restaurant=restaurant)
	return render(request, 'delivery/update_menu.html', {"itemList": itemList, "restaurant": restaurant})

def delete_item(request, item_id):
	item = Item.objects.get(id = item_id)
	item.delete()

	restaurant = item.restaurant
	itemList = Item.objects.filter(restaurant=restaurant)
	return render(request, 'delivery/update_menu.html', {"itemList": itemList, "restaurant": restaurant})

def view_menu(request, restaurant_id, username) :
	restaurant = Restaurant.objects.get(id=restaurant_id)
	itemList = Item.objects.filter(restaurant=restaurant)
	return render(request, 'delivery/customer_menu.html', {"itemList": itemList, "restaurant": restaurant, "username":username})

def add_to_cart(request, item_id, username) :
	item = Item.objects.get(id = item_id)
	customer = Customer.objects.get(username = username)
	cart, created = Cart.objects.get_or_create(customer = customer) # If there is no item in the cart then it doesnt exists, then create a cart
	#creates is avariable (bool) considering if variable is present or not, if present returns the same if not its createed
	
	cart.items.add(item)

	# Create or update Cart_Item for quantity tracking
	cart_item, created = Cart_Item.objects.get_or_create(cart=cart, menu_item=item)
	if not created:
		cart_item.quantity += 1
		cart_item.save()

	messages.success(request, f"{item.name} has been added to your cart.")
	return redirect(reverse('view_menu', args=[item.restaurant.id, username]))
 	# return HttpResponse("added to cart")

def view_cart(request, username):
	customer = Customer.objects.get(username = username)
	cart = Cart.objects.filter(customer = customer).first() #Fetching all the objects from Cart table which belong to the perticular customer and fetching the first of them
	# That returns a list of the latest cart
	cart_items = cart.cart_items.all() if cart else [] # if cart objects exists then give all items present in the cart if not gives an empty list
	total_price = sum(item.get_price() for item in cart_items)

	#return HttpResponse(f"In {username}'s cart")
	return render(request, 'delivery/cart.html', {"items": cart_items, "total_price": total_price, "username":username})

def delete_item_from_cart(request, username, item_id):
	cart_item = get_object_or_404(Cart_Item, id=item_id)
	cart_item.delete()

	# return HttpResponse("Item deleted from cart")
	messages.success(request, "Item successfully removed from cart.")
	return redirect(reverse('view_cart', args=[username]))

def checkout(request, username):
    # Fetch customer and their cart
    customer = get_object_or_404(Customer, username=username)
    cart = Cart.objects.filter(customer=customer).first()
    cart_items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    if total_price == 0:
        return render(request, 'delivery/checkout.html', {
            'error': 'Your cart is empty!',
        })

    # Initialize Razorpay client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Create Razorpay order
    order_data = {
        'amount': int(total_price * 100),  # Amount in paisa
        'currency': 'INR',
        'payment_capture': '1',  # Automatically capture payment
    }
    order = client.order.create(data=order_data)

    # Pass the order details to the frontend
    return render(request, 'delivery/checkout.html', {
        'username': username,
        'cart_items': cart_items,
        'total_price': total_price,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'order_id': order['id'],  # Razorpay order ID
        'amount': total_price,
    })


# Orders Page
def orders(request, username):
    customer = get_object_or_404(Customer, username=username)
    cart = Cart.objects.filter(customer=customer).first()

    # Fetch cart items and total price before clearing the cart
    cart_items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    # Clear the cart after fetching its details
    if cart:
        cart.items.clear()

    return render(request, 'delivery/orders.html', {
        'username': username,
        'customer': customer,
        'cart_items': cart_items,
        'total_price': total_price,
    })