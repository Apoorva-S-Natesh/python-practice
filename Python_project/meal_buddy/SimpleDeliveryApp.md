## a Simple Food Delivery App (MVP)

**Example feature:** A user can view a list of available food items.

---

## Coding Flow

---

### 1: Create a Django Project and App

```bash
django-admin startproject foodie
cd foodie
python manage.py startapp delivery
```

---

### 2: Register the App in `settings.py`

Open `foodie/settings.py`, add `'delivery'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'delivery',
]
```

---

### 3: Define the Model (`delivery/models.py`)

Start with the data: What is being stored?

```python
from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
```

Then run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4: Create Admin Interface (Optional but useful)

In `delivery/admin.py`:

```python
from django.contrib import admin
from .models import FoodItem

admin.site.register(FoodItem)
```

Create a superuser to access admin:

```bash
python manage.py createsuperuser
```

---

### 5: Create a View (`delivery/views.py`)

Now you decide what to do with that data – for now, **list all food items**.

```python
from django.shortcuts import render
from .models import FoodItem

def food_list(request):
    items = FoodItem.objects.filter(available=True)
    return render(request, 'delivery/food_list.html', {'items': items})
```

---

### 6: Add URL Patterns

#### Project-level `foodie/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('delivery.urls')),  # Include app URLs
]
```

#### App-level `delivery/urls.py` (create this file):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
]
```

---

### 7: Create Template (`delivery/templates/delivery/food_list.html`)

Make sure the folder structure is correct: `delivery/templates/delivery/food_list.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Food Items</title>
</head>
<body>
    <h1>Available Food</h1>
    {% for item in items %}
        <div>
            <h2>{{ item.name }} - ${{ item.price }}</h2>
            <p>{{ item.description }}</p>
        </div>
    {% empty %}
        <p>No food items available.</p>
    {% endfor %}
</body>
</html>
```

---

### 8: Run the Server and Test

```bash
python manage.py runserver
```

Go to `http://127.0.0.1:8000/` — you should see the list of food items.

---

## Summary of Coding Order

| Step | File                        | What You Do                      |
| ---- | --------------------------- | -------------------------------- |
| 1    | `models.py`                 | Define data structure            |
| 2    | Terminal                    | `makemigrations`, `migrate`      |
| 3    | `views.py`                  | Define logic for displaying data |
| 4    | `urls.py` (app and project) | Route URLs to views              |
| 5    | `templates/`                | Create HTML structure            |
| 6    | `admin.py` (optional)       | Add model to Django admin        |


