# 🍽️ Meal Ordering System - Django Web App

This is a Django-based web application for a **meal ordering platform**, designed as a practice project. It supports functionalities for user authentication, restaurant and menu management, item browsing, cart management, and order placement with Razorpay integration for payment.

---

## Features

### Authentication
- **Sign Up & Sign In**: Users can register and log in using their credentials.
- **Admin Access**: A special user (`username='admin'`) is redirected to the admin dashboard.

### Restaurant Management (Admin)
- **Add Restaurant**: Add new restaurants with details like name, cuisine, rating, and image.
- **Update/Delete Restaurant**: Edit or remove existing restaurants.
- **Menu Management**: Add, update, or delete menu items for a restaurant.

### Menu Browsing (Customer)
- **Restaurant Listing**: View available restaurants after login.
- **Menu Viewing**: Browse items from a specific restaurant.

### Cart Functionality
- **Add to Cart**: Customers can add items to their cart.
- **View Cart**: See cart contents with quantity and total price.
- **Remove Items**: Delete items from the cart.

### Checkout & Payment
- **Razorpay Integration**: Seamless payment processing using Razorpay.
- **Order Confirmation**: Upon successful checkout, the cart is cleared and order summary is shown.

---

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, Bootstrap (assumed from template usage)
- **Database**: SQLite (default Django DB)
- **Payment Gateway**: Razorpay

---

## URL Routes

### User Authentication
| URL | Description |
|-----|-------------|
| `/` | Home page |
| `/open_signin` | Sign in form |
| `/open_signup` | Sign up form |
| `/signup` | Register user |
| `/signin` | Authenticate user |

### Restaurant (Admin)
| URL | Description |
|-----|-------------|
| `/open_add_restaurant` | Form to add restaurant |
| `/add_restaurant` | Submit new restaurant |
| `/open_show_restaurant` | List all restaurants |
| `/open_update_restaurant/<id>` | Edit restaurant |
| `/update_restaurant/<id>` | Submit updated restaurant |
| `/delete_restaurant/<id>` | Delete restaurant |

### Menu Management
| URL | Description |
|-----|-------------|
| `/open_update_menu/<restaurant_id>` | View/edit menu items |
| `/update_menu/<restaurant_id>` | Add menu item |
| `/open_update_item/<item_id>` | Edit menu item |
| `/update_item/<item_id>` | Submit updated item |
| `/delete_item/<item_id>` | Delete item |

### Customer Menu & Cart
| URL | Description |
|-----|-------------|
| `/view_menu/<restaurant_id>/<username>` | View restaurant's menu |
| `/add_to_cart/<item_id>/<username>` | Add item to cart |
| `/view_cart/<username>` | View cart |
| `/delete_item_from_cart/<username>/<item_id>` | Remove from cart |

### Checkout & Orders
| URL | Description |
|-----|-------------|
| `/checkout/<username>/` | Checkout via Razorpay |
| `/orders/<username>/` | Order summary page |

---

## Models (Overview)
- `Customer`: Stores user information.
- `Restaurant`: Holds restaurant details.
- `Item`: Menu items for a restaurant.
- `Cart`: One per customer.
- `Cart_Item`: Many-to-many mapping with quantity.

---

## How to Run

```bash
git clone <repo-url>
cd <project-folder>
python manage.py migrate
python manage.py runserver
```

Access the site at: `http://127.0.0.1:8000/`

---

## Notes
- This project is meant for **educational and practice purposes**.
- No user session management or security hashing for passwords implemented.
- All admin privileges are based on username check (`username == 'admin'`).

---

## Future Improvements
- Password hashing and session handling
- Enhanced UI with responsiveness
- Order history and item ratings
- Whole of Delivery System and tracking